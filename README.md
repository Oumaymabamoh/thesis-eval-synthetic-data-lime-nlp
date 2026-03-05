# IU INTERNATIONAL UNIVERSITY OF APPLIED SCIENCES

# Thesis: Evaluating the Influence of Synthetic Data Distribution and LIME's Parameters in the Explanation Fidelity in NLP Sentiment Analysis.

This repository contains the official implementation, data pipelines, and experimental results for my thesis conducted at IU university Germany.

# Abstract
As Large Language Models (LLMs) increasingly serve as engines for synthetic data generation, understanding the downstream effects on model interpretability is critical. This project investigates the influence of synthetic NLP data on the explanation fidelity of sentiment analysis models using LIME (Local Interpretable Model-agnostic Explanations). Specifically, we evaluate the relationship between data synthesis and explanation stability by training a sentiment classifier exclusively on a synthetic corpus under predefined hyperparametrs. Our findings offer insights into whether XAI methods remain reliable when the underlying training logic is derived from machine-generated rather than human-generated language. 

# Dataset overview
The dataste used in this study was sourced from Check out [huggingface](https://huggingface.co/datasets/InfinitodeLTD/CRSD/tree/main).  and treated with full compliance with the  and research paper ethics. 
# experimental design 
The flowchart below shows the exprimental workflow of this study.
<img width="2798" height="939" alt="workflow_diagram" src="https://github.com/user-attachments/assets/7c59fc66-6a05-4df1-96dd-8dec4948ad33" />

# Getting Started
```bash
pip install -r requirements.txt 
