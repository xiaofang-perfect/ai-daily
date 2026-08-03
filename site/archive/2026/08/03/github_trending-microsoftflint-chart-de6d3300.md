---
title: "microsoft/flint-chart"
source: GitHub Trending
url: https://github.com/microsoft/flint-chart
date: 2026-08-03
published_at: 2026-08-03T05:38:09.459385+00:00
tag: 工具开源
item_id: de6d3300b4e40fff
---
#  Flint: A Visualization Language for the AI Era
![](/microsoft/flint-chart/raw/main/assets/flint-logo.svg)






**Please visit:** [**Flint Project Site**](https://microsoft.github.io/flint-chart/) | [**MCP Server Guide**](https://microsoft.github.io/flint-chart/#/mcp) | **中文主页**

Flint is a visualization intermediate language that lets **AI agents create
expressive, polished visualizations from simple, human-editable chart specs**.
Instead of asking agents or developers to tune verbose chart configuration
details such as scales, axes, spacing, labels, and layout, the Flint compiler
derives optimized chart settings from the data, semantic types, chart type, and
encodings. The result is a compact chart specification that agents can produce
reliably, people can edit directly, and multiple backends can render as native
[Vega-Lite](https://vega.github.io/vega-lite/),
[ECharts](https://echarts.apache.org/),
[Chart.js](https://www.chartjs.org/), or
[Plotly](https://plotly.com/javascript/) specs, and native Excel charts through Office.js.

This repo contains two main components:

- **`flint-chart`** : a JavaScript/TypeScript library that compiles the same
Flint input into Vega-Lite, ECharts, Chart.js, Plotly, or Excel-native output.
- **`flint-chart-mcp`** : an MCP server that lets agents create, validate, and
render charts directly from a chat or coding environment.

  
![A wall of charts produced by Flint across its supported visualization backends.](https://github.com/microsoft/flint-chart/raw/main/docs/figs/chartwall.png)


- **Semantic chart specs.** Flint captures what each field means using 70+
semantic types such as`Rank` ,`Temperature` ,`Price` , or`Country` .
- **Automatic layout.** Flint adapts sizing, spacing, labels, marks, and legends
to the data cardinality, chart design, and canvas constraints.
- **Multiple backends.** Compile one input to backend-native output across[Vega-Lite](https://vega.github.io/vega-lite/) ,[ECharts](https://echarts.apache.org/) ,[Chart.js](https://www.chartjs.org/) ,[Plotly](https://plotly.com/javascript/) , and native Excel charts.
- **Agent-ready chart authoring.** The MCP server gives agents Flint tools and
chart guidance so they can choose a template, validate it, and open an
interactive chart view in MCP-capable clients.

- **July 24, 2026** — Flint 0.4.0 adds 38 Plotly chart types and 18 native,
editable Excel chart templates. ([v0.4.0](https://github.com/microsoft/flint-chart/releases/tag/0.4.0) )
- **July 19, 2026** — Flint 0.3.0 adds dynamic chart widgets that switch chart
types and edit chart properties in place. ([v0.3.0](https://github.com/microsoft/flint-chart/releases/tag/0.3.0) )
- **July 15, 2026** — Flint 0.2.2 added compact dodge modes and grouped violin
layouts.
- **July 13, 2026** — Flint 0.2.1 improved chart-property validation and backend
consistency. ([v0.2.1](https://github.com/microsoft/flint-chart/releases/tag/0.2.1) )

See the [changelog](https://github.com/microsoft/flint-chart/blob/main/CHANGELOG.md) for complete release notes.

  
  ![Flint compiling a compact chart spec into a Vega-Lite spec and rendered heatmap visualization.](https://github.com/microsoft/flint-chart/raw/main/docs/figs/compile-demo.png)


  <sub>Flint turns compact chart specs into backend-native specs and rendered visualizations.</sub>

```
# Use Flint in your JavaScript/TypeScript codebase
npm install flint-chart
# For agents and MCP clients
npx -y flint-chart-mcp
```
<sub>Python package: to be released. The current Python port is a source-only preview in this repo.</sub>

Every backend accepts the same `ChartAssemblyInput` and returns the target
library's native spec object.

```
import { assembleVegaLite } from 'flint-chart';
const spec = assembleVegaLite({
  data: { values: myData },
  semantic_types: { weight: 'Quantity', mpg: 'Quantity', origin: 'Country' },
  chart_spec: {
    chartType: 'Scatter Plot',
    encodings: { x: { field: 'weight' }, y: { field: 'mpg' }, color: { field: 'origin' } },
    baseSize: { width: 400, height: 300 },
  },
});
// → a ready-to-render Vega-Lite spec
```
Swap the backend without changing the input shape:

```
import { assembleECharts, assembleChartjs, assemblePlotly, assembleExcel } from 'flint-chart';
const echartsOption = assembleECharts(input);
const chartjsConfig = assembleChartjs(input);
const plotlyFigure = assemblePlotly(input);
const excelArtifact = assembleExcel(input);
```
See the [API reference](https://github.com/microsoft/flint-chart/blob/main/docs/api-reference.md), backend references for
[Vega-Lite](https://github.com/microsoft/flint-chart/blob/main/docs/reference-vegalite.md), [ECharts](https://github.com/microsoft/flint-chart/blob/main/docs/reference-echarts.md),
[Chart.js](https://github.com/microsoft/flint-chart/blob/main/docs/reference-chartjs.md), [Plotly](https://github.com/microsoft/flint-chart/blob/main/docs/reference-plotly.md), and
[Excel](https://github.com/microsoft/flint-chart/blob/main/docs/reference-excel.md), plus the
[live editor](https://microsoft.github.io/flint-chart/#/editor) for more library examples.

Install `flint-chart-mcp` as a [Model Context Protocol](https://modelcontextprotocol.io/)
server when you want an agent to create charts in the same conversation where
the question starts. It can open an interactive chart view, return static
PNG/SVG output, or produce backend-native chart specs.

For setup, start with the
[Flint MCP project page](https://microsoft.github.io/flint-chart/#/mcp). It
includes client configuration, usage examples, and links to deeper references.

  
![Agent chat showing Flint Chart as an MCP App with a grouped bar chart preview and chart options.](https://github.com/microsoft/flint-chart/raw/main/docs/figs/flint-mcp-experience.png)


MCP calls let agents embed rows directly as `data.values`, or read local JSON,
CSV, or TSV files by `data.url`. For agent workflows without MCP,
use the standalone [agent skill](https://github.com/microsoft/flint-chart/blob/main/agent-skills/flint-chart-author/SKILL.md).

```
flint-chart/
├── packages/
│   ├── flint-js/          npm package `flint-chart` (TypeScript)
│   │   └── src/
│   │       ├── core/      semantics, layout, decisions, shared types
│   │       ├── vegalite/  Vega-Lite backend
│   │       ├── echarts/   ECharts backend
│   │       ├── chartjs/   Chart.js backend
│   │       └── test-data/ fixtures + generators (drive tests and the gallery)
│   ├── flint-py/          Python port preview (package to be released)
│   └── flint-mcp/         npm package `flint-chart-mcp` (MCP render server)
├── site/                  Vite + React demo: landing, gallery, editor, docs
├── agent-skills/          fallback copy of the MCP-served agent skill
├── shared/test-data/      JSON fixtures shared across JS + Python
└── docs/                  architecture and design documents
```
The [project site](https://microsoft.github.io/flint-chart/) is the main entry
point for examples, the live editor, and concept docs. For source-level
references, start with the [API reference](https://github.com/microsoft/flint-chart/blob/main/docs/api-reference.md), the
[Flint MCP project page](https://microsoft.github.io/flint-chart/#/mcp), or the
[Development guide](https://github.com/microsoft/flint-chart/blob/main/docs/DEVELOPMENT.md). See the [changelog](https://github.com/microsoft/flint-chart/blob/main/CHANGELOG.md) for
notable changes in each release.

Contributions are welcome! See [.github/CONTRIBUTING.md](https://github.com/microsoft/flint-chart/blob/main/.github/CONTRIBUTING.md)
and the [Development guide](https://github.com/microsoft/flint-chart/blob/main/docs/DEVELOPMENT.md).

```
git clone https://github.com/microsoft/flint-chart
cd flint-chart
npm install            # root workspaces: packages/flint-js + flint-mcp + site
npm run typecheck      # typecheck packages/flint-js + packages/flint-mcp
npm run test           # Vitest (packages/flint-js + packages/flint-mcp)
npm run build          # build packages/flint-js + packages/flint-mcp
npm run site           # demo site (gallery + editor) at http://localhost:5274/
```
Node 18+ is required. The demo site aliases `flint-chart` to
`packages/flint-js/src`, so library edits hot-reload in the gallery and editor
without rebuilding `dist/`.

We especially welcome contributions that add new
[chart templates](https://github.com/microsoft/flint-chart/blob/main/docs/adding-a-chart-template.md) or new
[rendering backends](https://github.com/microsoft/flint-chart/blob/main/docs/adding-a-backend.md).

This project has adopted the
[Microsoft Open Source Code of Conduct](https://github.com/microsoft/flint-chart/blob/main/.github/CODE_OF_CONDUCT.md). See
[SECURITY.md](https://github.com/microsoft/flint-chart/blob/main/.github/SECURITY.md) to report vulnerabilities.

Flint is built by [Microsoft Research](https://www.microsoft.com/en-us/research/)
in collaboration with the [IDEAS Lab](https://ideas-lab.net/), Renmin University
of China. We welcome you to join us — see [Contributing](https://github.com#contributing) to get involved.

A research paper describing Flint is coming soon.

This project may contain trademarks or logos for projects, products, or services.
Authorized use of Microsoft trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not
cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks
or logos is subject to those third parties' policies.

[MIT](https://github.com/microsoft/flint-chart/blob/main/LICENSE) © Microsoft Corporation
