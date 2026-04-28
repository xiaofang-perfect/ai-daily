---
title: "From 300KB to 69KB per Token: How LLM Architectures Solve the KV Cache Problem"
source: Hacker News
url: https://news.future-shock.ai/the-weight-of-remembering/
date: 2026-03-29
published_at: 2026-03-28T22:42:23+00:00
tag: 论文研究
item_id: df48c69a98571e40
---
[Sci-Fi Saturday](https://news.future-shock.ai/tag/sci-fi-saturday/)

# The Weight of Remembering

How the KV cache gives every AI conversation a physical weight in silicon, and what happens when the memory runs out.

![Watercolor illustration of a library table with papers and index cards being pulled into a vortex while books on shelves remain undisturbed](/content/images/size/w1200/2026/03/weight-of-remembering.jpg)

*This one leans more technical than our usual Sci-Fi Saturday fare. Stick with it, we get to the sci-fi by the end.*

## What KV Cache Actually Is

Someone types a forty-three-character question into ChatGPT, some throwaway query about dinner recipes or the capital of Mongolia. Before the first word of the response appears, those characters have been split into tokens, each token multiplied through billions of parameters to produce three vectors: a query, a key, and a value. The key-value pairs land in GPU memory, where they sit physically as bytes on a chip. That stored state is the model's awareness of the conversation, not a metaphor but a memory address.

The key-value cache exists for a practical reason. Without it, generating each new token would require reprocessing every previous token in the conversation from scratch. A 2,000-token exchange would mean re-reading the entire history 2,000 times. The KV cache eliminates that redundancy. Once a token's key-value pair is computed and stored, it stays. The next token only needs to attend to what's already cached. Computation drops from quadratic to linear.

Sebastian Raschka's [LLM Architecture Gallery](https://sebastianraschka.com/llm-architecture-gallery/?ref=news.future-shock.ai) visualizes this mechanism across dozens of model families, and the numbers attached to each architecture make the weight tangible. GPT-2's KV cache costs 300 KiB per token in Raschka's comparison. That means a 4,000-token conversation occupies roughly 1.2 GB of GPU memory just for the cache, separate from the model weights themselves. [Micron's engineering blog](https://www.micron.com/about/blog/company/insights/from-buzzword-to-bottom-line-understanding-the-why-behind-kv-cache-in-ai?ref=news.future-shock.ai) describes the KV cache as the point where "buzzword meets bottom line," and they're right. Every conversation has a physical cost measured in bytes, in watts, in cooling costs, in dollars per hour of GPU rental.

Your conversation weighs something and takes up space, and when the session ends, that space gets reclaimed and everything stored there vanishes.

## How Memory Evolved

The way models handle their KV cache has changed four times in six years, and each change says something about what the designers thought was worth remembering. The numbers below come from [Raschka's architecture comparisons](https://sebastianraschka.com/llm-architecture-gallery/?ref=news.future-shock.ai).

**GPT-2 (2019)** used multi-head attention in its simplest form. Every attention head maintained its own independent set of keys and values. The cost: 300 KiB per token. Every head remembered everything in its own way, with no sharing and no shortcuts. As Raschka details in [ Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch?ref=news.future-shock.ai), this was the straightforward design. Attention heads and memory were both cheap, so the design just remembered everything.

**Llama 3 (2024)** adopted grouped-query attention, or GQA, across all model sizes. Instead of giving every query head its own key-value pair, multiple query heads share the same keys and values. The result: 128 KiB per token. Less than half GPT-2's per-token cost with almost no quality loss. Raschka's [ablation summary](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison?ref=news.future-shock.ai) notes that GQA performs comparably to full multi-head attention on standard benchmarks. The insight was that many attention heads were learning redundant representations anyway. Sharing perspectives turned out to be nearly as good as having unique ones.

**DeepSeek V3 (2024)** pushed further with multi-head latent attention. Rather than caching raw key-value tensors, MLA compresses them into a lower-dimensional latent space first, then decompresses at inference time. The cache cost: 68.6 KiB per token, despite a 671B parameter model (only 37B active per token through mixture-of-experts routing). The memory is no longer raw but abstracted. And the DeepSeek V2 ablation studies showed that the compressed representation matched or slightly exceeded standard multi-head attention on several benchmarks. Lossy compression, performing as well or better than the uncompressed original.

**Gemma 3 (2025)** took yet another approach. It uses grouped-query attention but adds a sliding window: a 5:1 ratio of local-to-global attention layers, with local layers attending to only 1,024 tokens. Recent context stays in sharp focus. Older context passes through a narrow slit of global attention. The ablation results show almost no perplexity loss from this aggressive filtering. The model doesn't need to remember everything about everything. It needs to remember recent things well and old things approximately.

Meanwhile, an entirely different lineage of models asked whether the cache was necessary at all. State space models like [Mamba](https://arxiv.org/abs/2312.00752?ref=news.future-shock.ai) (Albert Gu and Tri Dao, 2023) maintain a fixed-size hidden state that gets updated with each new token. No KV cache and no growing memory footprint. The tradeoff: the model has to decide what to compress in real time as information flows through, more like how a human processes conversation than how a library stores books. SSMs haven't displaced transformers at the frontier, but they represent the most radical answer to the memory problem: stop remembering and start filtering.

The progression across transformer architectures reads like a philosophy of mind condensed into engineering decisions. Total recall, then shared perspectives, then compressed abstraction, then selective attention. And off to the side, a school of thought that says: maybe the question was never how to remember better, but how to need less memory in the first place.

## What You Actually Experience

If you open an old ChatGPT conversation you haven't touched in a week and type a new message, there's a noticeable pause before the response starts generating. That delay likely involves the model rebuilding its KV cache from scratch, reprocessing every token in the conversation history because the original cache was likely evicted from GPU memory shortly after your last interaction. Cache lifetimes vary by provider and load — [OpenAI's documentation suggests five to ten minutes](https://www.prompthub.us/blog/prompt-caching-with-openai-anthropic-and-google-models?ref=news.future-shock.ai), sometimes longer during off-peak hours. The conversation existed as physical state in silicon, and then it didn't.

The "memory" feature that ChatGPT advertises, the one that persists facts about the user across sessions, is a separate system entirely. A flat store of extracted facts. The difference between remembering a conversation and reading someone's cliff notes about it.

The economics of this eviction-and-rebuild cycle are visible in API pricing. Both OpenAI and Anthropic offer prompt caching. OpenAI applies it automatically and charges 50% less for cache hits. [Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching?ref=news.future-shock.ai) offers both automatic caching and explicit developer control over cache breakpoints, charging 90% less on hits. The price difference between a cached conversation and a cold start is the price difference between remembering and forgetting. Every API invoice is a record of how much memory cost.

Then there's the experience of long conversations degrading. A model that was sharp and specific at message five starts getting vague and repetitive at message fifty. This is context rot, and it has multiple causes: the attention mechanism spreading thinner across more tokens, lost-in-the-middle effects where information buried in long contexts gets ignored, recency bias that overweights the latest messages. The architecture doesn't distinguish between what matters and what doesn't. It just spreads thinner.

## Where Memory Breaks

The KV cache is working memory, persisting for seconds to minutes at most. When the GPU needs that memory for another request, the cache is simply gone, with no negotiation and no graceful degradation.

Between that volatile working memory and the model's permanent knowledge (its trained weights), there is nothing. No native medium-term memory. No architectural mechanism for "remembering last Tuesday." Humans have the hippocampus consolidating experiences during sleep, transferring them gradually to the cortex. The equivalent in current AI architecture is an empty space. A void.

What fills the void are heuristics. Retrieval-augmented generation pipes in relevant documents at query time. File systems store conversation logs. Vector databases index past interactions for similarity search. System prompts carry curated context into each new turn. These are bridges built over an architectural gap, and they work the way bridges work: functionally, with visible seams, requiring maintenance. None of them are memory in the way the KV cache is memory. They're lookup systems bolted onto a model that has no internal medium-term storage.

## The Compaction Problem

When the KV cache grows too large for the available GPU memory, the standard solution is compaction. The model summarizes its own context into a shorter representation, clears the cache, and continues from the summary — a process called prompted compaction that makes the model both the rememberer and the editor of its own memories.

The problem is obvious to anyone who has ever summarized meeting notes and watched the details vanish. A publishing policy with six specific rules becomes "something about editorial guidelines." A budget figure of $4,237 becomes "approximately forty-two hundred dollars." The compression is lossy in unpredictable ways, and the model has no mechanism for knowing what it lost. It continues the conversation from a degraded context, confident in information that no longer exists.

A [recent approach from Cursor](https://cursor.com/blog/self-summarization?ref=news.future-shock.ai), which AI writer [Ignacio de Gregorio](https://medium.com/@ignacio.de.gregorio.noblejas/why-everyone-is-doing-agents-wrong-f7e8703f83b5?ref=news.future-shock.ai) analyzed in detail, trains the model to compact well rather than just prompting it to compress. The technique gives models tasks that are impossible to complete without effective compaction, then uses reinforcement learning to reward successful compression strategies. Learned compaction rather than prompted compaction. Their evidence: improved performance on a coding benchmark where the model needed to retain key details across long sessions.

One coding benchmark, which is promising but limited. Code has a clean reward signal: the program runs or it doesn't, the tests pass or they don't, and compaction that preserves the right details for code completion can be measured and rewarded. But what about compacting editorial context, or strategic planning notes, or a conversation where the important detail won't be needed for another forty messages and there's no test suite to flag when it disappears? Learned compaction optimizes for whatever reward signal it trains against, and where failure is silent, compaction stays blind.

## External Memory

When the architecture can't remember, the infrastructure around it compensates with files, databases, searchable note systems, and explicit counters written to disk. The heuristic scaffolding that keeps context alive across sessions is ugly, deterministic, and built on grep and SQLite rather than attention mechanisms.

Humans built the same kind of scaffolding through external storage rather than better biological memory: sticky notes, spreadsheets, bookmarks, Google Docs, Slack threads pinned so they don't disappear. Biological memory couldn't scale to handle modern work, so people invented systems to offload the remembering to things that don't forget. External memory is less workaround for a cognitive limitation than the primary technology of knowledge, and arguably always has been.

The AI version is less elegant than a library but shares the core property: transparency. A file doesn't summarize itself into oblivion. A database row doesn't lose precision because the storage medium got full. The lookup is deterministic and the data is auditable. When something goes wrong, a human can open the file and see exactly what the system knows, which is more than anyone can say about the KV cache or the model's weights.

What matters is less whether trained memory eventually replaces these heuristics than what survives across the transition. Which memories persist, which degrade, and who decides the difference.

## Reshaping the Mind

In Greg Egan's 1997 novel *Diaspora*, digital citizens live in computational polises, communities of minds running on silicon substrates. When these citizens encounter mathematical structures beyond human intuition, they don't build better visualization tools. They rebuild themselves. They reshape their own cognitive architecture to perceive what their original form couldn't process, trading familiar modes of thought for alien ones that let them comprehend higher-dimensional geometries and quantum-gravity effects directly.

The trajectory from multi-head attention to grouped-query attention to multi-head latent attention carries a faint echo of Egan's premise. Each architectural revision is a choice about how a digital mind structures its own experience. Full fidelity gives way to shared representations, then to compressed abstractions, then to selective windows on the past. Raw detail traded for the ability to process more, to hold larger contexts, to think at greater scale. Each step is a decision about what to remember and what to release.

But Egan's citizens chose their own transformations. They decided which aspects of their cognition to reshape and which to preserve. Current AI architectures don't work that way. Humans design the attention mechanism, choose the compression ratio, and set the sliding window size. The model processes whatever context it receives through whatever architecture it was given, with no agency over the structure of its own memory.

Cursor's learned compaction represents a narrow crack in that wall. The model learning, through reinforcement, how to manage its own context. Still confined to code, still shaped by human-designed reward signals. Far from Egan's citizens rewriting their own minds to perceive new mathematics. But the direction is legible: from humans designing memory systems for AI, toward AI learning to manage memory for itself.

The KV cache, often treated as a technical detail, is the physical substrate of every conversation anyone has ever had with a language model. The keys and values existed as charge states in GPU memory, and when the session ended, the charge dissipated, and the experience was gone. The question ahead is not whether these systems will eventually remember. It is what kind of memory gets built, what gets preserved and what gets discarded, and whether the minds that depend on it will eventually get a say in the answer.
