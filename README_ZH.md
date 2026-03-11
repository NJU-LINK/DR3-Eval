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
  <b>中文</b> | <a href="README_EN.md">English</a>
</p>

---

## ✨ 概述

**DR³-Eval** 是一个面向深度研究智能体的**真实、可复现、多模态**评测基准，专注于多文件报告生成任务的评估。

现有基准在评估深度研究智能体时面临**真实性**、**可控性**和**可复现性**之间的根本矛盾。DR³-Eval 通过以下设计解决这一问题：

- 🔬 **真实用户场景**：任务基于真实用户提供的多模态文件构建，涵盖 **3 大领域、13 个子领域**
- 📦 **静态沙盒语料库**：为每个任务构建独立的静态研究沙盒，包含支持性文档、干扰文档和噪声文档
- 🎯 **反向构建方法**：从已验证的证据文档反向推导查询，消除评估歧义
- 📊 **多维度评估**：信息召回、事实准确性、引用覆盖、指令遵循、深度质量五个维度

<p align="center">
  <img src="assets/intro.png" width="88%" alt="DR³-Eval 与其他基准的对比">
  <br>
  <em>图 1. DR³-Eval 与现有深度研究基准的对比。DR³-Eval 同时支持用户文件和沙盒语料库，提供真实、可复现的多模态评测环境。</em>
</p>

---

## 📰 动态

- 📦 **HuggingFace 数据集**：DR³-Eval 数据集已上线 HuggingFace！可直接从 [HuggingFace](https://huggingface.co/datasets/NJU-LINK/DR3-Eval) 下载使用。

---

## 🏆 基准对比

DR³-Eval 是首个同时满足以下所有条件的深度研究评测基准：用户文件输入、静态沙盒语料库、多模态、真实场景、多文件上传和反向构建。

<p align="center">
  <img src="assets/benchmark_comparison.png" width="88%" alt="基准对比">
  <br>
  <em>图 2. DR³-Eval 与代表性基准的全面对比。</em>
</p>

---

## 🧩 框架与流程

DR³-Eval 的整体框架包含三个核心部分：

1. 📝 **数据构建**：通过发散-收敛机制从真实多模态文件中合成搜索路径，建立具有可控信噪比的静态沙盒，并通过反向推导生成查询
2. 🤖 **DR³-Agent**：层次化多智能体架构（详见下节）
3. 📊 **评估协议**：多维度指标套件，全面评估证据获取和报告生成的性能

<p align="center">
  <img src="assets/framework.png" width="88%" alt="框架概览">
  <br>
  <em>图 3. DR³-Eval 框架概览。包括数据构建、DR³-Agent 多智能体系统和多维度评估协议。</em>
</p>

---

## 🤖 DR³-Agent

为验证 DR³-Eval 的有效性，我们开发了 **DR³-Agent**——一个基于 [MiroFlow](https://github.com/MiroMindAI/miroflow) 框架的 LLM 驱动多智能体深度研究系统。其核心架构如下：

- **主智能体（Main Agent）**：系统的推理中枢，集成了视频、音频等感知工具，维护全局任务上下文，运行动态的"计划-执行-观察"循环，协调子智能体完成信息获取任务
- **RAG 搜索子智能体**：与静态沙盒语料库交互，采用基于 `text-embedding-3-small` 的迭代密集检索机制，在 ReAct 范式下精炼查询以获取证据
- **文件阅读子智能体**：专门解析长文本用户文件，支持关键词查询和按页码检索内容

子智能体不共享全局状态，仅向主智能体返回高度浓缩的摘要，以减轻主智能体的上下文负担。

---

## 📊 数据集统计

- **100** 个独立任务（50 英文 + 50 中文）
- **3** 大领域、**13** 个子领域
- **68%** 的任务涉及多模态输入
- 每个任务平均 **2.24** 个用户文件，最多 6 个
- 512k 配置下沙盒语料库平均含 **465.5** 个网页

<p align="center">
  <img src="assets/data_stas.png" width="88%" alt="数据集统计">
  <br>
  <em>图 4. 数据集统计。(a) 领域分布。(b) 文件类型分布。(c) 每个任务的用户文件数量分布。</em>
</p>

---

## 📐 评估指标

| 维度               | 指标             | 描述                                         |
| ------------------ | ---------------- | -------------------------------------------- |
| **信息检索** | IR（信息召回）   | 报告对用户文件和沙盒语料库中关键洞察的覆盖率 |
| **信息检索** | CC（引用覆盖）   | 报告对必要来源文档的引用覆盖程度             |
| **报告生成** | FA（事实准确性） | 报告中引用声明的事实正确性                   |
| **报告生成** | IF（指令遵循）   | 报告是否满足任务查询中的各项要求             |
| **报告生成** | DQ（深度质量）   | 报告的分析深度和逻辑严谨性                   |

---

## 📈 实验结果

在 8 个最先进的 LLM 上进行了全面评估。**核心发现**：

1. DR³-Eval **极具挑战性**——最优模型 Claude Sonnet 4 在 512k 下平均分仅 65.6
2. **更长上下文 → 更低性能**——噪声和干扰信息使模型难以定位有效证据
3. **指令遵循 ≠ 事实准确**——部分模型生成"看起来"完整但事实错误的报告
4. **不同领域表现差异显著**

<p align="center">
  <img src="assets/main_results.png" width="88%" alt="主要实验结果">
  <br>
  <em>图 5. 不同模型在 64k/128k/512k 三种沙盒规模下的评估结果。</em>
</p>

<p align="center">
  <img src="assets/heatmap_no8b.png" width="88%" alt="跨领域性能热力图">
  <br>
  <em>图 6. 不同模型在 13 个领域上的性能热力图。</em>
</p>

<details>
<summary>📦 更多实验结果</summary>

<p align="center">
  <img src="assets/scaele_results.png" width="85%" alt="规模分析">
  <br>
  <em>图 7. 不同沙盒语料库规模（32k-512k）下的性能变化趋势。</em>
</p>

<p align="center">
  <img src="assets/error_types_font.png" width="85%" alt="错误类型分析">
  <br>
  <em>图 8. 不同模型的错误类型分布。幻觉是大多数模型失败的主要原因。</em>
</p>

<p align="center">
  <img src="assets/ablation_longcontext-rag.png" width="85%" alt="消融实验">
  <br>
  <em>图 9. 长上下文与 RAG 方法的消融实验对比。</em>
</p>

<p align="center">
  <img src="assets/online.png" width="85%" alt="沙盒与在线语料库对比">
  <br>
  <em>图 10. 静态沙盒语料库与真实网络搜索的性能对比分析。</em>
</p>

<p align="center">
  <img src="assets/retrieve.png" width="85%" alt="检索器分析">
  <br>
  <em>图 11. 不同检索方法的效果对比。</em>
</p>

<p align="center">
  <img src="assets/人类一致性.png" width="85%" alt="人类评估一致性">
  <br>
  <em>图 12. LLM-as-Judge 与人类评估的一致性分析。</em>
</p>

</details>

---

## 🚀 快速开始

### 📥 数据集获取

数据集托管在 [HuggingFace](https://huggingface.co/datasets/NJU-LINK/DR3-Eval)，可直接下载使用。

### 🔧 环境配置

```bash
# 安装依赖
uv sync

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API 密钥（OPENROUTER_API_KEY 等）

# 验证安装
uv run python main.py --help
```

### ▶️ 运行 DR³-Agent

```bash
# 单个任务
uv run python main.py run \
    --folder data/datasets_en/001 \
    --query "Analyze the documents and generate a research report." \
    --offline

# 批量任务
uv run python main.py batch \
    --data-dir data/datasets_en \
    --context-size 128k \
    --llm-config gpt-4 \
    --offline
```

### 📊 评估

```bash
uv run python eval.py all \
    --result-base results_main/datasets_en \
    --datasets-dir data/datasets_en \
    --workers 4
```

---

## 📝 引用

如果您觉得本工作有用，请引用：

```bibtex
@article{dr3eval2026,
  title={DR3-Eval: Towards Realistic and Reproducible Deep Research Evaluation},
  author={},
  journal={arXiv preprint arXiv:xxxx.xxxxx},
  year={2026}
}
```

## 🌟 许可证

本项目采用 Apache License 2.0 许可证，详见 [LICENSE](LICENSE)。

## 🙏 致谢

本项目的 DR³-Agent 基于 [MiroMind AI](https://github.com/MiroMindAI) 的 [MiroFlow](https://github.com/MiroMindAI/miroflow) 框架构建。我们在此基础上扩展了 DR³-Eval 评测框架，包括多维度报告质量指标、基准支持和多模型对比能力。

## 📧 联系方式

如有问题，请通过 GitHub Issues 联系我们。

---

**NJU-LINK Team, Nanjing University**
