---
title: "cloudflare/computer"
source: GitHub Trending
url: https://github.com/cloudflare/computer
date: 2026-08-07
published_at: 2026-08-07T04:23:14.690370+00:00
tag: 工具开源
item_id: d57720eb32ca3cfb
---
Cloudflare Computer is a virtual filesystem that lives inside a
Durable Object. The Durable Object holds the authoritative state in
SQLite and exposes one pluggable execution surface through
`workspace.runtime`. Three backends ship today:

- **Container** projects the SQLite state into a sandbox container as
a real FUSE mount. A sandbox-side daemon (`computerd` ) mounts the state
as a filesystem and syncs changes back over a capnweb RPC channel.
Full Linux userland, real binaries, real network.
- **Isolate shell** runs[just-bash](https://github.com/vercel-labs/just-bash) in a Dynamic Worker. It reaches the authoritative Workspace over
Workers RPC, so there is no second store or sync round trip.
- **Isolate JavaScript** runs an ECMAScript module in a fresh Dynamic
Worker with structured input/results, durable relative imports,
configured libraries, Workspace-backed`node:fs/promises` , and trusted`ws:git` and`ws:artifacts` modules.

A Workspace may register multiple backends under stable IDs.
`workspace.runtime.exec(source, { backend })` is the single execution
entry point; the selected backend defines whether `source` is a shell
command or an ECMAScript module. Backends connect lazily on first use.

Workspace can also be constructed without a backend at all, giving callers the filesystem on its own.

Important

**PREVIEW ONLY** This package is provided as a preview for feedback only.
APIs are unstable and the design is subject to change.

Suitable for experiments, exploration and prototypes. It is NOT suitable for production use at this time.

The specification under [`docs/`](https://github.com/cloudflare/computer/blob/main/docs) is forward-looking — read it for
intent, not as description of the code today.

If you want to build on Cloudflare Computer, install
[`@cloudflare/computer`](https://github.com/cloudflare/computer/blob/main/packages/computer/README.md) and follow that
package's README — it has the installation steps, the entrypoint map,
and worked examples of the `fs` and `runtime` surfaces.

To contribute feedback, see [`CONTRIBUTING.md`](https://github.com/cloudflare/computer/blob/main/CONTRIBUTING.md).
Approved collaborators should follow [`COLLABORATORS.md`](https://github.com/cloudflare/computer/blob/main/COLLABORATORS.md)
for setup, build, and test instructions.

The [`examples/`](https://github.com/cloudflare/computer/blob/main/examples) directory holds runnable consumers of the
public surface. Each is a Worker workspace with its own README.

- [`examples/container`](https://github.com/cloudflare/computer/blob/main/examples/container) — runs`computerd` inside a
container, mounts a workspace, and talks to a Durable Object over
capnweb. A`write` /`read` /`exec` HTTP surface.
- [`examples/worker-shell`](https://github.com/cloudflare/computer/blob/main/examples/worker-shell) — same HTTP surface as the
container example, but the shell runs[just-bash](https://github.com/vercel-labs/just-bash) in a Dynamic Worker loaded through`env.LOADER` . No container.
- [`examples/worker-javascript`](https://github.com/cloudflare/computer/blob/main/examples/worker-javascript) — mirrors`worker-shell` , but`exec` evaluates an ECMAScript module in a Dynamic
Worker instead of running a shell command.
- [`examples/think`](https://github.com/cloudflare/computer/blob/main/examples/think) — a[`@cloudflare/think`](https://www.npmjs.com/package/@cloudflare/think) chat agent that uses the workspace as its working directory, reachable
from a terminal.
- [`examples/think-compare-runtimes`](https://github.com/cloudflare/computer/blob/main/examples/think-compare-runtimes) —
a web UI that runs the same agent task against the container and
worker runtimes side by side.
- [`examples/tutorial`](https://github.com/cloudflare/computer/blob/main/examples/tutorial) — a step-by-step build: one
endpoint, one agent that writes a markdown recipe card on the host and
runs`pandoc` on it in the container to produce a PDF.
- [`examples/artifacts`](https://github.com/cloudflare/computer/blob/main/examples/artifacts) — generates a Worker project
in a workspace and publishes it to Cloudflare Artifacts as a
clone-ready repo.
- [`examples/assets`](https://github.com/cloudflare/computer/blob/main/examples/assets) — turns a prompt into an image with
Workers AI, writes it to the workspace, and returns a shareable link
through`@cloudflare/computer/assets` .

The repo is a small monorepo. Each package has its own README with package-specific status and usage notes.

- [`packages/dofs`](https://github.com/cloudflare/computer/blob/main/packages/dofs/README.md) (`@cloudflare/dofs` ) —
Durable Object SQLite-backed virtual filesystem, sync protocol
building blocks, and a`@platformatic/vfs` provider for Node.
- [`packages/rpc`](https://github.com/cloudflare/computer/blob/main/packages/rpc/README.md) (`@cloudflare/computer-rpc` ) — capnweb wire types and
server/client helpers shared between the Durable Object and`computerd` .
- [`packages/computerd`](https://github.com/cloudflare/computer/blob/main/packages/computerd/README.md) (`@cloudflare/computerd` ) — the`computerd` daemon: a FUSE mount plus
HTTP/WebSocket RPC server that runs inside the sandbox container.
- [`packages/computer`](https://github.com/cloudflare/computer/blob/main/packages/computer/README.md) (`@cloudflare/computer` ) — the top-level Computer package
consumed by Durable Objects. Work in progress.
- [`packages/computer-computerd-linux-x64`](https://github.com/cloudflare/computer/blob/main/packages/computer-computerd-linux-x64/README.md) — private Docker image context for the prebuilt`computerd` linux-x64
binary. The image, not an npm package, is the release artifact.

computerd's FUSE mount beats real disk on metadata-heavy work and
trails it on large sequential I/O. See
[`docs/19_performance.md`](https://github.com/cloudflare/computer/blob/main/docs/19_performance.md) for the full `fs-bench`
numbers, a `cloudflare/sandbox-sdk` `npm install` comparison, and how
to reproduce them.

- [`docs/`](https://github.com/cloudflare/computer/blob/main/docs/README.md) — design specification. Forward-looking;
treat as intent.
- [`docs/19_performance.md`](https://github.com/cloudflare/computer/blob/main/docs/19_performance.md) — filesystem benchmarks.

We accept bug reports, fix proposals, feature requests, and design
proposals through issues and discussions. We do not accept unsolicited
pull requests. See [`CONTRIBUTING.md`](https://github.com/cloudflare/computer/blob/main/CONTRIBUTING.md) for the public
contribution paths.

Approved collaborators should follow
[`COLLABORATORS.md`](https://github.com/cloudflare/computer/blob/main/COLLABORATORS.md) for setup, formatting, testing,
commit message, and pull request conventions.

If you're working in this repo as an agent, start with
[`AGENTS.md`](https://github.com/cloudflare/computer/blob/main/AGENTS.md) and the skills under
[`.agents/skills/`](https://github.com/cloudflare/computer/blob/main/.agents/skills).

MIT. See [`LICENSE`](https://github.com/cloudflare/computer/blob/main/LICENSE).
