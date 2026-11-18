---
title: "google-research/paper-orchestra"
source: GitHub Trending
url: https://github.com/google-research/paper-orchestra
date: 2026-11-18
published_at: 2026-11-18T09:40:28.487335+00:00
tag: 工具开源
item_id: 36b7a199b395a31b
---
<sup>1</sup>, Yale Song

<sup>1</sup>, Tomas Pfister

<sup>1</sup>, and Jinsung Yoon

<sup>1</sup>

<sup>1</sup>Google Cloud AI Research

PaperOrchestra is a multi-agent framework for automated AI research paper writing. It flexibly transforms unconstrained pre-writing materials (ideas and experimental logs) into submission-ready LaTeX manuscripts, including comprehensive literature synthesis and generated visuals, such as plots and conceptual diagrams.

Acting like an orchestrated team of specialized agents, it handles outline generation, literature review, section writing, content refinement, and plotting to close the gap between raw research materials and submission ready papers.

![PaperOrchestra Overview](https://github.com/google-research/paper-orchestra/raw/main/assets/overview.png)

- **Multi-Agent Pipeline**: Orchestrates specialized agents (Outline, Literature Review, Section Writing, Content Refinement, Plotting) for end-to-end paper generation.
- **Comprehensive Literature Synthesis**: Automatically searches, prioritizes, and integrates relevant literature into the manuscript.
- **Visuals Generation**: Generates plots and supports the inclusion of conceptual diagrams.
- **LaTeX Automation**: Produces submission-ready LaTeX manuscripts adhering to target conference templates.

1. **Environment Setup**: The project relies on a Conda environment named `paper_orchestra`. You can set up a similar environment with Python 3.11 and install the required dependencies.
conda create -n paper\_orchestra python=3.11 conda activate paper\_orchestra pip install -r requirements.txt
2. **Environment Variables**: Create a `.env` file in the root of the project and add your API keys:
\# Add keys if you have them, otherwise leave them empty # You need to specify related keys if you want to use the model # For example, if you want to use Gemini models, you need to specify either VERTEX\_AI\_PROJECT and VERTEX\_AI\_LOCATION, or GEMINI\_API\_KEY # If you want to use OpenAI models, you need to specify OPENAI\_API\_KEY SEMANTIC\_SCHOLAR\_API\_KEY=your\_semantic\_scholar\_api\_key OPENAI\_API\_KEY=your\_openai\_api\_key VERTEX\_AI\_PROJECT=your\_vertex\_ai\_project VERTEX\_AI\_LOCATION=your\_vertex\_ai\_location GEMINI\_API\_KEY=your\_gemini\_api\_key # if you want to run demo and send emails to yourself at the end, set these 2 fields as well SMTP\_EMAIL=your\_email SMTP\_PASSWORD=your\_password

The dataset used for paper generation is **not included** in this code repository. It will be released separately at a later date.
Once available, you should download the dataset and place it under the `datasets/` directory.

You can run the paper generation pipeline using the provided bash script or directly via the Python CLI.

`./paper_writing_cli.sh````
python paper_writing_cli.py \
  --raw_materials_dir /path_to_your_raw_materials/ \
  --latex_template_dir /path_to_your_latex_template/ \
  --output_dir /path_to_your_output_folder/ \
  --use_plotting true
```
- `--raw_materials_dir`: (Required) Directory containing the raw materials (e.g., idea and experimental log).
- `--latex_template_dir`: (Required) Directory containing the LaTeX template (e.g., `templates/cvpr2025`).
- `--output_dir`: Directory to output the generated paper. If not specified, an automatic folder with a timestamp is created.
- `--use_plotting`: Enable the plotting agent workflow to generate figures from code (Default: `False`).
- `--writer_model_name`: LLM for writer and literature agents.
- `--reflection_model_name`: LLM for reflection agents.

We provide an interactive Streamlit demo for the paper generation pipeline. For instructions on how to run and use it, please refer to the [README.md](https://github.com/google-research/paper-orchestra/blob/main/frontend/README.md) in the `frontend` directory.

- `autoraters/`: Contains scripts for automated evaluation.
- `methods/`: Core logic for agents and pipeline execution.
- `templates/`: LaTeX templates for target conferences, you can add your own template by creating a new subfolder under this directory.
- `utils/`: Utility functions for API calls, PDF handling, etc.

If you find this repo or our paper helpful, please cite it as follows:

```
@article{song2026paperorchestra,
  title={PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing},
  author={Song, Yiwen and Song, Yale and Pfister, Tomas and Yoon, Jinsung},
  journal={arXiv preprint arXiv:2604.05018},
  year={2026}
}
```
This is not an officially supported Google product.
