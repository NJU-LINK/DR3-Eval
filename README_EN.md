<h1 align="center">DR<sup>3</sup>-Eval: Towards Realistic and Reproducible<br>Deep Research Evaluation</h1>

<p align="center">
  <a href="https://arxiv.org/abs/xxxx.xxxxx">
    <img src="https://img.shields.io/badge/Paper-ArXiv-red.svg" alt="Arxiv Paper">
  </a>
  <a href="https://huggingface.co/datasets/NJU-LINK/DR3-Eval">
    <img src="https://img.shields.io/badge/🤗%20HuggingFace-Dataset-yellow.svg" alt="HuggingFace Dataset">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-Apache%202.0-green.svg" alt="License">
  </a>
</p>

<p align="center">
  <a href="README_ZH.md">中文</a> | <b>English</b>
</p>

---

## ✨ Overview

**DR³-Eval** is a **realistic, reproducible, and multimodal** evaluation benchmark for Deep Research Agents, focusing on multi-file report generation tasks.

Existing benchmarks face a fundamental tension between **realism**, **controllability**, and **reproducibility** when evaluating deep research agents. DR³-Eval addresses this through the following design:

- 🔬 **Real User Scenarios**: Tasks are constructed from real user-provided multimodal files, covering **3 major domains and 13 sub-domains**
- 📦 **Static Sandbox Corpora**: An independent static research sandbox is built for each task, containing supportive, distracting, and noisy documents
- 🎯 **Reverse Construction Method**: Queries are reverse-engineered from verified evidence documents, eliminating evaluation ambiguity
- 📊 **Multi-dimensional Evaluation**: Five dimensions — Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality

<p align="center">
  <img src="assets/intro.png" width="88%" alt="Comparison of DR³-Eval with other benchmarks">
  <br>
  <em>Figure 1. Comparison of DR³-Eval with existing deep research benchmarks. DR³-Eval supports both user files and sandbox corpora, providing a realistic and reproducible multimodal evaluation environment.</em>
</p>

---

## 📰 News

- 📦 **HuggingFace Dataset**: The DR³-Eval dataset is now available on HuggingFace! Download it directly from [HuggingFace](https://huggingface.co/datasets/NJU-LINK/DR3-Eval).

---

## 🏆 Benchmark Comparison

DR³-Eval is the first deep research evaluation benchmark that simultaneously satisfies all of the following: user file input, static sandbox corpora, multimodality, real-world scenarios, multi-file upload, and reverse construction.

<p align="center">
  <img src="assets/benchmark_comparison.png" width="88%" alt="Benchmark Comparison">
  <br>
  <em>Figure 2. Comprehensive comparison of DR³-Eval with representative benchmarks.</em>
</p>

---

## 🧩 Framework and Pipeline

The overall framework of DR³-Eval consists of three core components:

1. 📝 **Data Construction**: Synthesizes search paths from real multimodal files through a diverge-converge mechanism, establishes static sandboxes with controllable signal-to-noise ratios, and generates queries via reverse engineering
2. 🤖 **DR³-Agent**: Hierarchical multi-agent architecture (see next section)
3. 📊 **Evaluation Protocol**: A multi-dimensional metric suite that comprehensively evaluates evidence retrieval and report generation performance

<p align="center">
  <img src="assets/framework.png" width="88%" alt="Framework Overview">
  <br>
  <em>Figure 3. DR³-Eval framework overview. Includes data construction, DR³-Agent multi-agent system, and multi-dimensional evaluation protocol.</em>
</p>

---

## 🤖 DR³-Agent

To validate the effectiveness of DR³-Eval, we developed **DR³-Agent** — an LLM-driven multi-agent deep research system built on the [MiroFlow](https://github.com/MiroMindAI/miroflow) framework. Its core architecture is as follows:

- **Main Agent**: The reasoning hub of the system, integrating perception tools for video, audio, etc. It maintains global task context, runs a dynamic "Plan-Execute-Observe" loop, and coordinates sub-agents to complete information retrieval tasks
- **RAG Search Sub-agent**: Interacts with the static sandbox corpus using an iterative dense retrieval mechanism based on `text-embedding-3-small`, refining queries under the ReAct paradigm to obtain evidence
- **File Reading Sub-agent**: Specializes in parsing long-form user files, supporting keyword queries and page-number-based content retrieval

Sub-agents do not share global state; they only return highly condensed summaries to the main agent to reduce its context burden.

---

## 📊 Dataset Statistics

- **100** independent tasks (50 English + 50 Chinese)
- **3** major domains, **13** sub-domains
- **68%** of tasks involve multimodal input
- Average of **2.24** user files per task, up to 6
- Sandbox corpus contains an average of **465.5** web pages under the 512k configuration

<p align="center">
  <img src="assets/data_stas.png" width="88%" alt="Dataset Statistics">
  <br>
  <em>Figure 4. Dataset statistics. (a) Domain distribution. (b) File type distribution. (c) Distribution of user files per task.</em>
</p>

---

## 📐 Evaluation Metrics

| Dimension | Metric | Description |
|-----------|--------|-------------|
| **Information Retrieval** | IR (Information Recall) | Coverage of key insights from user files and sandbox corpus in the report |
| **Information Retrieval** | CC (Citation Coverage) | Extent to which the report cites necessary source documents |
| **Report Generation** | FA (Factual Accuracy) | Factual correctness of cited claims in the report |
| **Report Generation** | IF (Instruction Following) | Whether the report satisfies all requirements specified in the task query |
| **Report Generation** | DQ (Depth Quality) | Analytical depth and logical rigor of the report |

---

## 📈 Experimental Results

Comprehensive evaluation was conducted on 8 state-of-the-art LLMs. **Key findings**:

1. DR³-Eval is **extremely challenging** — the best model, Claude Sonnet 4, achieves only 65.6 average score under 512k
2. **Longer context → Lower performance** — Noise and distracting information make it difficult for models to locate effective evidence
3. **Instruction following ≠ Factual accuracy** — Some models generate reports that "look" complete but contain factual errors
4. **Significant performance variation across domains**

<p align="center">
  <img src="assets/main_results.png" width="88%" alt="Main Experimental Results">
  <br>
  <em>Figure 5. Evaluation results of different models under 64k/128k/512k sandbox scales.</em>
</p>

<p align="center">
  <img src="assets/heatmap_no8b.png" width="88%" alt="Cross-domain Performance Heatmap">
  <br>
  <em>Figure 6. Performance heatmap of different models across 13 domains.</em>
</p>

<details>
<summary>📦 More Experimental Results</summary>

<p align="center">
  <img src="assets/scaele_results.png" width="85%" alt="Scale Analysis">
  <br>
  <em>Figure 7. Performance trends under different sandbox corpus scales (32k–512k).</em>
</p>

<p align="center">
  <img src="assets/error_types_font.png" width="85%" alt="Error Type Analysis">
  <br>
  <em>Figure 8. Error type distribution across different models. Hallucination is the primary cause of failure for most models.</em>
</p>

<p align="center">
  <img src="assets/ablation_longcontext-rag.png" width="85%" alt="Ablation Study">
  <br>
  <em>Figure 9. Ablation study comparing long-context vs. RAG approaches.</em>
</p>

<p align="center">
  <img src="assets/online.png" width="85%" alt="Sandbox vs. Online Corpus">
  <br>
  <em>Figure 10. Performance comparison between static sandbox corpus and real-world web search.</em>
</p>

<p align="center">
  <img src="assets/retrieve.png" width="85%" alt="Retriever Analysis">
  <br>
  <em>Figure 11. Comparison of different retrieval methods.</em>
</p>

<p align="center">
  <img src="assets/人类一致性.png" width="85%" alt="Human Evaluation Consistency">
  <br>
  <em>Figure 12. Consistency analysis between LLM-as-Judge and human evaluation.</em>
</p>

</details>

---

## 🚀 Quick Start

### 📥 Dataset Access

The dataset is hosted on [HuggingFace](https://huggingface.co/datasets/NJU-LINK/DR3-Eval) and can be downloaded directly.

### 🔧 Environment Setup

```bash
# Install dependencies
uv sync

# Configure environment variables
cp .env.example .env
# Edit .env to fill in API keys (OPENROUTER_API_KEY, etc.)

# Verify installation
uv run python main.py --help
```

### ▶️ Running DR³-Agent

```bash
# Single task
uv run python main.py run \
    --folder data/datasets_en/001 \
    --query "Analyze the documents and generate a research report." \
    --offline

# Batch tasks
uv run python main.py batch \
    --data-dir data/datasets_en \
    --context-size 128k \
    --llm-config gpt-4 \
    --offline
```

### 📊 Evaluation

```bash
uv run python eval.py all \
    --result-base results_main/datasets_en \
    --datasets-dir data/datasets_en \
    --workers 4
```

---

## 📝 Citation

If you find this work useful, please cite:

```bibtex
@article{dr3eval2026,
  title={DR3-Eval: Towards Realistic and Reproducible Deep Research Evaluation},
  author={},
  journal={arXiv preprint arXiv:xxxx.xxxxx},
  year={2026}
}
```

## 🌟 License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgements

The DR³-Agent in this project is built on the [MiroFlow](https://github.com/MiroMindAI/miroflow) framework by [MiroMind AI](https://github.com/MiroMindAI). We extended it with the DR³-Eval evaluation framework, including multi-dimensional report quality metrics, benchmark support, and multi-model comparison capabilities.

## 📧 Contact

For questions, please reach out via GitHub Issues.

---

**NJU-LINK Team, Nanjing University**
