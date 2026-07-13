---
title: "Nutlope/hallmark"
source: GitHub Trending
url: https://github.com/Nutlope/hallmark
date: 2026-07-13
published_at: 2026-07-13T05:33:39.973452+00:00
tag: 工具开源
item_id: bae253af31056ac5
---
**A design skill for Claude Code, Cursor, and Codex that refuses to look AI-generated.**

[Live demo →](https://www.usehallmark.com)  ·  twenty themes  ·  four verbs  ·  press `T` to cycle.

Made by Together AI.

  
![Hallmark, a design skill that refuses to look AI-generated](https://github.com/Nutlope/hallmark/raw/main/site/OG-hallmark.png)


Hallmark picks a macrostructure for the brief, dresses it in one of twenty themes, runs fifty-seven slop-test gates plus a pre-emit self-critique, and refuses the on-distribution defaults every LLM was trained into. Two pages by Hallmark for two different briefs feel like different sites, not colour-swaps of the same template.

| Verb | What it does | 
|---|---|
| (default) | Build new UI. Picks a macrostructure, applies the rule-set, runs the slop test before handing back. | 
| `hallmark audit <target>` | Score existing code against the anti-patterns. Punch list, no edits. | 
| `hallmark redesign <target>` | Throw out the structure, keep copy + IA + brand, rebuild with a different fingerprint. | 
| `hallmark study <screenshot | URL>` | Extract the DNAfrom a design you admire: macrostructure, type-pairing, colour anchor. Refuses pixel-clones and paid templates. Optionally emits a portable`design.md`for handoff to other AI tools. | 

Each generated from a different brief. The skill picks the theme, structure, and craft to fit each one, not from a template.

| ![Bubble guided sourdough app hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-hum-07.jpg) | ![Distil content-extraction API hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-cobalt-01.jpg) | ![Cold Snap record-label EP hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-carnival-01.jpg) | ![Cinder AI reasoning tool hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-lumen-01.jpg) | 
| BubbleSourdough app · Hum | DistilExtraction API · Cobalt | Cold SnapRecord label · Carnival | CinderAI tool · Lumen | 
| ![Ferns and Fathom tea menu hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-custom-03.jpg) | ![Hollowback Apiary honey farm hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-garden-01.jpg) | ![Off-Register risograph print fair hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-riso-01.jpg) | ![Press Quaternary type studio hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-press-01.jpg) | 
| Ferns & FathomTea menu · Custom | Hollowback ApiaryHoney farm · Garden | Off-RegisterPrint fair · Riso | Press QuaternaryType studio · Custom | 
| ![Tally SaaS product page hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-tally.jpg) | ![Wayfare travel booking hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-wayfare.jpg) | ![NAJM Moroccan fashion brand hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-najm.jpg) | ![Hyperlane developer infrastructure hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-hyperlane.jpg) | 
| TallySaaS · modern-minimal | WayfareTravel · atmospheric | NAJMFashion brand | HyperlaneDev infrastructure | 

Each page is self-contained HTML + CSS, stamped with its macrostructure in the CSS comment. Browse the full set at [usehallmark.com](https://www.usehallmark.com) or under [ site/_tests/](https://github.com/Nutlope/hallmark/blob/main/site/_tests).

When a brief carries creative intent that no catalog theme fits, Hallmark switches to **Custom** and designs the page from scratch: a made-to-measure palette, type, and layout. Same 57 slop-test gates, no template underneath.

| ![The Cascadia Nightjar sleeper-train ticket hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-custom-02.jpg) | ![The Mend Assembly repair-café broadsheet hero](https://github.com/Nutlope/hallmark/raw/main/docs/screenshots/hero-custom-04.jpg) | 
| The Cascadia NightjarSleeper-train ticket · Custom | The Mend AssemblyRepair-café broadsheet · Custom | 

It stays a quiet branch; vanilla briefs never see it. The protocol lives in [ custom-theme.md](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/references/custom-theme.md).

```
npx skills add nutlope/hallmark
```
Re-run any time to update. Or copy [ SKILL.md](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/SKILL.md) + 

[into:](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/references)

`references/`- **Claude Code**:- `~/.claude/skills/hallmark/`
- **Cursor**:- `.cursor/rules/hallmark.mdc`(body of- `SKILL.md`, no frontmatter)
- **Codex**:- `~/.codex/skills/hallmark/`(personal) or- `.codex/skills/hallmark/`(project-scoped)

The rule-set lives in [ SKILL.md](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/SKILL.md) and 

[. Worked examples in](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/references)

`references/`[and](https://github.com/Nutlope/hallmark/blob/main/docs/recipes.md)

`docs/recipes.md`[.](https://github.com/Nutlope/hallmark/blob/main/docs/study-examples.md)

`docs/study-examples.md`MIT. Use it, fork it, ship it.
