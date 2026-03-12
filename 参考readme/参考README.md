# T2AV-Compass: Towards Unified Evaluation for Text-to-Audio-Video Generation

[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://nju-link.github.io/T2AV-Compass/)
[![Dataset](https://img.shields.io/badge/🤗-Dataset-yellow)](https://huggingface.co/datasets/NJU-LINK/T2AV-Compass)
[![arXiv](https://img.shields.io/badge/arXiv-Paper-red)](https://arxiv.org/abs/2512.21094)

> 中文版：[README_cn.md](README_cn.md)

## 📖 Abstract

**T2AV-Compass** is a unified benchmark for evaluating **Text-to-Audio-Video (T2AV)** generation, targeting not only unimodal quality (video/audio) but also cross-modal alignment & synchronization, complex instruction following, and perceptual realism grounded in physical/common-sense constraints.

Text-to-Audio-Video (T2AV) generation aims to synthesize temporally coherent video and semantically synchronized audio from natural language, yet its evaluation remains fragmented, often relying on unimodal metrics or narrowly scoped benchmarks that fail to capture cross-modal alignment, instruction following, and perceptual realism under complex prompts.

This package includes **500 taxonomy-driven prompts** and fine-grained checklists for an **MLLM-as-a-Judge** protocol.

## 🌟 Key Features

- **Taxonomy-Driven High-Complexity Benchmark**: 500 semantically dense prompts synthesized through a hybrid pipeline of taxonomy-based curation and video inversion. It targets fine-grained audiovisual constraints—such as off-screen sound and physical causality—frequently overlooked in existing evaluations.

- **Unified Dual-Level Evaluation Framework**:
  - **Objective evaluation**: Video quality (VT, VA), Audio quality (PQ, CU), Cross-modal alignment (T-A, T-V, A-V, DeSync, LatentSync)
  - **Subjective evaluation (MLLM-as-a-Judge)**: Interpretable checklist-based assessment for **Instruction Following** and **Perceptual Realism**

- **Extensive Benchmarking**: Systematic evaluation of 11 state-of-the-art T2AV systems, including Veo-3.1, Sora-2, Kling-2.6, Wan-2.5/2.6, Seedance-1.5, PixVerse-V5.5, Ovi-1.1, JavisDiT, and composed pipelines.

## 📊 Evaluation Metrics

### Objective Metrics

| Category | Metric | Description |
|----------|--------|-------------|
| **Video Quality** | VT (Video Technological) | Low-level visual integrity via DOVER++ |
| | VA (Video Aesthetic) | High-level perceptual attributes via LAION-Aesthetic V2.5 |
| **Audio Quality** | PQ (Perceptual Quality) | Signal fidelity and acoustic realism |
| | CU (Content Usefulness) | Semantic validity and information density |
| **Cross-modal Alignment** | T-A | Text–Audio alignment via CLAP |
| | T-V | Text–Video alignment via VideoCLIP-XL-V2 |
| | A-V | Audio–Video alignment via ImageBind |
| | DS (DeSync) | Temporal synchronization error (lower is better) |
| | LS (LatentSync) | Lip-sync quality for talking-face scenarios |

### Subjective Metrics (MLLM-as-a-Judge)

**Instruction Following (IF)** - 7 dimensions, 17 sub-dimensions:
- **Attribute**: Look, Quantity
- **Dynamics**: Motion, Interaction, Transformation, Camera Motion
- **Cinematography**: Light, Frame, Color Grading
- **Aesthetics**: Style, Mood
- **Relations**: Spatial, Logical
- **World Knowledge**: Factual Knowledge
- **Sound**: Sound Effects, Speech, Music

**Realism** - 5 metrics:
- **Video**: MSS (Motion Smoothness), OIS (Object Integrity), TCS (Temporal Coherence)
- **Audio**: AAS (Acoustic Artifacts), MTC (Material-Timbre Consistency)

## 📦 Files

- `prompts_with_checklist.json`: Core benchmark data (500 prompts + checklists)

## 🧩 Data Schema

Each sample is a JSON object with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `index` | int | Sample ID (1–500) |
| `source` | str | Source tag (e.g., `LMArena`, `RealVideo`, `VidProM`, `Kling`, `Shot2Story`) |
| `subject_matter` | str | Theme/genre |
| `core_subject` | list[str] | Subject taxonomy (People/Objects/Animals/…) |
| `event_scenario` | list[str] | Scenario taxonomy (Urban/Living/Natural/Virtual/…) |
| `sound_type` | list[str] | Sound taxonomy (Ambient/Musical/Speech/…) |
| `camera_movement` | list[str] | Camera motion taxonomy (Static/Translation/Zoom/…) |
| `prompt` | str | **Integrated prompt** (visual + audio + speech) |
| `video_prompt` | str | Video-only prompt |
| `audio_prompt` | str | Non-speech audio prompt (can be empty) |
| `speech_prompt` | list[object] | Structured speech with `speaker`/`description`/`text` |
| `video` | str | Reference video path (optional) |
| `checklist_info` | object | Checklist for MLLM-as-a-Judge |

## 🧠 Model Adaptation

- **End-to-end T2AV models** (e.g., Veo, Kling): Use `prompt`
- **Two-stage / modular pipelines**:
  - Video model: `video_prompt`
  - Audio model: `audio_prompt`
  - TTS / speech: `speech_prompt`

## 🚀 Quick Start

```python
import json

with open("prompts_with_checklist.json", "r", encoding="utf-8") as f:
    data = json.load(f)

item = data[0]
print(f"Prompt: {item['prompt'][:200]}...")
print(f"Video Prompt: {item['video_prompt'][:200]}...")
print(f"Audio Prompt: {item['audio_prompt']}")
print(f"Speech Prompt: {item['speech_prompt']}")
print(f"Checklist Dimensions: {list(item['checklist_info'].keys())}")
```

## 📈 Citation

If you find this work useful, please cite:

```bibtex
@misc{cao2025t2avcompass,
  title         = {T2AV-Compass: Towards Unified Evaluation for Text-to-Audio-Video Generation},
  author        = {Cao, Zhe and Wang, Tao and Wang, Jiaming and Wang, Yanghai and Zhang, Yuanxing and Chen, Jialu and Deng, Miao and Wang, Jiahao and Guo, Yubin and Liao, Chenxi and Zhang, Yize and Zhang, Zhaoxiang and Liu, Jiaheng},
  year          = {2025},
  eprint        = {2512.21094},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url           = {https://arxiv.org/abs/2512.21094},
}
```

## 🔗 Links

- **Project Page**: [nju-link.github.io/T2AV-Compass/](https://nju-link.github.io/T2AV-Compass/)
- **arXiv Paper**: [arxiv.org/abs/2512.21094](https://arxiv.org/abs/2512.21094)
- **Dataset**: [huggingface.co/datasets/NJU-LINK/T2AV-Compass](https://huggingface.co/datasets/NJU-LINK/T2AV-Compass)

## 📧 Contact

- `zhecao@smail.nju.edu.cn`
- `liujiaheng@nju.edu.cn`

---

**NJU-LINK Team, Nanjing University** · **Kling Team, Kuaishou Technology** · **Institute of Automation, Chinese Academy of Sciences**
