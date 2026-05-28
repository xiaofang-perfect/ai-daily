---
title: "Extract More Kernel Performance with NVIDIA CompileIQ Auto-Tuning"
source: TLDR AI · 2026-05-27
url: https://developer.nvidia.com/blog/extract-more-kernel-performance-with-nvidia-compileiq-auto-tuning/?utm_source=tldrai
date: 2026-05-28
published_at: 2026-05-27T12:00:00+00:00
tag: 工具开源
item_id: 3ee36f9ca3d83219
---
NVIDIA CompileIQ tackles one of the hardest problems in performance engineering: finding the compiler options that unlock the best performance for a specific workload.

Consider a team that has spent weeks optimizing an LLM inference pipeline on GPUs, tuning batch sizes, quantizing to FP8, adopting flash attention, fusing every kernel they can. The profiler says there’s nothing left to squeeze.

But what if you could turn the compiler itself into a tunable parameter? Now you can. The release of [NVIDIA CUDA 13.3](https://developer.nvidia.com/blog/nvidia-cuda-13-3-enhances-gpu-development-with-tile-programming-in-cpp-compiler-autotuning-and-python-updates) includes CompileIQ, an AI-powered compiler auto-tuning framework that uses evolutionary and genetic algorithms to optimize NVIDIA general purpose GPU compilers for individual workloads.

NVIDIA GPU compilers apply the same default heuristics (register allocation strategies, instruction scheduling decisions, loop unrolling thresholds, etc.) to every kernel they compile. These heuristics are engineered to produce good results across a vast range of workloads. But “good across the board” and “optimal for your workload” are two very different things.

The competitive landscape in AI infrastructure has made this gap impossible to ignore. Teams building custom CUDA, [Triton](https://github.com/triton-lang/triton/), and [Helion](https://github.com/pytorch/helion) kernels are striving for every percentage point of throughput. Until now, there hasn’t been a way to fine-tune code generation for a specific workload.

## The 90% problem and the opportunity

To understand why compiler-level optimization matters so much, consider where GPU compute actually goes in modern LLM inference.

In attention inference kernels, GEMMs in the linear layers of FFN/MLP blocks plus the Q, K, V, and output projections account for approximately 70% of total FLOPs. Scaled dot-product attention, fused and flash attention variants account for another 25%. Together, these two kernel families represent more than 90% of end-to-end inference compute.

This is not unique to AI inference. There are many applications and algorithms where a large portion of the compute time is spent in relatively small portions of the code, which means these small code sections contribute an outsized influence to the performance of the application. Because of this, performance improvements in those code portions, even fractions of a percent, have outsized improvements on overall application performance.

## Introducing CompileIQ

[CompileIQ](https://github.com/nvidia/compileiq) is an AI-powered compiler auto-tuning framework that uses evolutionary and genetic algorithms to optimize NVIDIA GPU compilers for individual workloads. Instead of accepting one generic compiler configuration for all workloads, CompileIQ flips the script, generating specialized compiler configurations tailored to each of your most critical kernels.

Under the hood, CompileIQ explores a rich space of internal compiler parameters that aren’t exposed through any public compiler flag: register allocation strategies, instruction scheduling policies, loop transformations, and more. The output is an advanced controls file (ACF) that the compiler ingests via the –apply-controls flag, producing a kernel binary optimized specifically for your workload.

Think of it this way: Your compiler already has the capability to generate better code for your kernel. It just doesn’t know which combination of internal settings will get there. CompileIQ’s evolutionary search finds that combination automatically.

The team that hit a wall after exhausting every optimization lever they knew now has a new lever with CompileIQ—the compiler itself.

CompileIQ is available and can be installed into your favorite Python environment using pip, as shown in the next section. Leading AI labs are already using it in production for their most performance-critical workloads.

## Getting started in 4 steps

CompileIQ is a Python package with a simple workflow:

- Learn
- Install
- Define your objective
- Run

```
pip install compileiq
```

CompileIQ ships with compiler search spaces for both PTXAS and NVCC that are automatically fetched via APIs. No manual downloads or configuration are required.

Your job as the developer is to define your objective function: for instance, a Python callable that takes a candidate compiler configuration, compiles your kernel with it, benchmarks the result, and returns a score. If you can benchmark your kernel, you can use CompileIQ.

Here’s an example:

```
import subprocess
from compileiq.ciq import Search
from compileiq.types import SearchConfiguration
# Define your objective: compile with the ACF and measure runtime
def objective(config_blob):
with open("config.acf", "wb") as f:
f.write(bytes.fromhex(config_blob))
result = subprocess.run([
"ptxas", "-v", "-arch=sm_90a",
"--apply-controls", "config.acf",
"my_kernel.ptx"
], capture_output=True, text=True)
return extract_runtime(result.stdout)
# Configure and run the evolutionary search
config = SearchConfiguration(
pool_size=32, cull_size=24, generations=20,
mutate_rate=0.1, problem_type="min",
num_objectives=1
)
search = Search(config, objective)
best_acf = search.run()
```

The code above can be separated into three distinct sections:

- Define your objective: We define the function objective, which takes the configuration to be evaluated in
`config_blob`

, saves it to disk, compiles and runs the kernel, and then extracts the metric. - Configure the search: Set the parameters that will drive the search, like how many candidates to try in one generation (
`pool_size`

), how many generations to run, and the number of objectives to be optimized. - Run the search and extract the best candidate.

That’s it. When the search starts, CompileIQ initializes a population of compiler configurations, evaluates each one against your objective function, selects the best performers, applies mutation and crossover to generate new candidates, and converges on an optimal ACF over successive generations.

You define what “better” means for your workload in the objective function, and CompileIQ finds it.

![The evolutionary optimization loop: define your objective, and CompileIQ handles the rest – from population initialization through convergence to a deployable ACF](https://developer-blogs.nvidia.com/wp-content/uploads/2026/05/image3-4.webp)

*Figure 1. CompileIQ workflow: Define objective, initialize, evaluate, select and mutate, converge, deploy*

## Examples

Now let’s focus on self-contained examples that you can try. There are a number of examples in the GitHub repo, and we’ll demonstrate two here. First, the single objective example, which has nothing to do with GPU computing, but demonstrates the principles of using CompileIQ.

```
from compileiq.ciq import Search
from compileiq.types import SearchConfiguration
import compileiq.search_spaces.base as ss
def objective(config):
score = config["x"] ** 2 + config["y"]
return score
def main():
dna_config = {
"x": ss.range(start=1.0, end=20.0, step=0.5),
"y": ss.choice([1, 2, 3]),
"z": ss.literal("this is a constant", knockout_prob=0.5),
}
main_config = SearchConfiguration(
generations=5,
problem_type="min",
num_objectives=1,
)
tuner = Search(
objective_function=objective,
search_space=dna_config,
search_config=main_config,
)
results = tuner.start()
print(f"Entire Results Dataframe:\n {results.get_results()}")
print(f"Best Result: {results.get_best_result()}")
if __name__ == "__main__":
main()
```

First, the objective function:

```
def objective(config):
score = config["x"] ** 2 + config["y"]
return score
```

This is a simple function that squares x, and adds that value to y. This is the function we’ll optimize:

```
dna_config = {
"x": ss.range(start=1.0, end=20.0, step=0.5),
"y": ss.choice([1, 2, 3]),
"z": ss.literal("this is a constant", knockout_prob=0.5),
```

The config specifies what values are permitted for the variables. For **x**, the range is between 1.0 and 20.0, with step size of 0.5. For **y**, the choices are either 1, 2 or 3; **z** doesn’t actually contribute to the calculation of the objective, but illustrates dropout.

```
main_config = SearchConfiguration(
generations=5,
problem_type="min",
num_objectives=1,
)
```

Next we specify the search configuration. In this case we’ll run 5 generations, we want to minimize the objective function, and there is only one objective being analyzed.

The rest of the code sets up the arguments and the search. This is a very simple objective function and you can calculate it by hand easily, but for illustrative purposes here’s what happens when you run the code.

$ python single_objective.py 🧬 Generation: 5/5|█| [elapsed: 00:00 · eta: 00:00] , 🏆 best_score=3.2500 Entire Results Dataframe: metadata ... params 0 {"pid": 2562276} ... {'x': 2.5, 'y': 2, 'z': 'this is a constant'} 1 {"pid": 2562276} ... {'x': 8.5, 'y': 3} 2 {"pid": 2562276} ... {'x': 11.0, 'y': 1, 'z': 'this is a constant'} 3 {"pid": 2562276} ... {'x': 19.0, 'y': 2} 4 {"pid": 2562276} ... {'x': 13.5, 'y': 3} .. ... ... ... 109 {"pid": 2562276} ... {'x': 1.5, 'y': 3, 'z': 'this is a constant'} 124 {"pid": 2562276} ... {'x': 1.0, 'y': 2, 'z': 'this is a constant'} 126 {"pid": 2562276} ... {'x': 2.0, 'y': 1, 'z': 'this is a constant'} 135 {"pid": 2562276} ... {'x': 3.0, 'y': 2, 'z': 'this is a constant'} 138 {"pid": 2562276} ... {'x': 1.5, 'y': 3} [61 rows x 4 columns] Best Result: {'metadata': '{"pid": 2562276}', 'generation': 4, 'score_1': 3.0, 'params': {'x': 1.0, 'y': 2, 'z': 'this is a constant'}}

Notice the listing of the best result has **x = 1.0** and **y = 2**, which results in a score of 3.0. But we know the best score is actually when **x = 1.0** and **y = 1**, so in this case CompileIQ didn’t find the best answer. Due to the very low number of generations (in our case 5) and the stochastic nature of the search, we didn’t happen to find the absolute best answer. However, in this case if you increase the generation to a larger number, say 15, you will almost always obtain the best answer.

Let’s move to an example that measures GPU performance of a specific kernel. In the GitHub repo there is an example using NVCC to build a reduction kernel. We won’t include the entire code here for brevity, but will show snippets to illustrate the concepts.

In the Python function which sets up the search, we have this code:

```
# Configure and run search
search_space = args.search_space if args.search_space else NvccSearchSpace(version=cuda_version)
config = SearchConfiguration(
problem_type=ProblemType.MIN,
generations=args.generations,
pool_size=args.pool_size,
)
```

The search space is configured to use the `NvccSearchSpace`

for CUDA 13.3. And you can see the problem type to optimize for is `MIN`

, which means we want to find the minimum of the objective function. Generations and pool size are command line arguments which default to 10 and 15 respectively in this Python script. The GPU kernel code is set up to run a reduction and then print out the time, and the objective function (not listed here) essentially builds and runs the kernel, and searches for the `Time =`

string and this is the value that is minimized over the search space.

Assuming you’re in the `compilers/nvcc_example`

folder, here’s what it looks like when you run the search.

$ python optimize_reduction.py --arch sm_120 Running baseline... Baseline: 0.777 ms Starting optimization (10 generations, pool=15)... 🧬 Generation: 10/10|█| [elapsed: 09:29 · eta: 00:00] , 🏆 best_score=0.7700, a Baseline: 0.777 ms Optimized: 0.770 ms Speedup: 1.01x Config saved: reduction_best_config.bin Usage: nvcc --apply-controls reduction_best_config.bin -arch=sm_120 ...

The performance increase found via the search is roughly 1%, and you can see that to apply this saved configuration you just need to use the `–-apply-controls`

option and add the ACF that you just generated.

## Multi-objective optimization and IP protection

Most auto-tuning tools optimize for a single metric, typically runtime. CompileIQ goes further, supporting multi-objective optimization, simultaneously exploring trade-offs across competing objectives like runtime, compile time, and power consumption.

This matters because “fastest possible” isn’t always the right answer. A power-constrained datacenter might accept a marginal runtime increase in exchange for significantly lower power draw. A CI/CD pipeline might prioritize compile time to keep iteration cycles fast. An embedded deployment might need to balance all three.

CompileIQ’s evolutionary engine computes a [ Pareto frontier](https://en.wikipedia.org/wiki/Pareto_front) of non-dominated solutions, or configurations where no single objective can be improved without worsening another. Your team picks the trade-off that fits your constraints, rather than being locked into a single optimization axis.

This capability extends CompileIQ’s applicability well beyond LLM inference. Anywhere NVIDIA compilers are used—scientific computing, autonomous vehicles, image processing, recommendation systems—CompileIQ can explore the optimization space and surface configurations that default heuristics miss.

On the IP protection front, CompileIQ is designed so that both sides stay secure. Compiler internals remain encapsulated within the search space and ACFs. Users need not concern themselves with compiler parameters. User workloads never leave their own environment; the objective function runs locally, and only the resulting ACF is produced. ACFs are safe to commit to version control and share across teams.

![Multi-objective optimization produces a Pareto frontier of non-dominated solutions. Teams can select configurations optimized for low runtime (orange), low power (gold), low compile time (cyan), or an optimal trade-off (teal)](https://developer-blogs.nvidia.com/wp-content/uploads/2026/05/image5-3.webp)

*Figure 2. 3D Pareto frontier: Runtime vs compile time vs power*

## Results and production adoption

CompileIQ has been validated across GPU and CPU targets on production workloads. For example, Meta has seen up to 15% performance improvement on both TritonBench and Helion kernels as shown in this [GTC talk](https://www.nvidia.com/en-us/on-demand/session/gtc26-s81859/).

These gains come on top of already-optimized baselines in kernels that were considered “done” by their authors. The improvements are the direct result of CompileIQ discovering compiler configurations that the default heuristics would never select.

Leading AI labs are already using CompileIQ in production for their most performance-critical inference and training workloads. The ACFs it produces are fully reproducible and portable: the same ACF generates the same optimized binary across deployments as long as the same benchmark and underlying compiler are matching. Teams commit ACFs to version control alongside their kernel source code, making compiler optimization a versioned, reviewable part of the development workflow.

## Your turn

Compiler search spaces are available for both **PTXAS** and **NVCC**. Identify your highest-impact kernels – GEMM and attention are the best candidates – write a benchmark that measures what matters to your workload, and run CompileIQ.

Documentation, API reference, and useful examples are available at the CompileIQ [documentation](https://nvidia.github.io/CompileIQ/) site. For questions and support, file an issue on the [CompileIQ GitHub ](https://github.com/NVIDIA/CompileIQ)repository.

One thing we should be clear on: CompileIQ is not a magic tool that automatically turns poorly-written code into high-performing code. To get the best value from CompileIQ, you need to start with reasonably high-performing code, which then enables the final compiler-heuristics tweaks to take you to maximum performance.

But, if your team has exhausted every optimization lever they know of, CompileIQ gives them a new lever—the compiler itself.

Download CompileIQ, check out the examples in GitHub, and start optimizing your kernels today*.*
