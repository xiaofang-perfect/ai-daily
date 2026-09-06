---
title: "GPT-6 Astra on robot arms"
source: Hacker News
url: https://openai.robocurve.org/gpt-6-astra/
date: 2026-09-06
published_at: 2026-09-06T01:52:45+00:00
tag: 产品发布
item_id: 9da64b2511faf72e
---
# GPT‑6 Astra on robotic manipulation

September 4, 2026

A follow‑up to [our comparison of Claude Fable 5 and Fable 5.1](https://anthropic.robocurve.org/fable-5.1/).
  We gave OpenAI's GPT‑6 Astra control of the same YAM arms under the same
  [Inspect Robots](https://github.com/robocurve/inspect-robots) agent policy, on the same two tasks:

“Pick up the red block from the table and place it inside the bowl.”

“Pick up the round blue puzzle piece by the knob at its center and place it into the matching circular groove in the board.”

On the bowl task Astra placed the block in **19 of 20** trials, against Fable 5.1's **8 of 20** and Fable 5 in 1 of 20, in 2.5 minutes per trial to Fable 5.1's 6.8, at an estimated $0.94 per run to $2.12.

The puzzle task is a different story: Astra completed the insertion 2 times in 20 against Fable 5.1's 2 in 20. It reaches the groove and stalls at the same final step Fable does, at $1.36 per run to $2.18.

Block into bowl: the best completed run of each model (highest stage, then shortest), each played in its own time at the same speed‑up. Timers show real elapsed time with thinking pauses removed.

## Astra completes the bowl task far more often, at about half the cost per run

Large dots are condition means; faint dots are individual trials (100 if completed, 0 otherwise) at their own cost.

## Scoring

Every trial was scored by a human grader on the highest stage it reached, so a run that fails still records how far it got. The rubric is unchanged from the Fable report.

| 0 | No purposeful approach | 
| 1 | Made contact with the object | 
| 2 | Lifted the object clear of the table | 
| 3 | Positioned it above the deposit point | 
| 4 | Placed it in its final position | 

## Astra places the block almost every time; on the puzzle it stalls where Fable does

Share of trials per model reaching each stage; n per row is the number of trials in that cell.

## Results

| Task | Model | Mean stage | Completions | Rate | Output tokens/run | Est. cost/run | Minutes/run | 
|---|---|---|---|---|---|---|---|
| Block into bowl | Fable 5 | 1.30 | 1 / 20 | 5% | 19.2k | $2.69 | 8.2 | 
| Block into bowl | Fable 5.1 | 2.40 | 8 / 20 | 40% | 12.9k | $2.12 | 6.8 | 
| Block into bowl | GPT-6 Astra | 3.95 | 19 / 20 | 95% | 2.1k | $0.94 | 2.5 | 
| Puzzle into groove | Fable 5 | 1.50 | 0 / 20 | 0% | 16.3k | $2.63 | 7.9 | 
| Puzzle into groove | Fable 5.1 | 2.35 | 2 / 20 | 10% | 10.5k | $2.18 | 5.9 | 
| Puzzle into groove | GPT-6 Astra | 2.00 | 2 / 20 | 10% | 2.7k | $1.36 | 3.4 | 

## All runs

Every counted trial, 120 in total.

| Task | Model | Score | Time (min) | Output tokens | Transcript | Video | Rerun | 
|---|---|---|---|---|---|---|---|
| Block into bowl | GPT-6 Astra | 4 | 1.7 | 1,533 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_6b47f3c6.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_6b47f3c6.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_6b47f3c6.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 1.7 | 1,734 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_ce096d00.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_ce096d00.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_ce096d00.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 1.7 | 1,573 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_331420ca.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_331420ca.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_331420ca.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 1.8 | 1,669 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_bbabb896.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_bbabb896.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_bbabb896.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 1.9 | 1,570 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_4265dd2b.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_4265dd2b.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_4265dd2b.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.1 | 1,491 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_af4ad27d.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_af4ad27d.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_af4ad27d.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.1 | 2,153 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_74dc0873.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_74dc0873.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_74dc0873.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.1 | 1,782 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_67e2f399.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_67e2f399.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_67e2f399.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.2 | 2,034 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_1d7495e7.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_1d7495e7.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_1d7495e7.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.5 | 2,441 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_74369b9a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_74369b9a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_74369b9a.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.5 | 2,625 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_b7ce2b74.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_b7ce2b74.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_b7ce2b74.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.5 | 1,697 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_dcc477ea.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_dcc477ea.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_dcc477ea.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.8 | 2,434 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_67a7102e.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_67a7102e.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_67a7102e.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 2.9 | 2,966 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_6382f6da.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_6382f6da.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_6382f6da.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 3.2 | 1,627 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_efac9fe1.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_efac9fe1.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_efac9fe1.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 3.3 | 2,768 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_040f1344.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_040f1344.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_040f1344.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 3.3 | 2,777 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_721d78a5.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_721d78a5.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_721d78a5.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 3.4 | 2,185 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_5f53a87d.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_5f53a87d.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_5f53a87d.rrd) | 
| Block into bowl | GPT-6 Astra | 4 | 3.5 | 1,979 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_4f94b36e.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_4f94b36e.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_4f94b36e.rrd) | 
| Block into bowl | GPT-6 Astra | 3 | 3.5 | 2,428 | [view](https://openai.robocurve.org/runs/transcripts/rig-1_8ca08ed9.html) | [watch](https://openai.robocurve.org/runs/videos/rig-1_8ca08ed9.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-1_8ca08ed9.rrd) | 
| Block into bowl | Fable 5 | 4 | 5.2 | 13,120 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_e1117d44.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_e1117d44.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_e1117d44.rrd) | 
| Block into bowl | Fable 5 | 3 | 7.1 | 14,048 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_247be7bf.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_247be7bf.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_247be7bf.rrd) | 
| Block into bowl | Fable 5 | 2 | 5.0 | 10,663 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_f0cf92a3.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_f0cf92a3.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_f0cf92a3.rrd) | 
| Block into bowl | Fable 5 | 2 | 8.7 | 17,859 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_3a9b0ddb.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_3a9b0ddb.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_3a9b0ddb.rrd) | 
| Block into bowl | Fable 5 | 2 | 9.1 | 15,064 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_ab7e654f.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_ab7e654f.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_ab7e654f.rrd) | 
| Block into bowl | Fable 5 | 1 | 4.7 | 9,096 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_f3810f56.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_f3810f56.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_f3810f56.rrd) | 
| Block into bowl | Fable 5 | 1 | 5.8 | 13,800 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_b2321570.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_b2321570.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_b2321570.rrd) | 
| Block into bowl | Fable 5 | 1 | 5.8 | 9,954 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_1eaf9989.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_1eaf9989.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_1eaf9989.rrd) | 
| Block into bowl | Fable 5 | 1 | 7.1 | 16,666 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_6046d265.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_6046d265.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_6046d265.rrd) | 
| Block into bowl | Fable 5 | 1 | 7.2 | 18,165 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_2a2bde2e.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_2a2bde2e.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_2a2bde2e.rrd) | 
| Block into bowl | Fable 5 | 1 | 7.2 | 14,719 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_e1754989.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_e1754989.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_e1754989.rrd) | 
| Block into bowl | Fable 5 | 1 | 8.4 | 24,975 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_bf238349.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_bf238349.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_bf238349.rrd) | 
| Block into bowl | Fable 5 | 1 | 8.7 | 17,436 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_8c3e0134.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_8c3e0134.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_8c3e0134.rrd) | 
| Block into bowl | Fable 5 | 1 | 8.8 | 21,388 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_45801dbe.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_45801dbe.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_45801dbe.rrd) | 
| Block into bowl | Fable 5 | 1 | 9.6 | 30,566 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_c16654a2.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_c16654a2.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_c16654a2.rrd) | 
| Block into bowl | Fable 5 | 1 | 10.8 | 28,784 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_6e8e0044.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_6e8e0044.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_6e8e0044.rrd) | 
| Block into bowl | Fable 5 | 1 | 11.7 | 27,810 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_29103b97.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_29103b97.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_29103b97.rrd) | 
| Block into bowl | Fable 5 | 1 | 14.8 | 35,211 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_c5d62cba.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_c5d62cba.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_c5d62cba.rrd) | 
| Block into bowl | Fable 5 | 0 | 8.7 | 17,764 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_79082e74.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_79082e74.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_79082e74.rrd) | 
| Block into bowl | Fable 5 | 0 | 9.7 | 27,582 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_c2c68390.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_c2c68390.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_c2c68390.rrd) | 
| Block into bowl | Fable 5.1 | 4 | 4.2 | 9,124 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_f3f30ea2.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_f3f30ea2.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_f3f30ea2.rrd) | 
| Block into bowl | Fable 5.1 | 4 | 4.8 | 9,779 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_447ac0a9.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_447ac0a9.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_447ac0a9.rrd) | 
| Block into bowl | Fable 5.1 | 4 | 5.0 | 11,359 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_198ac66c.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_198ac66c.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_198ac66c.rrd) | 
| Block into bowl | Fable 5.1 | 4 | 5.1 | 8,526 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_5f24ff1a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_5f24ff1a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_5f24ff1a.rrd) | 
| Block into bowl | Fable 5.1 | 4 | 5.6 | 10,998 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_43385463.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_43385463.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_43385463.rrd) | 
| Block into bowl | Fable 5.1 | 4 | 6.5 | 7,031 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_9c985869.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_9c985869.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_9c985869.rrd) | 
| Block into bowl | Fable 5.1 | 4 | 6.7 | 15,901 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_baf7102e.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_baf7102e.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_baf7102e.rrd) | 
| Block into bowl | Fable 5.1 | 4 | 7.5 | 8,964 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_81500aaa.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_81500aaa.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_81500aaa.rrd) | 
| Block into bowl | Fable 5.1 | 3 | 5.7 | 14,477 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_c3fc27fa.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_c3fc27fa.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_c3fc27fa.rrd) | 
| Block into bowl | Fable 5.1 | 3 | 8.6 | 20,110 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_9ba9fc30.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_9ba9fc30.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_9ba9fc30.rrd) | 
| Block into bowl | Fable 5.1 | 2 | 7.3 | 20,022 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_678b9e3b.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_678b9e3b.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_678b9e3b.rrd) | 
| Block into bowl | Fable 5.1 | 2 | 18.9 | 14,526 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_5bc8330b.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_5bc8330b.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_5bc8330b.rrd) | 
| Block into bowl | Fable 5.1 | 1 | 5.7 | 13,265 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_4e5067fa.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_4e5067fa.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_4e5067fa.rrd) | 
| Block into bowl | Fable 5.1 | 1 | 5.9 | 18,073 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_fe9d6f8f.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_fe9d6f8f.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_fe9d6f8f.rrd) | 
| Block into bowl | Fable 5.1 | 1 | 6.0 | 13,070 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_41c88041.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_41c88041.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_41c88041.rrd) | 
| Block into bowl | Fable 5.1 | 1 | 6.6 | 11,506 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_0c4282a8.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_0c4282a8.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_0c4282a8.rrd) | 
| Block into bowl | Fable 5.1 | 1 | 7.1 | 11,404 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_e0d75213.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_e0d75213.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_e0d75213.rrd) | 
| Block into bowl | Fable 5.1 | 1 | 8.5 | 17,760 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_09b168e7.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_09b168e7.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_09b168e7.rrd) | 
| Block into bowl | Fable 5.1 | 0 | 4.5 | 8,979 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_4f4d481c.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_4f4d481c.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_4f4d481c.rrd) | 
| Block into bowl | Fable 5.1 | 0 | 5.2 | 13,394 | [view](https://openai.robocurve.org/runs/transcripts/rig-3_4e39dc4a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-3_4e39dc4a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-3_4e39dc4a.rrd) | 
| Puzzle into groove | GPT-6 Astra | 4 | 2.8 | 2,229 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_edd32a0a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_edd32a0a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_edd32a0a.rrd) | 
| Puzzle into groove | GPT-6 Astra | 4 | 3.3 | 1,967 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_e013c39a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_e013c39a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_e013c39a.rrd) | 
| Puzzle into groove | GPT-6 Astra | 3 | 2.3 | 2,581 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_76c6c1aa.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_76c6c1aa.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_76c6c1aa.rrd) | 
| Puzzle into groove | GPT-6 Astra | 3 | 2.6 | 2,805 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_d26e22e6.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_d26e22e6.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_d26e22e6.rrd) | 
| Puzzle into groove | GPT-6 Astra | 3 | 2.6 | 2,470 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_27172965.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_27172965.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_27172965.rrd) | 
| Puzzle into groove | GPT-6 Astra | 3 | 2.9 | 2,978 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_c3ae5367.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_c3ae5367.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_c3ae5367.rrd) | 
| Puzzle into groove | GPT-6 Astra | 3 | 3.0 | 2,937 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_3198e78e.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_3198e78e.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_3198e78e.rrd) | 
| Puzzle into groove | GPT-6 Astra | 3 | 3.1 | 2,932 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_eb40eafd.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_eb40eafd.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_eb40eafd.rrd) | 
| Puzzle into groove | GPT-6 Astra | 3 | 3.6 | 2,538 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_f127e66b.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_f127e66b.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_f127e66b.rrd) | 
| Puzzle into groove | GPT-6 Astra | 3 | 3.6 | 3,417 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_c57bff1a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_c57bff1a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_c57bff1a.rrd) | 
| Puzzle into groove | GPT-6 Astra | 2 | 3.9 | 3,142 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_a1a54798.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_a1a54798.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_a1a54798.rrd) | 
| Puzzle into groove | GPT-6 Astra | 1 | 2.2 | 2,458 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_f6191432.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_f6191432.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_f6191432.rrd) | 
| Puzzle into groove | GPT-6 Astra | 1 | 2.8 | 2,464 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_fb8daf2d.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_fb8daf2d.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_fb8daf2d.rrd) | 
| Puzzle into groove | GPT-6 Astra | 1 | 3.0 | 2,117 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_c4c2e75a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_c4c2e75a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_c4c2e75a.rrd) | 
| Puzzle into groove | GPT-6 Astra | 1 | 3.1 | 2,901 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_fe062fe0.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_fe062fe0.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_fe062fe0.rrd) | 
| Puzzle into groove | GPT-6 Astra | 1 | 3.9 | 3,041 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_c74997eb.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_c74997eb.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_c74997eb.rrd) | 
| Puzzle into groove | GPT-6 Astra | 1 | 10.2 | 2,491 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_3a441687.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_3a441687.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_3a441687.rrd) | 
| Puzzle into groove | GPT-6 Astra | 0 | 2.6 | 3,025 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_45cf10d2.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_45cf10d2.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_45cf10d2.rrd) | 
| Puzzle into groove | GPT-6 Astra | 0 | 2.8 | 2,916 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_281ccc8d.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_281ccc8d.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_281ccc8d.rrd) | 
| Puzzle into groove | GPT-6 Astra | 0 | 3.3 | 3,161 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_bb22303f.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_bb22303f.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_bb22303f.rrd) | 
| Puzzle into groove | Fable 5 | 3 | 5.4 | 12,599 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_452ee506.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_452ee506.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_452ee506.rrd) | 
| Puzzle into groove | Fable 5 | 3 | 6.6 | 11,044 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_0e760ca6.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_0e760ca6.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_0e760ca6.rrd) | 
| Puzzle into groove | Fable 5 | 3 | 6.7 | 11,726 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_5ba76d19.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_5ba76d19.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_5ba76d19.rrd) | 
| Puzzle into groove | Fable 5 | 3 | 6.8 | 10,743 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_2da7cfde.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_2da7cfde.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_2da7cfde.rrd) | 
| Puzzle into groove | Fable 5 | 3 | 8.8 | 14,855 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_6a99bdfd.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_6a99bdfd.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_6a99bdfd.rrd) | 
| Puzzle into groove | Fable 5 | 2 | 7.0 | 19,149 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_fb1601c3.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_fb1601c3.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_fb1601c3.rrd) | 
| Puzzle into groove | Fable 5 | 2 | 9.1 | 22,592 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_b90fd8b1.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_b90fd8b1.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_b90fd8b1.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 4.5 | 9,620 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_3f7d4c96.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_3f7d4c96.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_3f7d4c96.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 4.7 | 9,942 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_f455e605.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_f455e605.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_f455e605.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 5.3 | 13,629 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_6708f542.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_6708f542.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_6708f542.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 5.8 | 16,029 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_1bf1d77c.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_1bf1d77c.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_1bf1d77c.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 6.6 | 16,460 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_701665da.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_701665da.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_701665da.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 7.3 | 10,544 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_e888be5b.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_e888be5b.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_e888be5b.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 8.3 | 25,603 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_f26762f6.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_f26762f6.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_f26762f6.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 8.3 | 23,105 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_9e92d8b3.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_9e92d8b3.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_9e92d8b3.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 9.1 | 20,718 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_73ce3b83.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_73ce3b83.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_73ce3b83.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 15.1 | 29,746 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_658c1744.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_658c1744.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_658c1744.rrd) | 
| Puzzle into groove | Fable 5 | 1 | 17.2 | 11,577 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_fd7cfdc7.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_fd7cfdc7.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_fd7cfdc7.rrd) | 
| Puzzle into groove | Fable 5 | 0 | 6.2 | 18,229 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_a685676a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_a685676a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_a685676a.rrd) | 
| Puzzle into groove | Fable 5 | 0 | 10.0 | 18,386 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_cd296d55.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_cd296d55.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_cd296d55.rrd) | 
| Puzzle into groove | Fable 5.1 | 4 | 5.2 | 10,618 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_fd86a832.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_fd86a832.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_fd86a832.rrd) | 
| Puzzle into groove | Fable 5.1 | 4 | 7.6 | 10,306 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_d3d2906e.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_d3d2906e.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_d3d2906e.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 4.1 | 9,993 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_6aeb92f9.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_6aeb92f9.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_6aeb92f9.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 5.0 | 11,549 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_1ddcd3a0.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_1ddcd3a0.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_1ddcd3a0.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 5.4 | 10,450 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_19d5f265.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_19d5f265.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_19d5f265.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 6.0 | 10,417 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_3d4f61c3.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_3d4f61c3.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_3d4f61c3.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 6.5 | 10,725 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_3d04f389.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_3d04f389.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_3d04f389.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 7.1 | 10,312 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_2f9792ae.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_2f9792ae.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_2f9792ae.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 7.2 | 11,048 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_75cb68ae.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_75cb68ae.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_75cb68ae.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 7.4 | 11,978 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_18201d7e.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_18201d7e.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_18201d7e.rrd) | 
| Puzzle into groove | Fable 5.1 | 3 | 7.5 | 12,251 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_13d31c2f.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_13d31c2f.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_13d31c2f.rrd) | 
| Puzzle into groove | Fable 5.1 | 2 | 3.7 | 9,362 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_80e328d1.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_80e328d1.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_80e328d1.rrd) | 
| Puzzle into groove | Fable 5.1 | 2 | 4.5 | 8,946 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_86114266.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_86114266.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_86114266.rrd) | 
| Puzzle into groove | Fable 5.1 | 2 | 4.9 | 9,432 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_b23f225d.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_b23f225d.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_b23f225d.rrd) | 
| Puzzle into groove | Fable 5.1 | 2 | 6.6 | 12,046 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_93e6a606.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_93e6a606.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_93e6a606.rrd) | 
| Puzzle into groove | Fable 5.1 | 1 | 3.9 | 9,341 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_bc0ec864.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_bc0ec864.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_bc0ec864.rrd) | 
| Puzzle into groove | Fable 5.1 | 1 | 4.3 | 9,597 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_b483b6bb.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_b483b6bb.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_b483b6bb.rrd) | 
| Puzzle into groove | Fable 5.1 | 1 | 5.5 | 12,735 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_c9ce782a.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_c9ce782a.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_c9ce782a.rrd) | 
| Puzzle into groove | Fable 5.1 | 1 | 10.0 | 9,111 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_0c35809b.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_0c35809b.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_0c35809b.rrd) | 
| Puzzle into groove | Fable 5.1 | 0 | 6.5 | 10,359 | [view](https://openai.robocurve.org/runs/transcripts/rig-4_e409c0ea.html) | [watch](https://openai.robocurve.org/runs/videos/rig-4_e409c0ea.mp4) | [download](https://openai.robocurve.org/runs/rrd/rig-4_e409c0ea.rrd) | 

## Technical specifications

| Embodiment | Bimanual I2RT YAM arms, 6-DoF per arm with parallel-jaw grippers | 
| Control | Absolute end-effector poses ( `move_to` ): x, y, z, yaw, pitch, roll and gripper, per arm. The robot's IK converts poses to joint angles. | 
| Observation | Three camera views (top, left wrist, right wrist) plus proprioceptive state, each turn | 
| Policy | `agent` policy, medium thinking effort, 20-LLM-call budget, 25% speed cap, default safety guardrails on | 
| Models | `gpt-6-astra` ,`claude-fable-5` and`claude-fable-5-1` | 
| Harness | [Inspect Robots](https://github.com/robocurve/inspect-robots) 0.58.0 | 
| Trials | 20 per model per task; puzzle on rig-4 for all models, bowl on rig-3 for the Fable models and rig-1 for Astra | 
| Token counts | Wire-level request and response tokens, not billed tokens; cost at list price, $10 / $50 per million input / output tokens for all three models | 

## Limitations

- Astra's trials were run two days after the Fable trials, and not interleaved with them. The puzzle comparison is on the same rig; the bowl comparison is not: the Fable bowl trials ran on rig-3, which was unavailable.
- Grading was operator-judged with the model known, so scores are open to unconscious bias.
- Costs are list price. Anthropic requests were sent without prompt caching; OpenAI cached about a fifth of Astra's input automatically, which is not discounted here, so Astra's cost is, if anything, overstated.
- Objects were reset by hand between trials, and all models ran at medium reasoning effort only.
