# Multi-Agent Operations Automation System

## Overview
This project implements a multi-agent collaborative system designed to automate content operations workflows. It demonstrates a modular pipeline architecture where multiple agents coordinate to complete end-to-end tasks including planning, information processing, content generation, optimization, and final output.

## Architecture
The system is composed of the following core agents:

- Planner Agent: Generates structured task plans based on input topics
- Research Agent: Extracts and organizes relevant information
- Content Agent: Produces initial content drafts
- Optimization Agent: Refines and improves generated content
- Publisher Agent: Outputs final results

These agents are orchestrated in a sequential pipeline, enabling multi-step reasoning and task decomposition.

## Workflow
1. Input topic is provided to the system
2. Planner Agent generates a structured plan
3. Research Agent gathers and summarizes key information
4. Content Agent generates initial content
5. Optimization Agent refines the output
6. Publisher Agent produces the final result

## Features
- Modular multi-agent design
- Pipeline-based orchestration
- Extensible architecture for additional agents
- Support for batch task execution
- LLM abstraction layer for flexible model integration

## Project Structure
##  运行方式

```bash
python main.py
