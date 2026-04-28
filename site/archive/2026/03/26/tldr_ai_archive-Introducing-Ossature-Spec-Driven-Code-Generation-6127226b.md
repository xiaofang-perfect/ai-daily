---
title: "Introducing Ossature: Spec-Driven Code Generation"
source: TLDR AI · 2026-03-25
url: https://ossature.dev/blog/introducing-ossature/?utm_source=tldrai
date: 2026-03-26
published_at: 2026-03-25T12:00:00+00:00
tag: 工具开源
item_id: 6127226bba3801eb
---
# Introducing Ossature: Spec-Driven Code Generation

LLMs are getting good at generating code. Really good, actually. When you give a model a focused task, a single function or a well-scoped module, you'll often get back something that's good enough to ship. But ask it to produce a whole project with a storage layer, a CLI, a web interface, and shared types across all of them, and things start to fall apart. The model can write each piece just fine. The problem is that nothing ensures the pieces fit together.

The tooling gap is real. OpenAI's team recently wrote about [building an entire product with zero manually-written code](https://openai.com/index/harness-engineering/). They spent five months not writing code, but building what they call a *harness*: the environment, constraints, and feedback loops that let agents produce reliable software at scale. Custom linters, structural tests, a curated knowledge base in the repo, agents that periodically sweep for architectural drift. They found that the hard problem isn't code generation itself, it's designing the scaffolding that keeps a growing codebase coherent. Agents are most effective in environments with strict boundaries and predictable structure, and when an agent struggles, the fix is almost never "try harder" but rather "what capability or constraint is missing?"

Several people in the [Exploring Gen AI series on Martin Fowler's blog](https://martinfowler.com/articles/exploring-gen-ai.html) have been thinking about these problems. [Birgitta Böckeler's piece on harness engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) observed that for maintainable AI-generated code you have to constrain the solution space, trading "generate anything" flexibility for reliability. She also raised a question we think about a lot: can these harnessing techniques work for existing applications, or only for projects built from scratch with a harness in mind? [Kief Morris's piece on humans and agents](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html) framed it as the difference between being *in* the loop (inspecting every line) versus *on* the loop (building the harness that produces the right output). The idea is that rather than personally reviewing everything an agent produces, you invest in making it better at producing it. And then there's [Böckeler's look at spec-driven development tools](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) like Kiro, spec-kit, and Tessl, where she found that many of the current tools create elaborate multi-file workflows that end up feeling like overkill for real problems, and that agents frequently ignore their own generated instructions anyway. She asked whether some of these tools are a "Verschlimmbesserung", making things worse in the attempt to make them better.

These are all real problems. Ossature is our attempt at addressing some of them.

It's an open-source harness for spec-driven code generation. You write specifications describing *what* your software should do. Ossature validates them, has an LLM audit them for ambiguities and gaps, produces a build plan you can review and edit, then generates code one task at a time. Each task gets only the context it needs, not a 128K token dump of everything.

## How it works

A project is a collection of spec files. Each spec uses a Markdown-based format called SMD that describes behavior: what a module accepts, what it returns, what happens on errors, and how the internals should work. Here's a trimmed version of the encode requirement from [Qoizig](https://github.com/ossature/ossature-examples/tree/main/qoizig), a QOI image codec in Zig:

```
# Qoizig
@id: QOI_CODEC
@status: draft
@priority: high
@depends: []
## Requirements
### Encode Command (`qoizig encode`)
Reads a source image file (PPM P6 for RGB, PAM P7 for RGBA)
and encodes it into a QOI file.
**Accepts:**
- `input` (positional, required): Path to the source PPM/PAM file.
- `output` (positional, required): Path for the resulting QOI file.
**Returns:**
- A QOI file written to disk.
- A stdout message: `Encoded {width}x{height} image to {output}`.
**Behavior:**
1. Parse input file header (PPM/PAM).
2. Initialize pixel history `index[64]` to rgba(0,0,0,0).
Initialize `previous_pixel` to `{r: 0, g: 0, b: 0, a: 255}`.
3. Iterate through pixels (Left to Right, Top to Bottom):
- **Run check**: If current pixel matches `previous_pixel`,
increment run counter. If run == 62 or next pixel differs,
write `QOI_OP_RUN` (tag `b11`, 6-bit run with bias -1).
- **Diff check**: If `dr`, `dg`, `db` are each in [-2, 1]
and alpha is unchanged, write `QOI_OP_DIFF` (tag `b01`,
2-bit per channel with bias 2). Differences use wraparound:
`1 - 2 = 255`, `255 + 1 = 0`.
- **Luma check**: If `dg` in [-32, 31] and `dr-dg`, `db-dg`
in [-8, 7] and alpha unchanged, write `QOI_OP_LUMA`.
- **Fallback**: Write `QOI_OP_RGB` (tag `0xFE`) if only RGB
changed, or `QOI_OP_RGBA` (tag `0xFF`) if alpha changed.
4. Write 8-byte End Marker.
**Errors:**
- Input file not found -> print error and exit code 1.
- Invalid PPM/PAM header -> print error and exit code 1.
```


This is the kind of detail that matters. "Handle invalid input" leaves too much room for interpretation. But "wraparound arithmetic where `1 - 2 = 255`

" or "run-lengths capped at 62 because 63 and 64 collide with the RGB/RGBA tags" are things the LLM can actually implement correctly from. The more concrete the spec, the less guessing.

You can also write an architecture file (AMD) that pins down components, file paths, and interface signatures if you want more control. If you skip it, the LLM infers the architecture during audit.

## Three stages: validate, audit, build

```
ossature init qoizig && cd qoizig
# write specs in specs/
ossature validate
ossature audit
# review .ossature/plan.toml
ossature build
```


graph LR S[(QOI_CODEC.smd)] --> V([ossature validate]) V --> A([ossature audit]) A --> P[(plan.toml)] P --> B([ossature build]) B --> O1[(build.zig)] B --> O2[(src/qoi.zig)] B --> O3[(src/encoder.zig)] B --> O4[(src/decoder.zig)] B --> O5[(src/image_io.zig)] B --> O6[(src/main.zig)]

**Validate** parses every spec and checks that all `@depends`

targets exist, all architecture files reference real specs, there are no duplicate components, and there are no cycles. No LLM involved, it's instant.

**Audit** sends your specs to an LLM for semantic review. It catches ambiguities, contradictions, and gaps. If a spec's example output shows ISO timestamps but the requirement says SQLite's space-separated format, the audit flags it. After review it generates a build plan, a TOML file listing every task in dependency order, what spec sections feed into each task's prompt, what files get injected from earlier tasks, and what verification command runs after generation.

The plan is human-readable and human-editable. You can reorder tasks, change verify commands, skip tasks, or add notes before building. Here's what a couple of tasks look like in the Qoizig plan:

```
[[task]]
id = "002"
spec = "QOI_CODEC"
title = "QOI Types & Constants"
outputs = ["src/qoi.zig"]
depends_on = ["001"]
spec_refs = [
"QOI_CODEC:QOI Format Fundamentals",
"QOI_CODEC:Constraints",
]
verify = "zig build --summary all"
inject_files = ["build.zig", "src/main.zig"]
context_files = ["qoi_specification.md"]
[[task]]
id = "003"
spec = "QOI_CODEC"
title = "QOI Encoder Implementation"
outputs = ["src/encoder.zig"]
depends_on = ["001", "002"]
spec_refs = [
"QOI_CODEC:QOI Format Fundamentals",
"QOI_CODEC:Constraints",
]
verify = "zig build --summary all"
inject_files = ["build.zig", "src/main.zig", "src/qoi.zig"]
context_files = ["qoi_specification.md"]
```


You can see what's going on here: `spec_refs`

controls which parts of the spec go into the prompt, `inject_files`

is what the task can see from earlier tasks, `outputs`

is what it writes, and `verify`

is the command that checks whether the result actually compiles.

Here's the full Qoizig task graph. Each arrow means "depends on output from":

graph TB T1([001: Scaffold]) --> T2[002: Types & Constants] T1 --> T6[006: PPM/PAM I/O] T2 --> T3[003: Encoder] T2 --> T4[004: Decoder] T3 & T4 --> T5[005: Codec Tests] T6 --> T7[007: I/O Tests] T2 & T3 & T4 & T6 --> T8[008: CLI & Main] T8 --> T9[009: Integration Tests]

**Build** executes the plan task by task. For each task Ossature assembles a prompt from the project brief, relevant spec sections, interface files from upstream specs, and output from earlier tasks. The LLM generates code. A verification command runs. If it fails, a separate fixer agent reads the errors and tries to repair the code, up to three attempts. Every prompt and response is saved to `.ossature/tasks/`

so when something goes wrong at task 14 you can read the logs instead of guessing.

sequenceDiagram participant O as Ossature participant L as LLM participant V as Verify loop Each task in plan O->>L: spec refs + inject files + context L-->>O: generated code O->>V: run verify command alt passes V-->>O: ok else fails V-->>O: errors loop Up to 3 fix attempts O->>L: errors + code L-->>O: fixed code O->>V: re-verify end end O->>O: save prompt + response to .ossature/tasks/ end

## Narrow context and deterministic boundaries

One of the things the OpenAI team emphasized was that agents work best when the environment is predictable and constrained. Each build task in Ossature sees only what it needs. Look at task 003 in the plan above: it gets `src/qoi.zig`

injected because it needs the `Pixel`

struct, the `ChannelDiff`

helpers, and the chunk tag constants. But it doesn't see `src/image_io.zig`

or `src/main.zig`

's CLI parsing. The prompt for the encoder task looks roughly like this:

```
<specification_context>
(the "QOI Format Fundamentals" and "Constraints" sections
from the spec, selected by spec_refs)
</specification_context>
<dependency_files>
- build.zig (1996 bytes)
- src/main.zig (1560 bytes)
- src/qoi.zig (10055 bytes)
</dependency_files>
<context_files>
- qoi_specification.md (the actual QOI spec document)
</context_files>
<task>
Implement the QOI encoder...
Files to produce: src/encoder.zig
</task>
```


graph LR subgraph Visible["Task 003 context"] direction TB SR(["spec: Format, Constraints"]) IF1[(build.zig)] IF2[(src/main.zig)] IF3[(src/qoi.zig)] CF(["ctx: qoi_specification.md"]) end subgraph Hidden["Not visible"] direction TB H1[(src/image_io.zig)] H2[(src/decoder.zig)] H3[CLI parsing] end Visible --> OUT[(src/encoder.zig)]

The LLM generates `src/encoder.zig`

against the types defined in `src/qoi.zig`

. It can call `Pixel.hash()`

, use `ChannelDiff.fitsSmallDiff()`

, reference `QOI_OP_DIFF`

, and so on. But it can't see or depend on anything else. Less context means less room for the model to get confused or drift off.

In multi-spec projects this matters even more. Specs can depend on each other with `@depends`

, and downstream specs only see the public interface of their dependencies, not the implementation. Like a header file in C, the interface is the only thing other specs can see. This is what Böckeler was asking about when she said she couldn't quite imagine what "parse data shapes at the boundary" looks like in practice. In Ossature, the boundary is the interface file, and it's enforced by the build system, not by hoping the LLM remembers a rule from a markdown file.

## Incremental builds and observability

Builds are incremental: every input gets a SHA-256 checksum, so when you change a spec, only the affected tasks rebuild. You can iterate on one part of your project without regenerating everything. Combined with the full logging mentioned above, this is what Morris's "on the loop" model requires: you can see exactly what the harness is doing and improve it when it falls short.

## Minimal by design

Böckeler noted that the SDD tools she tried created elaborate workflows that felt like overkill. Kiro turned a small bug fix into four user stories with sixteen acceptance criteria. Spec-kit generated piles of markdown files for a medium-sized feature. We've tried to avoid this. One spec file per module. One build plan for the whole project. The format is minimal, metadata fields at the top, then sections you actually need. You don't have to define user stories or acceptance criteria unless they're useful. The spec describes behavior, the plan describes tasks, and you can read both in a few minutes.

She also observed that agents frequently ignored their own generated instructions, even with larger context windows. We don't rely on the LLM remembering instructions across tasks. Each task gets its own prompt assembled from scratch with exactly the spec sections, interface files, and upstream output it needs. There's no accumulated conversation history to drift from.

## Verification in the loop

One thing Böckeler noted was missing from the OpenAI write-up: verification of functionality and behavior. Their harness focused on internal quality and maintainability, but didn't say much about whether the software actually does what it's supposed to. Ossature has verification built into the build loop. Every task has a `verify`

command that runs after code generation. In the Qoizig project that's `zig build --summary all`

for implementation tasks and `zig build test --summary all`

for test tasks. If verification fails, a fixer agent gets the error output and tries to repair the code. It's not a full test suite, but it catches a lot of breakage at generation time rather than after.

## Existing projects

Böckeler raised the question of whether harnesses can work for existing applications or only for greenfield projects built with a harness in mind. Right now, Ossature is primarily a greenfield tool. You write specs, you generate code from scratch.

But spec-driven code generation for existing projects is one of the first things we're working on. You could write specs for new modules that depend on existing code, inject existing files as context, and generate just the new parts. The challenge is making this feel natural rather than bolted on. We don't have a good answer yet and we don't want to pretend we do.

## Current status

Ossature is at version **0.0.1**, this is the first public release. While the project is in the 0.x series, the API, spec formats, and CLI should be considered **unstable**. Things will change, sometimes in breaking ways, as we learn from real usage. We follow [Semantic Versioning](https://semver.org/) so breaking changes will be reflected in version bumps.

It works with Anthropic, OpenAI, Mistral, Google, and most other hosted providers, as well as local models through Ollama. Requires Python 3.14+.

## Get started

Ossature is MIT-licensed and open source.

```
pip install ossature
# or run directly
uvx ossature init my-project
```


The [quickstart](https://docs.ossature.dev/getting-started/quickstart.html) will get you to a generated project in a few minutes. The [workflow walkthrough](https://docs.ossature.dev/getting-started/workflow.html) goes deeper into each stage.

[Documentation](https://docs.ossature.dev) / [GitHub](https://github.com/ossature/ossature) / [Example projects](https://github.com/ossature/ossature-examples) (Spenny in Python, Qoizig in Zig, Markman in Rust, Math Quest in Lua)

We'd love to hear what you build with it.
