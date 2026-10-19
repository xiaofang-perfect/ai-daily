---
title: "Torvalds use Claude for bottleneck fix, but race discovered"
source: Hacker News
url: https://thenewstack.io/torvalds-claude-code-kernel/
date: 2026-10-19
published_at: 2026-10-18T16:08:48+00:00
tag: 行业动态
item_id: f2120b2aec8da60d
---
# Linus Torvalds let Claude Code fix the Linux page cache. Then reviewers found a race.

![Featued image for: Linus Torvalds let Claude Code fix the Linux page cache. Then reviewers found a race.](https://cdn.thenewstack.io/media/2026/10/39123855-dorothy-livelo-l1lklun853s-unsplash-1024x647.jpg) 

Linux creator and longtime lead maintainer [Linus Torvalds](https://www.linkedin.com/in/linustorvalds/) turned to Anthropic’s Claude Code to tackle a kernel performance problem that developers have struggled with for more than two years. On Tuesday, he [submitted a 10-patch series](https://lkml.iu.edu/2610.1/13146.html) that delivered a 23-fold throughput improvement in a synthetic benchmark running on his Ryzen Threadripper.

Torvalds had spent 18 months running a broken version of his own fix for the page-cache reference-counting bottleneck, while other developers had encountered problems with their approaches. The new patches eliminate folio reference-count operations from a common buffered-read path, although Torvalds warned that the benchmark gains would be considerably smaller in real-world workloads.

Reviewers have since identified a race condition and raised concerns about memory reclamation. Torvalds has handed further development to [Kiryl Shutsemau](https://www.linkedin.com/in/kiryl-shutsemau-78153330/), a Linux kernel developer who previously worked on the same bottleneck.

Torvalds had spent 18 months running a broken version of his own fix for the page-cache reference-counting bottleneck, while other developers had encountered problems with their approaches.


## Page cache contention problem

On Torvalds’ Core i7-8565U laptop, folio reference-count contention accounted for 99.92% of cross-core load HITMs in eight-thread tests, [according to Hardware Busters](https://hwbusters.com/news/linus-torvalds-uses-claude-code-to-rework-the-linux-page-cache-tripling-small-read-throughput/).

The bottleneck was flagged in 2024 by Matthew Wilcox, an Oracle engineer and longtime Linux kernel memory-management developer, after it surfaced in a customer workload.

## Claude Code writes the patches

On Sunday, Phoronix’s [Michael Larabel](https://www.linkedin.com/in/michaellarabel/) spotted an experimental branch named `noref-filemap-read-with-llm` in Torvalds’ tree, which rarely contains anything outside the main development branch.

The eight-patch series, based on Linux 7.3-rc6, came with a clear account of what Claude Code did. Torvalds said the assistant wrote the implementation, tests, and initial documentation, and reviewed the code under his direction. He ran the benchmarks himself, despite having previously [criticized developers for claiming AI writes 99% of their code](https://thenewstack.io/torvalds-ai-programming-productivity/).

Earlier approaches copied data without holding a folio reference and checked its validity afterward, leaving races involving reclamation and replacement. The subsequent 10-patch `rcu-free-v3` series instead uses a new `PG_rcu_free` flag and RCU-delayed reclamation to protect the folio through the userspace copy, provided it doesn’t fault.

Earlier approaches copied data without holding a folio reference and checked its validity afterward, leaving races involving reclamation and replacement.


## Threadripper benchmark results

The original eight-patch branch nearly tripled throughput on Torvalds’ laptop, pushing eight-thread performance from 10 million to as many as 33 million reads per second while cutting kernel cycles per read from roughly 2,950 to 725. The revised series delivered a much larger gain under heavy contention on his 64-thread Threadripper, where throughput jumped from 13.3 million to 304 million reads per second and cycles per read fell from nearly 20,000 to 735.

The original eight-patch branch nearly tripled throughput on Torvalds’ laptop, pushing eight-thread performance from 10 million to as many as 33 million reads per second while cutting kernel cycles per read from roughly 2,950 to 725.


The performance gains came with trade-offs. In the first implementation, delayed reclamation forced an expedited grace period whenever a CPU queued more than 1,024 pages, [according to Hardware Busters](https://hwbusters.com/news/linus-torvalds-uses-claude-code-to-rework-the-linux-page-cache-tripling-small-read-throughput/). Reads into unmapped user pages also triggered an additional fault before falling back to the existing path, pushing a 16-byte single-thread read from about 4,150 to 6,550 cycles. Whether that regression persists in `rcu-free-v3` remains unclear.

## Maintainers question the reclamation design

Wilcox questioned the new `PG_rcu_free` flag and proposed using a page type instead, along with reclaiming inactive-list folios after an RCU grace period.

Torvalds rejected both approaches, arguing that the flag must be set while a folio can still be mapped into userspace and that inactive-list reclamation wouldn’t cover truncate and hole-punch operations. Shutsemau subsequently suggested restricting the flag to 64-bit systems, an approach supported by Arm engineer and Linux memory-management maintainer [David Hildenbrand](https://www.linkedin.com/in/david-hildenbrand-73416154/).

Shutsemau also identified a race in `filemap_read_rcu_batch()`, where folio replacement followed by an extension of `i_size` could expose data that had never been written. Torvalds recommended moving the file-size read earlier and consolidating the folio checks, which Shutsemau incorporated into a revised patch.

			
				[YOUTUBE.COM/THENEWSTACK
			
			
				Tech moves fast, don't miss an episode. Subscribe to our YouTube 
				channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)
