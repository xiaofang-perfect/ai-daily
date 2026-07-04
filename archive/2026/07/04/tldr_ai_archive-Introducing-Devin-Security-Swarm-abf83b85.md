---
title: "Introducing Devin Security Swarm"
source: TLDR AI · 2026-07-03
url: https://threadreaderapp.com/thread/2072368168182432109.html?utm_source=tldrai
date: 2026-07-04
published_at: 2026-07-03T12:00:00+00:00
tag: 工具开源
item_id: abf83b852082814c
---
**
              
              This Thread may be Removed Anytime!**
          

Twitter may remove this content at anytime! Save it as PDF for later use!

- Follow [@ThreadReaderApp](https://twitter.com/threadreaderapp)to mention us!
- From a Twitter thread mention us with a keyword "unroll"

`@threadreaderapp unroll`
          [Practice here](https://twitter.com/threadreaderapp/status/1054877865362112513) first or read more on our [help page](https://threadreaderapp.com/help)!

Introducing FrontierCode: a coding eval that raises the bar for difficulty & quality. Each task took 40+ hrs of work by leading open-source maintainers.


Models write sloppy code that works but isn’t maintainable. Our eval is first to measure: would you actually merge this code?![Image](/images/1px.png)


          Models write sloppy code that works but isn’t maintainable. Our eval is first to measure: would you actually merge this code?

20+ world-class open-source developers built realistic coding tasks on repos they maintain. They define what “mergeable” means in their repo.


What does it take to measure mergeability? We use a mix of unit tests, rubrics and novel verifiers to assess correctness, test quality, scope discipline, style, and adherence to codebase standards.![Image](/images/1px.png)


          What does it take to measure mergeability? We use a mix of unit tests, rubrics and novel verifiers to assess correctness, test quality, scope discipline, style, and adherence to codebase standards.

FrontierCode was built in close partnership with the expert maintainers of 36 flagship open-source repositories, like @smilingnosrati, CEO & Tech Lead @CeleryOrg (29k stars), and Martin McKeaveney, CTO of @Budibase (28k stars).


Maintainers invested more than 40 hours per task, undergoing multiple rounds of iteration to ensure that any PR that satisfies these standards would actually be merged.![Image](/images/1px.png)


![Image](/images/1px.png)


      Maintainers invested more than 40 hours per task, undergoing multiple rounds of iteration to ensure that any PR that satisfies these standards would actually be merged.

Meet Devin Review: a reimagined interface for understanding complex PRs.


Code review tools today don’t actually make it easier to read code. Devin Review builds your comprehension and helps you stop slop.


Try without an account:


More below 👇[devinreview.com](http://devinreview.com)

          Code review tools today don’t actually make it easier to read code. Devin Review builds your comprehension and helps you stop slop.

Try without an account:

More below 👇

Full breakdown: 


First, instead of presenting diffs alphabetically and file-by-file, Devin Review groups related changes together and orders them logically. Each group comes with a clear description of what’s going on. Devin Review also intelligently detects copied and moved code, separating signal from noise.[cognition.ai/blog/devin-rev…](https://cognition.ai/blog/devin-review)![Image](/images/1px.png)


          First, instead of presenting diffs alphabetically and file-by-file, Devin Review groups related changes together and orders them logically. Each group comes with a clear description of what’s going on. Devin Review also intelligently detects copied and moved code, separating signal from noise.

Devin Review includes a bug catching agent that labels potential issues by confidence and severity. It will also flag decisions / patterns that could be bad, even if they aren’t bugs, helping you stop slop.


Red: pay attention. Orange: take a look. Gray: FYI![Image](/images/1px.png)


      Red: pay attention. Orange: take a look. Gray: FYI

Our research interns present:

Kevin-32B = K(ernel D)evin


It's the first open model trained using RL for writing CUDA kernels. We implemented multi-turn RL using GRPO (based on QwQ-32B) on the KernelBench dataset.


It outperforms top reasoning models (o3 & o4-mini)! 🧵![Image](/images/1px.png)


          Kevin-32B = K(ernel D)evin

It's the first open model trained using RL for writing CUDA kernels. We implemented multi-turn RL using GRPO (based on QwQ-32B) on the KernelBench dataset.

It outperforms top reasoning models (o3 & o4-mini)! 🧵

We train on a subset of 180 PyTorch -> CUDA conversion tasks from KernelBench. It's a nice RL environment because we have immediate code execution feedback.


During training, we give the model 4 refinement steps. In each step, the model proposes a kernel. Then we evaluate correctness & performance and inject the environment feedback in the next step.


For more details on how we made GRPO work in a multi-turn setting read our blogpost (linked below)!![Image](/images/1px.png)


          During training, we give the model 4 refinement steps. In each step, the model proposes a kernel. Then we evaluate correctness & performance and inject the environment feedback in the next step.

For more details on how we made GRPO work in a multi-turn setting read our blogpost (linked below)!

We ablate two different ways of training:

- Single-turn RL (training on just the first step)

- Multi-turn RL (training on four refinement steps)


When evaluated on performance (= speedup of CUDA kernels over PyTorch) we see a significant improvement from multi-turn training.


The model learns how to refine itself more effectively!


(All models are evaluated on 4 & 8 refinement steps, i.e. same amount of compute)![Image](/images/1px.png)


      - Single-turn RL (training on just the first step)

- Multi-turn RL (training on four refinement steps)

When evaluated on performance (= speedup of CUDA kernels over PyTorch) we see a significant improvement from multi-turn training.

The model learns how to refine itself more effectively!

(All models are evaluated on 4 & 8 refinement steps, i.e. same amount of compute)

Project DeepWiki


Up-to-date documentation you can talk to, for every repo in the world.


Think Deep Research for GitHub – powered by Devin.


It’s free for open-source, no sign-up!

Visit deepwiki com or just swap github → deepwiki on any repo URL:

          Up-to-date documentation you can talk to, for every repo in the world.

Think Deep Research for GitHub – powered by Devin.

It’s free for open-source, no sign-up!

Visit deepwiki com or just swap github → deepwiki on any repo URL:

Go to  to explore wikis for the most popular open source repos.


Turn on Deep Research for agent-powered in-depth answers (vid sped up).[deepwiki.com](http://deepwiki.com)

          Turn on Deep Research for agent-powered in-depth answers (vid sped up).

Don't see your repo? We're happy to index any public GitHub repo for you (watch how).


To get wikis for private repos, sign up for a Devin account at .[devin.ai](http://devin.ai)

      To get wikis for private repos, sign up for a Devin account at .

Yesterday was Devin’s first day at work! Check out how engineering teams are building with Devin so far. ![Image](/images/1px.png)


          1/  

          2/  

      Devin is generally available today! 


Just tag Devin to fix frontend bugs, create first-draft PRs for backlog tasks, make refactors, and more.


Start building with Devin below:

          Just tag Devin to fix frontend bugs, create first-draft PRs for backlog tasks, make refactors, and more.

Start building with Devin below:

1/5  Devin is built to collaborate with engineering teams and starts at $500/month. Here’s how some of the best teams are using Devin today: 

          2/5  We worked with Devin to contribute to popular open source repos. Here is one example of a Devin session that triages, solves, and tests a fix for an issue in Anthropic’s MCP: [app.devin.ai/sessions/26695…](https://app.devin.ai/sessions/266955553baf40cfa7fdd32d42ab219d)


The merged PR is here:[github.com/modelcontextpr…](https://github.com/modelcontextprotocol/inspector/pull/105)


We’re sharing this session, and several other open source contributions, in our blog below.

      The merged PR is here:

We’re sharing this session, and several other open source contributions, in our blog below.
