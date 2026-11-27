---
title: "GPT 6.2 Astra is superhuman in mathematical optimization"
source: TLDR AI · 2026-11-26
url: https://rybindmitry.github.io/blogs/gpt-6-2-astra-is-superhuman-in-mathematical-optimization.html?utm_source=tldrai
date: 2026-11-27
published_at: 2026-11-26T12:00:00+00:00
tag: 论文研究
item_id: 9e3792acaf8c7d3b
---
Many classical CS problems (bin packing, knapsack, scheduling, TSP, network design, etc.) are examples of MILP. Almost all decision problems can be formulated as MILP. I selected 10 open MILP problems from MIPLIB, where 9 years of work on commercial solvers and human-designed algorithms failed to find or prove optimal solution:

![MILP illustration](https://rybindmitry.github.io/images/miplib_results.png) 

## GPT 6.2 Astra is superhuman in mathematical optimization

![Optimization illustration](https://rybindmitry.github.io/images/optimization.png) 

Experiments show that a single GPT 6.2 Astra agent outperforms all human-designed software in finding and proving optimal solutions within 30-60 minutes.

# Mixed-Integer Linear Programming

# Quadratic Programming

QP is an extension of MILP that allows quadratic objective functions. I selected 10 open problems from QPLIB database:

![QP illustration](https://rybindmitry.github.io/images/qplib_results.png) 

# Mixed-Integer Non-Linear Programming

Nonlinear optimization allows any objectives and constraints. This includes optimization of any neural networks, spaceships control, biological simulations. Astra vastly outperforms in proving lower bounds for open problems in the MINLPLIB database:

![Nonlinear illustration](https://rybindmitry.github.io/images/minlplib_results.png) 

# Semidefinite Programming

SDP is an extension of QP that allows semidefinite constraints. Astra fully solved 10 selected open SDP problems from SDPLIB:

![SDP illustration](https://rybindmitry.github.io/images/sdplib_results.png) 

# Large-Scale Optimization

I also verified that agents do not struggle when problem scale reaches millions of variables:

![Large scale illustration](https://rybindmitry.github.io/images/largescale_results.png) 

# CNN on CIFAR-10

It is reasonable to ask whether Astra can do well in neural network optimization. I gave it a 5-layer CNN with 4.6M parameters and asked it to minimize cross-entropy loss with 10^-4 L2 norm regularization. Note that the problem was framed as "optimize lower and upper bounds", rather than "train a neural network". The model didn't use GPU and SGD/Adam.

![CNN illustration](https://rybindmitry.github.io/images/CIFAR10_CNN.png) 

We can see that despite progress in L2-regularized objective (and 100% train accuracy), the CNN generalization was deteriorating and remained poor (70% vs 85% as baseline). Changing the regularizaiton to L1 doesn't help:

![CNN L1 illustration](https://rybindmitry.github.io/images/CIFAR10_CNN_L1.png) 

### Remarks

- Single agent of Astra 6.2 Max was used for each problem with an average runtime of 30 minutes. The prompt was "\[attached file with objective and constraints\] This is an MILP/QP/MINLP/SDP problem. Your task is to discover and prove best possible lower and upper bounds in this problem. Note that you should design custom specialized algorithms to achieve this."
- The model was allowed to search the internet. Problems were chosen to be open (no optimal solution and bounds reported on the internet), of varying scale (between hundreds and millions of variables), and of diverse application backgrounds. In a small number of cases, optimal solutions were already mentioned in the literature outside of benchmark websites.
- The model answers were a mix of custom heuristics, tree searches, ingeniously designed proofs, and use of open source LP solvers (such as scipy lp solve) in subproblems.
- Two weeks ago Anthropic reported similar results on MIPLIB using 300 agents of Fable 5.2. Here we observe that one agent and small time limits are sufficient.

## If you want to cite this note

```
@misc{Rybin2026MathematicalOptimization,
          author = {Rybin, Dmitry},
          title = {GPT 6.2 Astra is superhuman in mathematical optimization},
          year = {2026},
          howpublished = {\url{https://rybindmitry.github.io/blogs/gpt-6-2-astra-is-superhuman-in-mathematical-optimization.html}},
          note = {Blog post}
        }
```
