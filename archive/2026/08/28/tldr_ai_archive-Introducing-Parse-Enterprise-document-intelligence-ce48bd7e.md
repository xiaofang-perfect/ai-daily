---
title: "Introducing Parse: Enterprise document intelligence at scale"
source: TLDR AI · 2026-08-28
url: https://cohere.com/blog/parse?utm_source=tldrai
date: 2026-08-28
published_at: 2026-08-28T12:00:00+00:00
tag: 产品发布
item_id: ce48bd7e01f68ab6
---
Key takeaways

- **Best-in-class value** : outperforms leading document parsers and hyperscaler services while remaining cost-effective at enterprise scale.
- **Beyond OCR** : understands tables, forms, diagrams, and images to extract richer semantic context across key global commercial languages.
- **Enterprise-first** : trained to handle business documents in major industries and domains, such as finance, insurance, and scientific work.
- **Spatially aware** : returns bounding boxes for visual elements, preserving document structure for retrieval, grounding, and automation.
- **Available in Compass** : use Parse today as part of Cohere’s Compass search and retrieval stack - alongside Embed, and Rerank.
- **Secure deployments** : run in any private cloud or on-premises environment to match your organization's security and compliance profile.

Cohere Parse is a cost-effective vision language model for processing large volumes of enterprise documents. It converts complex, multimodal files into structured, machine-readable data that can power enterprise knowledge use cases–including document indexing, RAG, and agentic retrieval.

More than text recognition, Parse detects and understands key visual elements - such as tables and embedded images - and returns clean Markdown files for downstream processing and application. Use Parse to process your documents and images across nine major world languages.

Parse is designed to preserve parsing quality and keep inference costs predictable as workloads scale. It supports the high-throughput needed in production environments. Customers can access Parse through the [Cohere API](http://dashboard.cohere.com) for just $1.50 per 1,000 pages, or deploy in [Model Vault](http://dashboard.cohere.com) for secure, single-tenant inference and even further cost savings per page. Teams in regulated industries can deploy Parse securely on their own infrastructure with a minimal serving footprint.

Want to try it first? See how Cohere Parse handles your documents for free using our [Space](https://huggingface.co/spaces/CohereLabs/cohere-parse).

### Performance

Cohere Parse delivers the *strongest price–performance tradeoff* among the models we evaluated. It is a highly competitive model that outperforms leading specialized document parsing solutions while maintaining a price point suitable for high-volume workloads spanning hundreds of thousands to millions of pages.

![](https://cdn.sanity.io/images/rjtqmwfu/web3-prod/998be854bd3fd9f57b5e998ebf834cb7c50b95fb-3140x2044.png?auto=format&fit=max&q=80&w=800)

On [ParseBench](https://www.parsebench.ai/) - which measures agent-suitable parsing performance - Parse scores 79.2 across three evaluation dimensions compared with 74.5 for Mistral OCR 4, 72.4 for Databricks AI Parse, and 78.3 for LlamaParse’s Cost Effective offering.

This performance gap is even larger compared with hyperscaler document intelligence solutions, with an over 20-point improvement on both AWS Textract and Google Document AI. In our evaluation set, Parse is only bettered by the frontier LLMs (GPT-5.5, Opus 4.8 and Gemini 3.5 Flash) - each general purpose and significantly larger than Parse.

![](https://cdn.sanity.io/images/rjtqmwfu/web3-prod/050e4caa8871604c6b34af21a87b43b22eb579e0-3140x2020.png?auto=format&fit=max&q=80&w=800)

| Model | Average | Tables | Content Faithfulness | Semantic Formatting | 
|---|---|---|---|---|
| **Cohere Parse** | **79.2** | **87.0** | **86.6** | **64.0** | 
| GPT-5.5 | 84.4 | 89.3 | 87.5 | 76.5 | 
| Opus 4.8 | 84.3 | 89.7 | 89.0 | 74.1 | 
| Gemini 3.5 Flash | 81.8 | 87.6 | 84.7 | 73.2 | 
| LlamaParse (Cost Effective) | 78.3 | 81.4 | 90.9 | 62.7 | 
| Chandra OCR 2 (open) | 77.7 | 89.2 | 83.7 | 60.3 | 
| Mistral OCR 4 | 74.5 | 73.9 | 89.5 | 60.1 | 
| Databricks AI Parse | 72.4 | 83.7 | 88.3 | 45.3 | 
| Azure Document Intelligence | 69.3 | 86.0 | 84.9 | 37.0 | 
| Deepseek-OCR 2 (open) | 65.9 | 61.7 | 82.0 | 54.0 | 
| dots.mocr (open) | 63.2 | 85.2 | 89.5 | 14.9 | 
| Google Document AI | 57.3 | 55.1 | 83.7 | 33.0 | 
| AWS Textract | 53.3 | 82.3 | 74.8 | 2.8 | 

[ParseBench](https://www.parsebench.ai/) scores by capability dimension. Tables tests for accurate structural extraction of data grids and cells. Content Faithfulness tests for text omissions, hallucinations, and broken reading order. Semantic Formatting <sup>1</sup> measures a model’s ability to capture styles that change data meaning, such as strike-throughs or italics. This evaluation did not test for Charts or Visual Grounding <sup>2</sup>.  (Zhang *et al.*, 2026)

In terms of throughput, Cohere Parse processes 4.5 pages per second (36 pages per second or 2160 pages per minute on an 8 H100 GPU node) - approximately 1.4x the throughput of RedNote's dots.mocr and 2.2x that of Chandra OCR 2 on the same GPU configuration.

![](https://cdn.sanity.io/images/rjtqmwfu/web3-prod/9ee315ad9370ba3858109837cc27de9ffd8d70db-3140x1324.png?auto=format&fit=max&q=80&w=800)

[vLLM](http://docs.vllm.ai/).

Parse is available through both the Cohere API and Model Vault, Cohere's secure, single-tenant platform for managed inference. For sustained, high-volume production workloads, we recommend Model Vault, which delivers significant cost savings as utilization grows. At 50% GPU utilization, Model Vault reduces inference costs by 23% compared with the Cohere API. At full hourly utilization, those savings can grow to 61%.

Consider a large enterprise accounts payable workflow processing approximately 13 million document pages per month. At this scale, deploying Cohere Parse through Model Vault instead of the Cohere API would reduce inference costs by approximately $12,000 per month, or $144,000 annually. Compared with a hyperscaler offering priced at $10 per 1,000 pages, annual savings would be approximately $1.47 million for this single workflow.

### What you can build with Parse

Parse provides the foundation for the full document intelligence stack. Use Parse for:

*Automated document processing* – Extract structured data from high-volume documents such as claims, contracts, and invoices without manual review or data entry.

*Semantic search and RAG* – Build higher-quality retrieval systems with representations optimized for chunking, indexing, and citation.

*Multimodal agents* – Equip AI agents with context they need for autonomous workflows and action-taking.

### The Cohere Search ecosystem

Parse is also available as part of [Compass](https://cohere.com/compass), alongside [Embed](https://cohere.com/embed) and [Rerank](https://cohere.com/rerank).

All our models are designed to work both independently and together. Adopt the components you need, or deploy the full managed platform for an integrated document-to-answer pipeline.

This is great for users who want:

- A single, easy-to-configure interface for document ingestion, parsing, chunking, embedding, indexing, hybrid search, and two-stage retrieval.
- Support for a broader range of document formats (including .xlsx, .docx, and .html) without building and maintaining custom preprocessing pipelines.
- Smart parsing that automatically routes documents through text or vision pathways to optimize latency and token usage.
- Fully managed indexes, including seamless embedding model upgrades without re-ingesting your data.
- Multi-tenant deployments with document-level access controls for sensitive workloads.
- Out-of-the-box connectors for your cloud storage systems such as SharePoint and Google Drive.

### Getting started

Parse is now generally available via the Cohere API, Model Vault, Microsoft Foundry, and AWS SageMaker.

[Visit our dashboard](https://app.notion.com/p/Announcement-blog-39c4398375db801bbe89cc3b63b3ad68?pvs=21) to create an API key or configure a new Vault, then use the code below to begin parsing.

```
import base64
import os
import requests
API_KEY = os.environ["CO_API_KEY"]
IMAGE_PATH = "YOUR_IMAGE.png"
with open(IMAGE_PATH, "rb") as f:
    image = base64.b64encode(f.read()).decode("utf-8")
response = requests.post(
    "https://api.cohere.com/v2/parse",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "parse-v5.0",
        "document": {
            "type": "image_url",
            "image_url": f"data:image/png;base64,{image}",
        },
        "output_format": "markdown",
    },
)
response.raise_for_status()
result = response.json()
markdown = "\n\n".join(
    page["markdown"]["content"] for page in result["pages"]
)
with open("parsed_output.md", "w", encoding="utf-8") as f:
    f.write(markdown)
print("Saved to parsed_output.md")
```
### Resources

### Footnotes

<sup>1</sup> 

All ParseBench scores reported here use the latest evaluation rules as of Aug 2026, which includes a fix to bold/heading detection that previously inflated Semantic Formatting scores. For a fair comparison, we re-scored all competitor models using their inference outputs against the updated rules.

<sup>2</sup> 

We exclude the Layout and Chart dimensions from our ParseBench comparison because they measure capabilities outside our current product scope, not model quality deficiencies:

- Layout scores element-level spatial detection (bbox + class label matching). Our model is designed to produce reading-order markdown — it does not emit per-element bounding boxes for text, only for tables or images. Scoring low on this dimension reflects an intentional output-format choice, not a transcription failure.
- Chart scores extraction of numerical data series from chart images into structured tables. Our model treats charts as visual elements with descriptive metadata, not as data-extraction targets. This is a product scoping decision — chart data extraction is planned for the next Parser version.

On the three dimensions that align with our product goals — Tables, Text Content, and Text Formatting — we report full results. These cover the structured transcription and semantic fidelity that our model is trained and optimized for.
