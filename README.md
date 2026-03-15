# AI Sales Assistant using Salesforce and Python

## Overview

This project implements an **AI-powered Sales Assistant** that analyzes CRM sales data and provides intelligent insights for sales representatives.

The assistant retrieves account and opportunity information, analyzes the sales pipeline, and generates actionable recommendations such as opportunity summaries, risk levels, follow-up emails, and proposal outlines.

The system is built using **Python, Salesforce CRM APIs, and an AI language model (Ollama)**.

---

# Project Workflow

1. The user asks a question about a customer or opportunity.
2. The system retrieves account and opportunity data.
3. The assistant identifies the relevant account mentioned in the prompt.
4. Account and opportunity data are added to an AI prompt.
5. The AI model analyzes the data.
6. The system returns insights and recommendations for the sales representative.

---


---

# File Descriptions

## main.py

This is the **main entry point of the application**.

Responsibilities:

- Accepts user input
- Retrieves relevant account data
- Builds the AI prompt
- Sends the prompt to the AI model
- Displays the AI-generated response

---

## data_loader.py

This module loads sales datasets used by the AI assistant.

It reads CSV files such as:

- Accounts
- Sales Pipeline
- Products
- Sales Teams

The data is loaded using **Pandas** for structured analysis.

---

## retrieval.py

This module is responsible for **finding relevant accounts and retrieving context data**.

Functions include:

- Identifying which account the user is referring to
- Extracting account details
- Extracting related opportunity information

This data is later passed to the AI model.

---

## prompt_builder.py

This module constructs the **AI prompt** sent to the language model.

The prompt contains:

- Account details
- Opportunity details

The AI is instructed to generate:

1. Opportunity Summary  
2. Risk Level  
3. Recommended Next Best Action  
4. Follow-up Email  
5. Proposal Outline

---

## ollama_client.py

This module connects to the **Ollama AI model**.

It sends the generated prompt to the AI model and receives the response.

The model used in this project is:

