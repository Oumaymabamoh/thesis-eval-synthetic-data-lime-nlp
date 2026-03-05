# IU INTERNATIONAL UNIVERSITY OF APPLIED SCIENCES

# Thesis: Evaluating the Influence of Synthetic Data Distribution and LIME's Parameters in the Explanation Fidelity in NLP Sentiment Analysis.

This repository contains the official implementation, data pipelines, and experimental results for my thesis conducted at IU university Germany.

# Abstract
This project investigates the influence of synthetic NLP data generted by LLMs distribution and LIME xai method on explination fedility in sentiment analysis. We evaluate this relahsionship by stability on a model trained only on synthetic dataset .
# Objectives
this thesis aims to evaluate LIME's stability on model trained soley on synthetic NlP dataset. Additionaly, analyzing how the noised data through perturbation techniques  affect the LIME's interpretation comparted to Model distortion itself.And how adjusting and choosing hyperparanetrs of LIME affect the overall concusion about both quality of data used and LIME.
# Dataset overview
The dataste used in this study was sourced from and treated with full compliance and research paper ethics. 
# experimental design 
The flowchart below shows the exprimental workflow to achive the stufy goals.
<img width="2798" height="939" alt="workflow_diagram" src="https://github.com/user-attachments/assets/7c59fc66-6a05-4df1-96dd-8dec4948ad33" />
# Model
The model used in this study to serve as black boxe model and classifier is DistilBERT developed by Hugging Face.
# Results 

# Getting Started
```bash
pip install -r requirements.txt 

