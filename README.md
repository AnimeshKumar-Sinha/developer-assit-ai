<p align="center">
  <img src="https://github.com/user-attachments/assets/your-org-or-project-logo.png" width="318px" alt="Developer-Assist AI logo" />
</p>

<p align="center">
  <a href="https://app.developer-assist.ai" rel="dofollow">App</a> | 
  <a href="https://docs.developer-assist.ai" rel="dofollow">Documentation</a> | 
  <a href="https://docs.developer-assist.ai/open-source" rel="dofollow">API Reference</a>
</p>

<p align="center">
  <a href="https://github.com/AnimeshKumar-Sinha/developer-assit-ai/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/AnimeshKumar-Sinha/developer-assit-ai" alt="License">
  </a>
  <a href="https://github.com/AnimeshKumar-Sinha/developer-assit-ai/stargazers">
    <img src="https://img.shields.io/github/stars/AnimeshKumar-Sinha/developer-assit-ai" alt="Stars">
  </a>
</p>

---

# 🤖 Developer-Assist: AI Agents for Your Codebase

Developer-Assist is an open-source platform that creates AI agents tailored to your codebase. It enables smart code analysis, debugging, testing, and feature planning through a knowledge graph built from your code.

---

## 📚 Table of Contents
- [⚡ Why Developer-Assist?](#why-developer-assist)
- [🤖 Available Agents](#available-agents)
- [🛠️ Tooling System](#tooling-system)
- [🚀 Getting Started](#getting-started)
- [💡 Use Cases](#use-cases)
- [🧠 Custom Agents](#custom-agents)
- [🔐 API Access](#api-access)
- [🎨 Customize Developer-Assist](#customize-developer-assist)
- [🤝 Contributing](#contributing)
- [📜 License](#license)

---

## ⚡ Why Developer-Assist?

- 💡 **Context-Aware AI Agents**: Specialized in your codebase, not generic.
- 🧠 **Graph-Powered**: Deep code understanding via knowledge graph.
- 🧪 **End-to-End**: Supports planning, testing, debugging, and code generation.
- 🛠️ **Integrated Workflow**: Designed to work inside VSCode, Slack, and CI/CD pipelines.

---

## 🤖 Available Agents

- **Debug Agent** – Diagnoses errors and suggests fixes.
- **Code Q&A Agent** – Explains architecture, functions, and flows.
- **Change Impact Agent** – Evaluates PRs, finds affected APIs.
- **Test Generation Agent** – Creates unit and integration test plans.
- **LLD Agent** – Produces low-level designs from feature requirements.
- **Code Gen Agent** – Writes, refactors, and optimizes code.

---

## 🛠️ Tooling System

Agents use these tools:

- `get_code_from_node_name`
- `ask_graph_questions`
- `change_detection`
- `get_code_structure`
- `code_graph_visualization`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10.x
- Docker
- Git

### Steps

```bash
git clone https://github.com/AnimeshKumar-Sinha/developer-assit-ai.git
cd developer-assit-ai
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x start.sh
./start.sh