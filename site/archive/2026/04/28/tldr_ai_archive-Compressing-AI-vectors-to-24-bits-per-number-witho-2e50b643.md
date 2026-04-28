---
title: "Compressing AI vectors to 2–4 bits per number without losing accuracy"
source: TLDR AI · 2026-04-28
url: https://arkaung.github.io/interactive-turboquant/?utm_source=tldrai
date: 2026-04-28
published_at: 2026-04-28T12:00:00+00:00
tag: 论文研究
item_id: 2e50b643003f36d3
---
# Compressing AI vectors to 2–4 bits per number

without losing
accuracy.

Modern language models store large tables of high-dimensional vectors: KV caches, embeddings, attention keys.
TurboQuant compresses each coordinate of these vectors to **2–4 bits** with provably near-optimal
distortion, no memory overhead for scale factors, and no training or calibration. This page explains how it
works.

[DRIVE: One-bit Distributed Mean Estimation
Vargaftik, Ben-Basat, Portnoy, Mendelson, Ben-Itzhak, Mitzenmacher · NeurIPS 2021 ·
arXiv:2105.08339
](https://arxiv.org/abs/2105.08339)

[EDEN: Communication-Efficient and Robust Distributed Mean Estimation for Federated Learning
Vargaftik, Ben-Basat, Portnoy, Mendelson, Ben-Itzhak, Mitzenmacher · ICML 2022 ·
arXiv:2108.08842
](https://arxiv.org/abs/2108.08842)

[RaBitQ: Quantizing High-Dimensional Vectors with a Theoretical Error Bound for Approximate
Nearest Neighbor Search
Gao, Long · SIGMOD 2024 · arXiv:2405.12497
](https://arxiv.org/abs/2405.12497)

[QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead
Zandieh, Daliri, Han · 2024 · arXiv:2406.03482
](https://arxiv.org/abs/2406.03482)

[Practical and Asymptotically Optimal Quantization of High-Dimensional Vectors in Euclidean
Space for Approximate Nearest Neighbor Search
Gao, Gou, Xu, Yang, Long, Wong · 2024 · arXiv:2409.09913
](https://arxiv.org/abs/2409.09913)

[PolarQuant: Quantizing KV Caches with Polar Transformation
Han, Kacham, Karbasi, Mirrokni, Zandieh · 2025 · arXiv:2502.02617
](https://arxiv.org/abs/2502.02617)

[TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate
Zandieh, Daliri, Hadian, Mirrokni · 2025 · arXiv:2504.19874
](https://arxiv.org/abs/2504.19874)

[A Note on TurboQuant and the Earlier DRIVE/EDEN Line of Work
Ben-Basat, Ben-Itzhak, Mendelson, Mitzenmacher, Portnoy, Vargaftik · 2026 ·
arXiv:2604.18555
](https://arxiv.org/abs/2604.18555)

[Revisiting RaBitQ and TurboQuant: A Symmetric Comparison of Methods, Theory, and
Experiments
Gao, Gou, Xu, Shi, Yang, Li, Wong, Long · 2026 · arXiv:2604.19528
](https://arxiv.org/abs/2604.19528)

The single load-bearing idea: in high dimensions, a random rotation turns every input vector into one whose coordinates follow a known fixed distribution. A codebook designed once for that distribution can then be reused for every input. Everything else on this page is the construction that puts this observation to work.

This construction was introduced by DRIVE (Vargaftik et al., NeurIPS 2021) for one-bit federated
mean estimation, and generalized to `b`

bits per coordinate by EDEN (Vargaftik et al.,
ICML 2022). TurboQuant (Zandieh et al., 2025) is the same construction with the per-vector
scale parameter fixed to a constant, repackaged for KV-cache compression and inner-product
retrieval. The mapping from each idea on this page to its source paper is in
[§0.9](https://arkaung.github.io#lineage).

## Eight ideas the rest of the page is built on.

Each mini-demo below covers one concept used later. Skip the ones you already know.

`[0.3, −1.2]`

. Geometrically it is an
**arrow from the origin**. A

*d-dimensional vector*is an arrow in $d$-space, hard to picture past 3-D, but the rules are the same.

**[0.70, 0.50]**length

**0.86**

**Length**= $\sqrt{x_1^2+x_2^2+\dots}$.

**Inner product**$\langle x,y\rangle = x_1 y_1 + x_2 y_2 + \dots = \|x\|\|y\|\cos\theta$. The inner product reaches its largest positive value when the two arrows point in the same direction. It drops to zero when the two arrows are perpendicular. It becomes negative when the arrows point in opposite directions, with its most negative value when they point exactly opposite.

**1.00**‖y‖

**1.00**⟨x,y⟩

**0.00**angle

**90°**

Error is the distance between a guess and the truth. Scoring a guess by the signed error
lets positive and negative errors cancel, which means the score does not penalise being
off. Squaring forces every error to count as a positive number and gives big errors a
larger penalty than small ones. The guess that minimises the mean of squared errors is the
data’s **average**: it is the unique number that minimises the sum of squared
distances to the points.

The **first moment** of a quantity $X$ is its mean $\mathbb{E}[X]$; the
**second moment** is the mean of its square $\mathbb{E}[X^2]$. A zero-mean variable
has a vanishing first moment because positive and negative deviations cancel. Its second
moment is strictly positive whenever any deviation is nonzero, because squared values
are nonnegative and cannot cancel. The MSE above is itself a second moment of the
residual error. This distinction returns in [§7](https://arkaung.github.io#bias), where the per-input
gap $\tilde y - y$ averages to zero in the first moment, while its square averages to a
strictly positive quantity in the second.

The average has a property we will use in [§7](https://arkaung.github.io#bias). It lies between the
data’s most extreme points, so its magnitude is smaller than at least one of them.
When a quantizer compresses a whole bin of values down to the bin’s average, the
stored value is smaller in magnitude than the bin’s largest values. The reconstruction
is a shrunken version of the input. An inner product against a shrunken reconstruction
comes out smaller than the same inner product against the input.

**0.00**MSE at guess

**1.00**MSE at mean

**1.00**

An **estimator** is a procedure that takes data and returns a guess $\hat\theta$ for an
unknown truth $\theta$. Repeat it on fresh data and the guesses form a cloud. The cloud can
fail in two independent ways. Variance is one: individual guesses are noisy. Bias is the
other: the procedure is wrong even after averaging many guesses. An estimator with
$\mathbb{E}[\hat\theta]=\theta$ is unbiased; the cloud’s centre sits at $\theta$
regardless of the cloud’s width.

The bullseye below shows both failure modes. Bias is the distance from the cloud’s
centre to the crosshair. Variance is the width of the cloud. The two quantities are
independent of each other. [§7](https://arkaung.github.io#bias) runs the same bullseye against the MSE
quantizer of [§6](https://arkaung.github.io#pipeline), and the cloud’s centre lands away from the
crosshair. [§8](https://arkaung.github.io#qjl) runs it against a different estimator whose cloud
centres on the crosshair.

**0**mean of shots

**–**bias

**–**

**rotation matrix**$R$ spins space. The key property: $\|Rx\|=\|x\|$ and $\langle Rx,Ry\rangle=\langle x,y\rangle$. Rotation only changes the

*basis*the coordinates are written in, not the geometry.

**1.41 → 1.41**preserved?

**yes**

**Central Limit Theorem**says that summing enough independent random numbers produces a distribution close to a bell curve. The shape of each individual term in the sum does not affect the limit. A sum of coin flips converges to the same Gaussian shape as a sum of uniform draws or a sum of skewed draws. A rotated coordinate is one of these sums: it is a weighted combination of every coordinate of the original vector, with random weights. After a random rotation, each new coordinate is therefore approximately Gaussian, which is the property TurboQuant relies on for every input.

**±1 coin**converged?

**no, n too small**

**measure concentration**, and it is the core fact TurboQuant exploits.

**≈ 0.71**1/√d

**0.71**

**4**gap Δ

**0.667**max error

**0.333**

**Vector**: ordered list of numbers / arrow from the origin.
**Length & inner product**: the norm $\sqrt{\sum x_i^2}$ and how much two vectors point the same way.
**MSE**: average squared error. **Unbiased**: the average of many estimates equals the truth.
**Rotation**: change of basis that preserves lengths and angles.
**CLT**: sum of many independent randoms converges to a Gaussian.
**High-D concentration**: coordinates of a random unit vector in $d$-space cluster near $\pm 1/\sqrt d$.
**Quantization**: snap each number to one of $2^b$ levels; one extra bit quarters the squared error.

## Where each idea on this page comes from.

DRIVE (Vargaftik et al., NeurIPS 2021) introduced the construction for one bit per coordinate. A sender rotates the input vector by a random orthogonal matrix, sends the sign of every rotated coordinate together with a single scalar scale $S$, and the receiver inverts the rotation after multiplying the sign vector by $S$. DRIVE derives two scale formulas. The MSE-optimal biased scale is $S = \|R(x)\|_1 / d$. The unbiased scale is $S = \|x\|_2^2 / \|R(x)\|_1$, which gives $\mathbb{E}[\hat x] = x$. DRIVE also shows that a Randomized Hadamard Transform can replace the uniform random rotation at $O(d \log d)$ cost (DRIVE, §6).

EDEN (Vargaftik et al., ICML 2022) generalizes DRIVE to any $b$ bits per coordinate. After the rotation, EDEN normalizes the rotated vector by $\eta_x = \sqrt{d}/\|x\|_2$ so each coordinate is approximately $\mathcal{N}(0,1)$, then quantizes against a Lloyd-Max codebook designed once for the standard normal. The 1-bit codebook is $\{\pm\sqrt{2/\pi}\}\approx\{\pm 0.798\}$ and the 2-bit codebook is $\{\pm 0.453, \pm 1.510\}$. These are the exact codebooks the page derives in §5. EDEN keeps a per-vector scale $S = \|x\|_2^2 / \langle R(x),\, Q(\eta_x R(x))\rangle$ that yields an unbiased estimate (EDEN, Theorem 2.1).

RaBitQ (Gao and Long, SIGMOD 2024) is a parallel line of work in approximate nearest-neighbor search. The encoder rotates the input vector with a randomized rotation, stores the sign of every rotated coordinate plus a per-vector normalization scalar, and the decoder estimates inner products from the signs and the scalar. The extended paper (Gao et al., 2024, arXiv:2409.09913) proves that this estimator achieves the asymptotic optimality bound of Alon and Klartag (FOCS 2017) for inner-product quantization. RaBitQ predates TurboQuant and shares the random-rotation backbone with the DRIVE/EDEN line. The two lines reach comparable theoretical results from different framings (federated mean estimation versus ANN search), and the relationship between them is the subject of an ongoing public discussion (arXiv:2604.18555 and arXiv:2604.19528, both 2026).

## Idea-to-source map

| Idea on this page | First introduced in |
|---|---|
| Random rotation, post-rotation distribution analysis (§3, §4) | DRIVE (2021), §3 |
| Randomized Hadamard transform as the practical rotation (§3) | DRIVE (2021), §6; EDEN (2022), §5 |
| Lloyd-Max codebook on $\mathcal{N}(0,1)$, including the $\{\pm\sqrt{2/\pi}\}$ 1-bit and $\{\pm 0.453,\,\pm 1.510\}$ 2-bit codebooks (§5) | EDEN (2022), §3 |
| Unbiased rotation-then-quantize via a per-vector scale (§7, §8 backbone) | DRIVE (2021), §4.2, Theorem 3 |
| The $b$-bit pipeline (§6) | EDEN (2022) with the per-vector scale fixed to a constant |
| QJL residual unbiasing (§8) | One-bit unbiased DRIVE applied to the residual instead of the input |
| Random rotation + 1-bit sign quantization for unbiased inner-product estimation in ANN search | RaBitQ (Gao & Long, SIGMOD 2024) |
| Asymptotic optimality matching the Alon–Klartag (FOCS 2017) inner-product bound | RaBitQ extended (Gao et al., 2024, arXiv:2409.09913) |
| Residual chain: biased $(b{-}1)$-bit + unbiased 1-bit (§7 then §8) | TurboQuant (2025) |
| KV-cache and inner-product application framing | TurboQuant (2025); QJL (2024) for the 1-bit case |

## What is vector quantization, really?

You have a vector $\mathbf{x}\in\mathbb{R}^d$, say $d{=}1536$ floats from an OpenAI embedding. You want to store it using $b$ bits per coordinate (total $b\cdot d$ bits), then later recover an approximation $\tilde{\mathbf{x}}$ close to $\mathbf{x}$. Closeness is measured by

**MSE distortion**$D_{\text{mse}} = \mathbb{E}\big[\,\|\mathbf{x} - \tilde{\mathbf{x}}\|_2^2\,\big]$ or

**inner-product error**$D_{\text{prod}} = \mathbb{E}\big[\,|\langle\mathbf{y},\mathbf{x}\rangle - \langle\mathbf{y},\tilde{\mathbf{x}}\rangle|^2\,\big]$

The second one matters because attention scores and nearest-neighbor queries are all *inner products*.
We would like the estimator to be *unbiased*: $\mathbb{E}[\langle\mathbf{y},\tilde{\mathbf{x}}\rangle] =
\langle\mathbf{y},\mathbf{x}\rangle$.

**MSE distortion**: average squared error between the true vector
and its reconstruction, [primer §0.3](https://arkaung.github.io#pr-mse).

**Inner product** $\langle y, x\rangle$: how much two vectors point
the same way, [primer §0.2](https://arkaung.github.io#pr-dot). This is what attention computes.

**Estimator**: a rule (here: quantize, then decode) that returns an
approximation $\hat s$ of a true number $s$.

**Unbiased estimator**: across many queries, the average of $\hat s$
equals $s$. Individual estimates can be noisy; the mean is on target. [Primer §0.4](https://arkaung.github.io#pr-bias).

### The obvious quantizer

For each coordinate, pick the closest of $2^b$ evenly-spaced levels in $[-1, 1]$. That is $b$ bits per number. The same rule runs in 2D and 3D first, where the geometry is visible, before the high-dimensional version below.

#### First, in 2D

Drag the tip of the vector. The vector snaps to the nearest point of a $2^b \times 2^b$ grid. The green arrow shows the original input. The blue arrow shows where the input is quantized to. The red segment between them is the reconstruction error $\mathbf{x} - \tilde{\mathbf{x}}$.

#### Same trick in 3D

A $2^b$-level grid on three axes gives $2^{3b}$ snap points. Drag the canvas to orbit the view. The spike preset shows where the construction breaks: the input lies near one axis and falls between two grid levels, which is where the reconstruction error is largest.

#### Now at scale (d up to 128)

The same rule applied to every coordinate of a high-dimensional vector. You cannot see the grid anymore, but the per-coordinate errors are still there.

Select the **spike** input. The naive quantizer's grid is spaced evenly over $[-1, 1]$.
The input has almost all of its magnitude in a single coordinate, whose value falls between
the two grid levels nearest to it and so reconstructs poorly. The remaining coordinates are
near zero and consume most of the levels despite carrying little of the input's information.

[§2](https://arkaung.github.io#naive)where the gap shows up

A fixed grid produces small reconstruction errors on inputs whose coordinates are roughly
uniform in magnitude, and large reconstruction errors on inputs whose magnitude is
concentrated in one or a few coordinates. Next: [§2](https://arkaung.github.io#naive) shows how production
systems handle the second case and what they pay for the fix.

## The adversarial coordinate, and why production systems pay a tax

Real embeddings are rarely flat. Trained models produce *outlier channels*,
a few coordinates much larger than the rest. A fixed $[-L, L]$ grid either clips the outliers
or wastes resolution on the bulk. Production quantizers (GPTQ, AWQ, KIVI, KVQuant) work around this by
computing $(\min, \max)$ (or zero-point and scale) for every small block and storing those in full
precision as side information.

**The catch.**To decode any block you also need its scale and zero-point, two float16 numbers (32 extra bits) stored next to every 16–64 quantized values. Walk through one case: a block of 32 numbers at 3 bits each is 96 payload bits, plus 32 metadata bits, which works out to

**4 bits per number, not 3**. Smaller blocks of 16 numbers push it to

**5 bits per number**. The advertised 3-bit scheme is really a 4–5-bit scheme once you count everything. TurboQuant matches this worst-case quality while storing zero per-block metadata.

`b`

bits/value, three strategies
A 64-dimensional vector whose coordinates are mostly small, with one large outlier shown in
red. Three quantizers reconstruct the same vector at the same `b`

-bit budget.
Strategy A uses a single fixed grid for the whole vector. Strategy B adapts the grid per
block, at the cost of a float16 header per block. Strategy C
rotates the vector first and then applies a single fixed grid. The metrics report the RMSE of
each reconstruction and the effective bits-per-value once the metadata cost is included.

**A. Fixed grid [−L, L]**

`b`

bits/value, no header. Outlier clips.**B. Per-block scale + zero**

`float16`

scale+zero per block
(dashed dividers). Outlier fits, header taxes you.**C. Rotate → fixed grid**

**Read the storage line.** The effective bits-per-value works out to `b + 32/s`

for the per-block scheme and to `b`

for the other two, because only the per-block
scheme stores a float16 scale and zero-point (32 bits together) for every block of
`s`

elements. At `b=3, s=16`

the per-block cost works out to
`3 + 2 = 5`

bits/value, a 66% surcharge over the nominal `b`

. Strategy
C achieves the same storage cost as strategy A while producing the reconstruction quality of
strategy B. The rest of this page explains the construction that makes that possible.

[§3](https://arkaung.github.io#rotation)one fixed recipe, any input

Production quantizers handle outliers by paying a per-block metadata tax. TurboQuant must
instead be *data-oblivious*: a single procedure that runs on every vector with no
calibration set and no per-block headers. Next: [§3](https://arkaung.github.io#rotation) introduces the
move that makes a fixed grid work for every input.

## Multiply by a random rotation. Watch the spike dissolve.

**The rotation trick:** apply a random orthogonal transform $\boldsymbol{\Pi}$, then quantize
coordinate-wise. Rotation is lossless, it preserves length and inner products exactly:

Because rotation is exact, all reconstruction error comes from the quantization step alone.
After a uniformly random rotation, every coordinate of $\boldsymbol{\Pi}\mathbf{x}$ follows
the same fixed Beta density (Lemma 1 of the paper), regardless of what $\mathbf{x}$ looked
like. **A single codebook designed once for that density is then optimal for every input.**
We build the codebook in [§5](https://arkaung.github.io#codebook).

[§0.9](https://arkaung.github.io#lineage)for the full mapping.

## How to construct $\boldsymbol{\Pi}$

Generate a $d\times d$ matrix of i.i.d. $\mathcal{N}(0,1)$ entries and run QR decomposition; keep the orthogonal factor $Q$. The result is uniform on the orthogonal group $O(d)$, which is what Lemma 1 needs.

#### A spike in 2D

Start with the extreme case: a vector with all of its magnitude in one coordinate, $(1, 0)$. Rotate by angle $\theta$ and observe how the magnitude is redistributed across the two coordinates. At $\theta{=}45°$ the magnitude is split evenly between the two coordinates, giving $(\tfrac{1}{\sqrt 2}, \tfrac{1}{\sqrt 2})$. The total length of the vector stays the same throughout.

**geometry**

**coordinate magnitudes**

#### A spike in 3D

The same construction in three dimensions. The spike $(1, 0, 0)$ is rotated by a random orthogonal matrix, which spreads the input's magnitude across all three coordinates of the output. The total length of the vector is preserved. Each fresh draw of the random rotation produces a different spread.

**geometry (drag to orbit)**

**coordinate magnitudes**

#### At high dimension

A single rotation in 2-D reduces the largest coordinate to at most half the input's magnitude. A random rotation in 3-D typically leaves one coordinate around $0.7$. At $d{=}64$ the largest coordinate after rotation is around $1/\sqrt d \approx 0.125$, regardless of how concentrated the input was.

**before**, $|x_i|$ (Cartesian)

**after**, $|(\boldsymbol{\Pi}\mathbf{x})_i|$

[§3.5](https://arkaung.github.io#targets)no spike survives a random rotation

Rotation preserves length and inner products. The only thing it changes is which coordinates
contain the magnitude of the vector. A vector with all of its mass concentrated in one
coordinate becomes, after rotation, a vector whose mass is spread across all $d$
coordinates. Every input that gets quantized is of this spread-out kind. Next:
[§3.5](https://arkaung.github.io#targets) shows that the same rotated coordinates feed three different
decoders across the prior-work map of [§0.9](https://arkaung.github.io#lineage).

## The rotation step is shared. The decoder is what changes.

The random rotation of [§3](https://arkaung.github.io#rotation) is the encoder front end shared by every
method on the prior-work map of [§0.9](https://arkaung.github.io#lineage) (DRIVE 2021, EDEN 2022, RaBitQ
2024, QJL 2024, TurboQuant 2025). The methods differ on the decoder side: each one reads
the rotated coordinates and recovers a different quantity from them.

The demo below runs one rotated vector through three decoders in parallel. The mean decoder from DRIVE returns an unbiased estimate of $\mathbf{x}$ itself. The inner-product decoder from RaBitQ and QJL returns an estimate of $\langle\mathbf{q},\mathbf{x}\rangle$ against a query. The MSE decoder from EDEN and TurboQuant returns a low-distortion reconstruction $\tilde{\mathbf{x}}$. Each panel reports its error against the true value and the bits it stored per coordinate to get there.

**Mean decoder · DRIVE (2021)**

**Inner-product decoder · RaBitQ (2024) / QJL (2024)**

**MSE decoder · EDEN (2022) / TurboQuant (2025)**

[§5](https://arkaung.github.io#codebook), then apply $\boldsymbol{\Pi}^{\!\top}$ to recover $\tilde{\mathbf{x}}$.

[§0.9](https://arkaung.github.io#lineage)for the full mapping.

[§4](https://arkaung.github.io#concentration)same primitive, different decoders

Random rotation plus a low-bit read of the rotated coordinates is the front end shared
across DRIVE, RaBitQ, QJL, EDEN, and TurboQuant. The methods differ on the decoder side
and on what each one is asked to recover: the input vector, an inner product against a
query, or an MSE-optimal reconstruction. The rest of this page follows the MSE branch
(EDEN and TurboQuant). Next: [§4](https://arkaung.github.io#concentration) explains the result that
lets a single fixed codebook serve every input.

## Coordinates of random unit vectors are nearly Gaussian.

Rotating $\mathbf{x}$ by a uniformly random $\boldsymbol{\Pi}$ is the same as picking a random point on the sphere of radius $\|\mathbf{x}\|$. So the question “what does a coordinate of $\boldsymbol{\Pi}\mathbf{x}$ look like?” is the same question as “what does a coordinate of a uniform point on the sphere look like?”

In low dimensions the answer is far from a bell curve. In 2-D the marginal is the arcsine density, which is U-shaped with peaks at $\pm 1$. In 3-D it is uniform on $[-1, 1]$. As $d$ grows the marginal narrows and converges to a Gaussian with variance $1/d$. The convergence is visible in the demos that follow.

## The exact density (Lemma 1)

For a uniform point on $\mathbb{S}^{d-1}$, the marginal density of any single coordinate is

a scaled/shifted Beta distribution. It converges pointwise to $\mathcal{N}(0,\,1/d)$ as $d\to\infty$.

#### Step one: the circle ($d=2$)

Sample 2000 points uniformly from the unit circle and look at a single coordinate, say $x_1$.
The marginal is the arcsine density $\tfrac{1}{\pi\sqrt{1-x^2}}$, which is U-shaped with peaks
at $\pm 1$. The shape is far from Gaussian: any value of $x_1$ between $-1$ and $+1$ is
possible, and the endpoints are *more* likely than the middle.

**points on the unit circle**

**marginal of $x_1$**

#### Step two: the sphere ($d=3$)

Now sample uniformly from the unit sphere in 3-D. The marginal of one coordinate is uniform on $[-1, 1]$ (Archimedes' hat-box theorem). The marginal is still not a bell curve. Drag to orbit the view.

**points on the unit sphere**

**marginal of $x_1$**

#### Step three: high dimensions

Drag $d$ upward. The marginal narrows and converges to a Gaussian with standard deviation $1/\sqrt d$. By $d{=}30$ the marginal is visually Gaussian. By $d{=}256$ almost all of the mass concentrates within a thin shell of width $\sim 1/\sqrt d$ around zero.

Distinct coordinates are also approximately independent, a stronger condition than uncorrelated, and what is actually needed for the per-coordinate quantization argument below.

[§5](https://arkaung.github.io#codebook)one distribution, one codebook

Every coordinate of a rotated vector follows the same known density. The scalar quantization
problem for that density can be solved once, and the solution can be reused for every
coordinate of every vector. There are no per-block scale factors and no side information to
store. Next: [§5](https://arkaung.github.io#codebook) builds the codebook with Lloyd–Max.

## Lloyd–Max: the optimal partition of a known distribution.

Every rotated coordinate looks like a draw from the same density ([§4](https://arkaung.github.io#concentration)).
So there is one scalar problem to solve, once: pick $2^b$ **landing values** on the number line
such that snapping any sample to its nearest landing value introduces as little error as possible.
Those landing values are the *codebook*.

A classical algorithm finds them: **Lloyd–Max**
([Lloyd 1957/82](https://doi.org/10.1109/TIT.1982.1056489),
[Max 1960](https://doi.org/10.1109/TIT.1960.1057548)).
Because the density is fixed and known in advance, Lloyd–Max runs once at table-build
time. The resulting landing values are saved into a tiny per-$b$ table. Encoding a coordinate
after that is a single nearest-neighbour lookup against the table. The same table is used for
every input, with no calibration step and no per-vector tuning.

Drag $b$ below to watch Lloyd–Max settle on the landing values for the Beta density.

## The Lloyd–Max iteration

Given a PDF $f_X$, choose centroids $c_1 \le \dots \le c_{2^b}$ minimising $\int (x - c_{i(x)})^2 f_X(x)\,dx$ by alternating:

**Assignment:**each centroid owns the Voronoi cell around it, boundaries are midpoints between adjacent centroids.**Update:**each centroid moves to the conditional mean of its cell, $c_k \leftarrow \mathbb{E}[X \mid X \in \text{cell}_k]$.

Repeat until stable. The demo runs this on the Beta density of [§4](https://arkaung.github.io#concentration).

For moderate $d$, the paper's explicit centroids (after normalising by $\sqrt{d}$) are: $b{=}1\!:\pm\sqrt{2/\pi}$, $b{=}2\!:\{\pm 0.453,\pm 1.510\}$, and so on. Theorem 1 proves the per-coordinate MSE is $\lesssim \tfrac{\sqrt{3}\pi}{2d}\cdot 4^{-b}$. The constant $\tfrac{\sqrt{3}\pi}{2}\approx 2.72$ is the asymptotic ratio to Shannon's minimum $\tfrac{1}{d}\cdot 4^{-b}$; at $b{=}1$ the paper reports a tighter ratio of $\approx 1.45$.

[§0.9](https://arkaung.github.io#lineage)for the full mapping.

[§6](https://arkaung.github.io#pipeline)a tiny lookup, baked once

Lloyd–Max gives the optimal partition for a known density, so the centroids for the
Beta marginal can be precomputed and stored as a tiny per-$b$ table. The per-coordinate MSE
that the resulting codebook achieves is within a factor of $\approx 2.72$ of Shannon's lower
bound asymptotically and within $\approx 1.45$ at $b{=}1$. Next: [§6](https://arkaung.github.io#pipeline)
assembles rotation and codebook into TurboQuant-MSE.

## Putting it together: TurboQuant-MSE.

**No scales, no zero-points.**

**x**(original)

**Πx**(rotated, nearly Gaussian)

**quantized Πx**(snap to codebook)

**x̃ = Πᵀ·quant(Πx)**(recovered)

**error**x − x̃

Toggle between input types. Naive quantization without rotation fails on the spike input and on the outlier-channel input. With the rotation step in front, the reconstruction error is roughly the same regardless of which input is selected. Every rotated coordinate follows the same $\mathcal{N}(0,\,1/d)$ distribution, which is the distribution the codebook was designed for.

[§7](https://arkaung.github.io#bias)MSE is solved, but…

TurboQuant-MSE stores $b\cdot d$ bits per vector and zero metadata. The reconstructed
$\tilde{\mathbf{x}}$ is nearly as close to the original $\mathbf{x}$ as any quantizer can
achieve, within a factor of $\approx 2.72$ of Shannon's information-theoretic lower bound.
Next: [§7](https://arkaung.github.io#bias) shows that the same codebook produces a systematically biased
estimate of inner products. This is an error that minimising reconstruction MSE does not
address.

## MSE-optimal quantizers underestimate inner products.

[§6](https://arkaung.github.io#pipeline)’s TurboQuant-MSE keeps $\tilde{\mathbf{x}}$ close to $\mathbf{x}$
in squared distance. Attention does not measure $\|\mathbf{x}-\tilde{\mathbf{x}}\|^2$. It computes
$\langle \mathbf{q}, \tilde{\mathbf{k}}\rangle$ and uses that number as a stand-in for
$\langle \mathbf{q}, \mathbf{k}\rangle$. The MSE codebook gives a systematically wrong answer to
the inner-product question. Each trial returns the same error, so averaging many trials does not
remove it.

Two earlier facts produce the shrinkage. In [§0.3](https://arkaung.github.io#pr-mse) the MSE-optimal
reconstruction for a set of values was the set’s average, and that average had smaller
magnitude than the set’s extreme values. In [§4](https://arkaung.github.io#concentration) a random
rotation made every coordinate of $\boldsymbol{\Pi}\mathbf{x}$ behave like a zero-mean draw
with most of its mass close to 0. Combine the two and the shrinkage is forced: the encoder
partitions each axis into $2^b$ bins and stores only which bin $\boldsymbol{\Pi}\mathbf{x}$
fell into, the decoder reconstructs with the bin’s average, and the bin’s average
sits closer to 0 than the tail inputs that fall into the same bin. The reconstruction
$\tilde{\mathbf{x}}$ is therefore a shrunken copy of $\mathbf{x}$, and an inner product
$\langle \mathbf{q}, \tilde{\mathbf{k}}\rangle$ comes out smaller than $\langle \mathbf{q},
\mathbf{k}\rangle$. Because the codebook is fixed, the shrinkage factor is identical on every
trial.

`y`

, watch ỹ snapOne rotated coordinate $y$ has the near-Gaussian density drawn on top. Lloyd–Max partitions the axis into $2^b$ bins (interior verticals); each bin’s centroid is the MSE-optimal reconstruction (red dots). Drag the mint handle to set $y$. The encoder snaps it to the centroid of the bin it fell into, giving $\tilde y$ (red). The staircase underneath plots that map $\tilde y(y)$ across the whole axis at once: every horizontal step sits inside the dashed identity line, and the gap between step and identity is the shrinkage at that input.

**Variance budget.**σ² = 1 splits into the part ỹ keeps and the part erased inside each bin.

=

*b***0.637**■ erased in-bin variance:

*D*

=

*b***0.363**

instantaneous, averages to D

b

= E[ỹ²]/σ²

*b*population, what counts

**What to notice.** Shrinkage is a second-moment statement. The signed gap
$\tilde y - y$ is positive for some inputs and negative for others; averaging it gives
zero, so any first-moment argument cancels out. The squared gap $(\tilde y - y)^2$ in
the third metric is always nonnegative, so summing it cannot cancel. Weighted by the
Gaussian density and integrated, it equals $D_b = \sigma^2 - \mathbb{E}[\tilde y^{\,2}]$,
the red segment of the budget bar; the staircase shading visualizes that gap pointwise,
with opacity tracking the Gaussian density so the visual area concentrates where the
distortion actually accumulates. As $b$ grows the shading thins and the red segment
shrinks with it. The fourth metric, $\lambda_b = \mathbb{E}[\tilde y^{\,2}]/\sigma^2$,
is the factor that multiplies every inner product
$\langle\mathbf q,\tilde{\mathbf k}\rangle$ in expectation; that is the shrinkage the
next paragraph quotes as $0.64 / 0.88 / 0.97 / 0.99$ for $b=1,2,3,4$.

The bullseye below measures the shrinkage. At $b{=}1$ the offset is $1 - 2/\pi \approx 0.36$ on every axis. The shrinkage factor approaches 1 quickly with more bits (about 0.88 at $b{=}2$, 0.97 at $b{=}3$, 0.998 at $b{=}5$), so by $b{=}3$ the residual bias is smaller than the trial-to-trial noise of a few thousand shots and the red dot visually overlaps the crosshair. The bias is theoretically strictly nonzero at every finite $b$, but the regime where it matters in practice is the low-bit one (1–2 bits per coordinate), where it dominates the per-trial variance.

Same bullseye as the [primer](https://arkaung.github.io#pr-bias). Each trial fires *two* shots at the
target, one inner-product estimate against $\mathbf{y}_1$ and one against an independent
$\mathbf{y}_2$, both divided by their truth and re-centred so a perfect estimate lands on the
centre. The **yellow crosshair** marks truth, the
**red dot** is the average of every shot fired so far. Unbiased means
the red dot sits on the crosshair, no matter how wide the cloud of shots around it.

**What to notice.** At $b{=}1$ the red dot is southwest of the crosshair, on the diagonal.
The offset on $\mathbf{y}_1$ and the offset on $\mathbf{y}_2$ are equal, which is what one
scalar shrinkage applied to the whole reconstruction would produce. Increase $b$: the offset
shrinks fast and is below the trial-to-trial noise by $b{=}3$, even though the underlying
shrinkage factor is still strictly less than 1.

## Derivation: where the $2/\pi$ factor comes from

For a standard Gaussian $g$, $\mathbb{E}[|g|]=\sqrt{2/\pi}$, the “half-normal” mean. The 1-bit MSE codebook rounds each rotated coordinate to $\pm\sqrt{2/\pi}/\sqrt d$; when you dot-product that reconstruction back against $\mathbf{y}$, you pick up another $\sqrt{2/\pi}$ factor in expectation. Multiply: $2/\pi \approx 0.637$.

Concretely at $b{=}1$, the optimal MSE codebook is $\{-\sqrt{2/\pi}/\sqrt{d},\,+\sqrt{2/\pi}/\sqrt{d}\}$, so $Q(\mathbf{x}) = \sqrt{2/(\pi d)}\cdot \operatorname{sign}(\boldsymbol{\Pi}\mathbf{x})$ and

The factor shrinks as $b$ grows but never vanishes, which is what the demo above shows.

[§8](https://arkaung.github.io#qjl)we need a different kind of estimator

An MSE-optimal codebook minimises squared reconstruction error. The cost is a fixed scalar
shrinkage on every inner product, and this shrinkage stays nonzero at any finite bit budget.
Attention and nearest-neighbour search need an inner-product estimator whose mean is correct.
**Next:** [§8](https://arkaung.github.io#qjl) keeps the same encoder and adds a fixed prefactor on the
decoder side equal to the reciprocal of the shrinkage. The mean of many trials then equals
$\langle \mathbf{q}, \mathbf{k}\rangle$.

## If the bias is a known number, multiply it out.

[§7](https://arkaung.github.io#bias) ended with a shrunken reconstruction. The MSE codebook produces
$\tilde{\mathbf{x}}$ values whose magnitudes are smaller than the inputs they encode, so every
inner product $\langle \mathbf{y}, \tilde{\mathbf{x}}\rangle$ comes out smaller than $\langle
\mathbf{y}, \mathbf{x}\rangle$ by the same scalar factor. At one bit per coordinate that factor
is exactly $2/\pi$. Averaging over trials does not move the estimate toward $\langle \mathbf{y},
\mathbf{x}\rangle$, because the same scalar multiplies the result on every trial.

A deterministic scalar bias is removable without changing the encoder. Multiply the decoder's output by the reciprocal of the bias and the expectation of the product equals the unbiased target. QJL applies this idea at one bit per coordinate. The encoder discards magnitude information, which is the same step that shrank §7's reconstruction. The decoder applies a fixed prefactor whose value is the reciprocal of the half-normal shrinkage that sign quantization introduces.

**Encoder.** Sample one random Gaussian matrix $\mathbf{S}$ once and share it between every
encoder and decoder. To store $\mathbf{x}$, write down the signs of $\mathbf{S}\mathbf{x}$. The
stored object is one bit per coordinate; the magnitudes of the entries of $\mathbf{S}\mathbf{x}$
are discarded. Discarding the magnitudes produces the bit savings and also produces a
$\sqrt{2/\pi}$ shrinkage on any reconstruction built from the signs alone, by the same
half-normal identity that produced §7's $2/\pi$.

**Decoder.** A full-precision query $\mathbf{y}$ arrives. Compute
$\langle \mathbf{S}\mathbf{y},\,\text{stored signs}\rangle$. This quantity is a noisy estimate
of $\langle \mathbf{x},\mathbf{y}\rangle$ scaled down by $\sqrt{2/\pi}$. Multiply by
$\sqrt{\pi/2}/d$. The factor $\sqrt{\pi/2}$ is the reciprocal of the half-normal shrinkage and
cancels it in expectation; the factor $1/d$ averages the estimate over the $d$ rows of
$\mathbf{S}$. The expected value of the result is $\langle \mathbf{x}, \mathbf{y}\rangle$. The
per-trial variance is larger than the MSE estimator's variance, but the mean of many trials
converges to $\langle \mathbf{x}, \mathbf{y}\rangle$.

Both panels use **exactly 1 bit per coordinate**. Left: the MSE-optimal codebook from
[§7](https://arkaung.github.io#bias), biased. Right: QJL with its calibration constant baked in. Each trial
fires two shots (against independent $\mathbf{y}_1$ and $\mathbf{y}_2$). Same number of trials,
same target. Watch where the red dot lands.

**What to notice.** The MSE panel's red dot is southwest of the centre at the same
offset as [§7](https://arkaung.github.io#bias)'s 1-bit measurement, and that offset stays the same
regardless of how many trials run. The QJL panel's red dot lands close to the centre but
with a residual offset from finite-sample noise. QJL's per-trial variance is larger than
MSE's (Lemma 4: $\propto \pi/(2d)$), so at the default trial count the residual offset is
small but visible. The key difference between the two estimators is the source of this
offset: MSE's offset is a fixed scalar bias on the inner product and does not shrink with
more trials; QJL's residual offset is sampling noise around a correct mean and shrinks at
the standard-error rate $1/\sqrt{n}$ as the trial count grows.

## The math: definition and where $\sqrt{\pi/2}/d$ comes from

With $\mathbf{S}\in\mathbb{R}^{d\times d}$ i.i.d. $\mathcal{N}(0,1)$:

Each row $\mathbf{s}_i$ makes $\mathbf{s}_i\mathbf{x}$ and $\mathbf{s}_i\mathbf{y}$ jointly Gaussian with covariance $\langle\mathbf{x},\mathbf{y}\rangle$. The half-normal identity gives $\mathbb{E}[(\mathbf{s}_i\mathbf{y})\,\text{sign}(\mathbf{s}_i\mathbf{x})] = \sqrt{2/\pi}\cdot\langle\mathbf{x},\mathbf{y}\rangle/\|\mathbf{x}\|$. Sum over $d$ rows and multiply by $\sqrt{\pi/2}/d$: the $\sqrt{2/\pi}$ shrinkage cancels, and the result is $\langle\mathbf{x},\mathbf{y}\rangle$ in expectation. Variance is bounded by $\tfrac{\pi}{2d}\|\mathbf{x}\|^2\|\mathbf{y}\|^2$ (Lemma 4 of the paper).

### Stretching it: TurboQuant-prod

QJL by itself uses one bit per coordinate. TurboQuant-prod extends the construction to a
$b$-bit budget by allocating the bits between the two estimators from §6 and §8. The first
$b{-}1$ bits encode $\boldsymbol{\Pi}\mathbf{x}$ with the MSE codebook of
[§6](https://arkaung.github.io#pipeline) to capture magnitude. The last bit encodes the residual
$\mathbf{r} = \boldsymbol{\Pi}\mathbf{x} - \tilde{\mathbf{y}}_{\text{mse}}$ with QJL to make
the inner-product estimate unbiased. The total cost is $b\cdot d$ bits plus one scalar per
vector (the residual norm $\|\mathbf{r}\|$), the same as TurboQuant-MSE.

## The full TurboQuant-prod recipe

- Rotate $\mathbf{x}\to \boldsymbol{\Pi}\mathbf{x}$ as in
[§3](https://arkaung.github.io#rotation). - Apply $(b{-}1)$-bit MSE-optimal quantization. Call the result $\tilde{\mathbf{y}}_{\text{mse}}$.
- Form the residual $\mathbf{r} = \boldsymbol{\Pi}\mathbf{x} - \tilde{\mathbf{y}}_{\text{mse}}$ and quantize it with one bit of QJL: store $\text{sign}(\mathbf{S}\mathbf{r})$ and the residual norm $\|\mathbf{r}\|$.
- Decode: $\tilde{\mathbf{x}} = \boldsymbol{\Pi}^{\top}\big(\tilde{\mathbf{y}}_{\text{mse}} + \|\mathbf{r}\|\cdot \tfrac{\sqrt{\pi/2}}{d}\,\mathbf{S}^{\top}\text{sign}(\mathbf{S}\mathbf{r})\big)$.

The residual norm is the only piece of side info in the whole scheme, one scalar per vector, not one per small block the way GPTQ, AWQ, or KIVI need. Variance is bounded by Theorem 2.

[§9](https://arkaung.github.io#bounds)two recipes, one budget

TurboQuant-MSE minimises reconstruction error and produces a biased inner-product estimate
with a known shrinkage factor. TurboQuant-prod allocates one of its $b$ bits to a QJL residual
and produces an unbiased inner-product estimate at higher per-trial variance. Both schemes use
$b\cdot d$ bits plus one scalar per vector. Next: [§9](https://arkaung.github.io#bounds) compares both upper
bounds against the information-theoretic lower bound.

## How close is TurboQuant to the theoretical best?

The paper uses Shannon's lossy source-coding theorem (via Yao's minimax principle) to prove that no quantizer can do better than $D_{\text{mse}} \ge 4^{-b}$ on worst-case inputs on the unit sphere. The bound covers every conceivable quantizer, including randomized and data-adaptive ones. TurboQuant's matching upper bound is $\tfrac{\sqrt{3}\pi}{2}\cdot 4^{-b}$, within a factor of $\approx 2.7$ of the lower bound asymptotically and within a factor of $\approx 1.45$ at $b{=}1$.

The plot uses a log scale on the vertical axis. All three curves have the same slope (the $4^{-b}$ exponential rate) and differ only by a small constant offset.

### The exponential improvement over older methods

Earlier data-oblivious quantizers (uniform rounding, scalar sketches) achieve a reconstruction
error that decays only polynomially in the bit budget, e.g. $\mathcal{O}(1/b)$. TurboQuant's
$4^{-b}$ rate is exponential in $b$. That exponential rate is what enables the
$4$–$6\times$ KV-cache compressions reported in [§10](https://arkaung.github.io#impact) without
measurable downstream quality loss.

[§10](https://arkaung.github.io#impact)tight against the floor

The upper bound, the lower bound, and the measured error all decay at the same exponential
rate $4^{-b}$ as $b$ grows, and they differ from each other only by a small constant.
TurboQuant therefore matches Shannon's $4^{-b}$ rate to within a factor of $\approx 2.72$
asymptotically and $\approx 1.45$ at $b{=}1$. Next: [§10](https://arkaung.github.io#impact) looks at the
systems consequences of this rate.

## Concrete wins in LLM inference.

### KV cache compression

Needle-in-a-Haystack recall on Llama-3.1-8B-Instruct, every compressed method evaluated at a $4\times$ memory-compression target (paper Fig. 4):

| Method | NiaH |
|---|---|
| Full cache (FP16) | 0.997 |
| SnapKV | 0.858 |
| PyramidKV | 0.895 |
| KIVI | 0.981 |
| PolarQuant | 0.995 |
TurboQuant |
0.997 |

TurboQuant matches the full-precision NiaH score at $4\times$ compression. On LongBench-V1 (paper Table 1), TurboQuant at $3.5$ bits per channel matches the full-precision average ($50.06$); at $2.5$ bits per channel it stays within $\approx 1\%$ of full precision ($49.44$ vs $50.06$), a $6.4\times$ compression.

After a random rotation, every coordinate of every input has the same fixed distribution: a low-variance Beta that converges to a Gaussian as $d$ grows. A single optimal codebook designed once for that distribution serves every input. The full vector-quantization problem reduces to the well-studied scalar quantization problem.
