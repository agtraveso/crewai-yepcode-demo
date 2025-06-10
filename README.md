![YepCode MCP Server Preview](/readme-assets/cover.png)

# YepCode MCP + crewAI: Asteroid Impact Demo

This repository is a sample project demonstrating how to integrate [YepCode MCP](https://github.com/yepcode/mcp-server-js) with [crewAI](https://crewai.com) to build collaborative, multi-agent AI workflows. It shows how agents can work together to solve real-world problems using external tools and APIs.

## 🚀 What's Inside?

This example simulates a scenario where AI agents collaborate to assess the impact of an asteroid hitting Earth:

- **Asteroid Data Scientist**: Calculates the effects of an asteroid impact using user-provided parameters, leveraging YepCode MCP for scientific computation.
- **Impact Reporter**: Writes a dramatic, informative report about the potential effects of the asteroid impact, making the science accessible and engaging.

## 🛠️ Tech Stack

- **crewAI**: A framework for building and orchestrating multi-agent AI systems.
- **YepCode MCP**: A platform for running code and automations in the cloud, used here to perform complex calculations as part of the agent workflow.

## 📝 How It Works

1. **User provides asteroid parameters** (diameter, speed, impact angle).
2. The **Asteroid Data Scientist** agent calls a YepCode MCP process to calculate the impact energy and consequences.
3. The **Impact Reporter** agent receives the results and generates a human-friendly, dramatic report.

All agent roles and goals are defined in [`src/crewai_yepcode_demo/config/agents.yaml`](src/crewai_yepcode_demo/config/agents.yaml).

## ⚡ Quickstart

### Prerequisites

- YepCode API token
  - Sign up to [YepCode Cloud](https://cloud.yepcode.io) (it's free!)
  - Visit `Settings` > `API credentials` to create a new API token.
- Python >=3.10, <3.13
- [UV](https://docs.astral.sh/uv/) for dependency management

### Installation

It is recommended to use a Python virtual environment to keep dependencies isolated:

```bash
python3 -m venv .venv
source .venv/bin/activate
```


```bash
uv tool install crewai
crewai install
```

### Configuration

- Copy `.env.example` to `.env` in the project root and fill in your credentials:
  ```bash
  cp .env.example .env
  ```
- Add your `OPENAI_API_KEY` and `YEPCODE_API_TOKEN` to the `.env` file.
- (Optional) Configure agents and tasks in the `src/crewai_yepcode_demo/config/` directory.

### Running the Demo

From the project root, run:

```bash
crewai run
```

This will execute the workflow, and generate a `asteroid_impact_report.md` file with the results of the asteroid impact scenario.

## 🧩 Customization
- **Agents**: Edit [`agents.yaml`](src/crewai_yepcode_demo/config/agents.yaml) to change agent roles or add new ones.
- **Tasks**: Edit [`tasks.yaml`](src/crewai_yepcode_demo/config/tasks.yaml) to define new workflows.
- **Logic**: Modify [`crew.py`](src/crewai_yepcode_demo/crew.py) for advanced logic or tool integration.

## 📚 Learn More
- [crewAI Documentation](https://docs.crewai.com)
- [YepCode Documentation](https://docs.yepcode.io)

## 💬 Support
- [crewAI GitHub](https://github.com/joaomdmoura/crewai)
- [YepCode Community](https://community.yepcode.io)

---

*This repository is a companion for an upcoming Medium post. Stay tuned for the article link!*
