---
title: "Google DeepMind's AlphaProof Nexus solves decades-old math problems for a few hundred dollars"
source: TLDR AI · 2026-05-26
url: https://the-decoder.com/google-deepminds-alphaproof-nexus-solves-decades-old-math-problems-for-a-few-hundred-dollars/?utm_source=tldrai
date: 2026-05-27
published_at: 2026-05-26T12:00:00+00:00
tag: 论文研究
item_id: c3f093b69d0d5fd7
---
# Google Deepmind's AlphaProof Nexus solves decades-old math problems for a few hundred dollars

![Image description](https://the-decoder.com/wp-content/uploads/2026/05/google_deepmind_alpha_evolve_llm_math.png)

## Key Points

- Google Deepmind has developed AlphaProof Nexus, a framework that autonomously solved nine of 353 open mathematical Erdős problems along with other complex conjectures, at an inference cost of just a few hundred dollars per problem.
- The system relies on the Gemini 3.1 Pro language model to generate proof steps in Lean, a formal programming language used for mathematical verification, enabling rigorous and machine-checkable solutions.
- While the vast majority of Erdős problems remained beyond the AI's reach, Deepmind researchers see the system as a valuable tool for supporting mathematical research.

**AlphaProof Nexus combines LLM-driven proof generation with machine verification to crack open math research problems that have stumped mathematicians for decades.**

Google Deepmind's new framework [AlphaProof Nexus](https://www.github.com/google-deepmind/alphaproof-nexus-results) has autonomously solved nine out of 353 open Erdős problems it attempted, including two questions that had gone unanswered for 56 years.

The system also proved 44 out of 492 open conjectures from the Online Encyclopedia of Integer Sequences (OEIS), settled a 15-year-old question about Hilbert functions in algebraic geometry, and improved a known bound in convex optimization. Inference costs ran just a few hundred dollars per problem, according to the [research paper](https://arxiv.org/abs/2605.22763v1).

Unlike (potentially) pure natural-language approaches [such as OpenAI's recent solution](https://the-decoder.com/openai-shifts-the-boundary-of-automated-reasoning-with-a-milestone-in-ai-mathematics-that-experts-are-now-unpacking/), the underlying language model in AlphaProof Nexus—in this case Gemini 3.1 Pro—doesn't have to carry the entire logical chain on its own.

Instead, it generates proof steps in Lean's formal language, and the compiler checks each one. Error messages feed directly back into the next attempt. That way, the LLM gets grounded by symbolic feedback, a safety net that offsets the well-known weaknesses of language models when it comes to logical reasoning. Humans only step in at the very end to check the results.

## Four agents, one surprising result

The system consists of four agent variants with increasing complexity. The simplest, Agent (A), deploys independent sub-agents running on Gemini 3.1 Pro in loops: the language model generates proof steps, the Lean compiler checks them, and error messages feed back into the next try.

Agent (B) adds queries to AlphaProof, Google's reinforcement-learning-based system for olympiad math, which can fill in missing proof segments. Agent (C) introduces an evolutionary component. Inspired by [AlphaEvolve](https://the-decoder.com/alphaevolve-is-google-deepminds-new-ai-system-that-autonomously-creates-better-algorithms/), sub-agents share a common population of proof sketches. Rating agents built on Gemini 3.0 Flash score these sketches for plausibility and novelty, then rank them using an Elo system. The fully equipped Agent (D) combines all of these capabilities.

Agent (D) was used for the Erdős problems. But a post-hoc analysis turned up a surprise: the simplest Agent (A), which only uses an LLM and compiler feedback, could also prove all nine solved Erdős problems, albeit pricier on the hardest ones.

The researchers attribute the simple agent's success to two factors: rapid improvement in the underlying language models and the "power of compiler feedback in grounding LLM reasoning." The fully equipped agent still holds an edge on the toughest tasks for now, but that lead could shrink as LLMs get better. The researchers say this points to a broader trend, describing "an ongoing shift from specialized trained systems toward simple agentic loops as LLMs become more capable."

![Six charts plotting solve rate (Y-axis) against mean cost in USD (X-axis) for Erdős problems 12(i), 12(ii), 125, 138, 152, and 26. Four agent variants are color-coded: (A) basic in blue, (B) basic with AlphaProof in orange, (C) basic with evolution in green, and (D) full in red. Numbers at data points indicate the number of sub-agents. On easier problems, all variants converge at high solve rates; on harder problems like erdos_125, solve rates stay low overall but rise with more sub-agents and higher cost.](https://the-decoder.com/wp-content/uploads/2026/05/alphaproof_erdos-2.png)


![Six charts plotting solve rate (Y-axis) against mean cost in USD (X-axis) for Erdős problems 12(i), 12(ii), 125, 138, 152, and 26. Four agent variants are color-coded: (A) basic in blue, (B) basic with AlphaProof in orange, (C) basic with evolution in green, and (D) full in red. Numbers at data points indicate the number of sub-agents. On easier problems, all variants converge at high solve rates; on harder problems like erdos_125, solve rates stay low overall but rise with more sub-agents and higher cost.](https://the-decoder.com/wp-content/uploads/2026/05/alphaproof_erdos-2.png)

## Useful even without a complete proof

The system's successes cluster in areas like combinatorics, convex optimization, and number theory, where Lean's math library Mathlib is mature and problems break down into manageable sub-goals. Most Erdős problems remained out of reach, "let alone problems that require extensive new theory," the researchers write. The agents also inherit the unreliability of the underlying language models.

Still, they see value beyond solved problems. Mathematicians who worked with the system reported that even failed proof attempts deepened their understanding of a problem, or as the authors put it, "AI-driven formal proof search can serve not only to solve problems but to deepen human understanding."

Because the sketches were formal, experts could focus on the unsolved sub-goals instead of re-checking the entire argument from scratch. The agents also proved effective at catching flawed formalizations in the literature. "Formal verification can serve as a filter for determining which proofs merit human review," the authors write.

The system is already being used in ongoing research on quantum optics and graph theory, according to the paper. All Lean proofs and selected natural-language proofs are [available on GitHub](https://www.github.com/google-deepmind/alphaproof-nexus-results).

![Three-column diagram showing AlphaProof Nexus's proof process for Erdős problem #125: on the left, the Lean input file with EVOLVE-BLOCK markers and a sorry placeholder; in the center, the prompt with prior attempts, Elo ratings, and the current plan; on the right, the step-by-step proof with chain-of-thought reasoning, search-replace operations, AlphaProof calls, and final validation of all six sub-goals.](https://the-decoder.com/wp-content/uploads/2026/05/alphaproof_erdos-1.png)


![Three-column diagram showing AlphaProof Nexus's proof process for Erdős problem #125: on the left, the Lean input file with EVOLVE-BLOCK markers and a sorry placeholder; in the center, the prompt with prior attempts, Elo ratings, and the current plan; on the right, the step-by-step proof with chain-of-thought reasoning, search-replace operations, AlphaProof calls, and final validation of all six sub-goals.](https://the-decoder.com/wp-content/uploads/2026/05/alphaproof_erdos-1.png)

## Erdős problems become the benchmark for AI math

OpenAI recently [used a proprietary reasoning model to disprove Erdős's unit-distance conjecture](https://the-decoder.com/openai-shifts-the-boundary-of-automated-reasoning-with-a-milestone-in-ai-mathematics-that-experts-are-now-unpacking/). Fields Medalist Tim Gowers called it "a milestone in AI mathematics." Before that, [GPT-5.2 Pro helped solve Erdős problem #281](https://the-decoder.com/gpt-5-2-pro-solves-another-erdos-problem-while-a-new-database-reveals-most-attempts-still-fail/), with Terence Tao calling the case "perhaps the most unambiguous instance" of an LLM solving an open math problem. Thereafter, [GPT-5.4 solved another Erdős problem](https://the-decoder.com/openais-gpt-5-4-pro-reportedly-solves-a-longstanding-open-erdos-math-problem-in-under-two-hours/).

In some ways, those results are more impressive than Deepmind's approach. The language model had to carry the entire logical chain through natural language, without [a Lean compiler checking each step](https://x.com/polynoamial/status/2057216766221115562). AlphaProof Nexus is more systematic and scalable, but it's tackling a different goal: building a reliable AI tool for everyday math research. OpenAI could integrate Lean into their scaffold as well, of course, but the point there is more about testing raw LLM capability.

Tao in the past warned against reading too much into the headlines, though. AI's actual success rate on Erdős problems sits at just one to two percent, concentrated on easier tasks. Google's system cracked only nine out of 353 problems. That lines up almost exactly with Tao's two-percent bar.

### AI News Without the Hype – Curated by Humans


Subscribe to THE DECODER for ad-free reading, a weekly AI newsletter, our exclusive "AI Radar" frontier report six times a year, full archive access, and access to our comment section.

[Subscribe now](https://the-decoder.com/subscription/)

[Paper](https://arxiv.org/pdf/2605.22763v1)
