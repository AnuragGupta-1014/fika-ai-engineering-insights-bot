# FIKA AI Insights Bot

## Overview
LangChain + Slack bot to summarize GitHub engineering productivity via agents.

## Setup
```bash
git clone https://github.com/AnuragGupta-1014/fika-ai-engineering-insights-bot.git
cd fika-ai-engineering-insights-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
python main.py  # Or run slack_bot.py for Slack integration
```

## Architecture
![Diagram](architecture_diagram.png)

## Agents
- DataHarvester: Reads GitHub events
- DiffAnalyst: Aggregates and summarizes
- InsightNarrator: LLM-generated reports

---

Let me know if you'd like a ZIP of this project or want me to generate charts & improve the summary or Slack UI!
