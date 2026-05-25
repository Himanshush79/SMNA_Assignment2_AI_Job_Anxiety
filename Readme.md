# SMNA Assignment 2: AI Job Replacement Anxiety on Reddit

## Project Title

Mapping AI Job Replacement Anxiety on Reddit: A Social Media and Network Analysis of Career Concerns, Sentiment, Topics, and Influential Discussion Communities

## Team Members

- Himanshu Sahu — s4129901
- Ayush Patel — s4130673

## Repository

https://github.com/Himanshush79/SMNA_Assignment2_AI_Job_Anxiety

## Project Overview

This project investigates how Reddit users discuss AI job replacement, career anxiety, and reskilling. The project uses social media and network analysis methods to analyse Reddit posts and comments from career, jobs, technology, and programming-related communities.

The analysis combines:

- text preprocessing
- unigram and bigram analysis
- VADER sentiment analysis
- LDA topic modelling
- Reddit reply network construction
- centrality analysis
- Louvain community detection

## Research Question

How do Reddit users discuss AI job replacement, career anxiety, and reskilling, and which users or communities appear most influential in shaping these discussions?

## Dataset

The full collected Reddit dataset contained 23,525 records from 343 Reddit posts and 14,759 unique authors.

A representative sample dataset is included for submission because the full raw dataset and analysed full dataset were too large for normal GitHub upload limits.

The dataset was collected from public Reddit JSON endpoints. No private credentials, API keys, passwords, or access tokens are included.

## Repository Structure


SMNA_Assignment2_AI_Job_Anxiety/
│
├── README.md
├── requirements.txt
├── .gitignore
├── data/
├── notebooks/
├── src/
├── figures/
├── management/
├── report/
└── presentation/

## Important Files

File/Folder	Purpose
notebooks/ai_job_anxiety_analysis.ipynb	Main notebook for data cleaning, NLP analysis, sentiment analysis, topic modelling, and network analysis
src/collect_reddit_public_json.py	Script used to collect public Reddit data
src/collect_reddit_data.py	Alternative Reddit/PRAW collection script
figures/	Generated report figures
management/team_plan.md	Teamwork and project management evidence
report/	Final report files
requirements.txt	Python package requirements

## How to Run

Create and activate a Python virtual environment.
python -m venv .venv
.venv\Scripts\Activate
Install required packages.
pip install -r requirements.txt
Open the notebook.
notebooks/ai_job_anxiety_analysis.ipynb
Run the notebook cells in order.
Required Python Packages

The required packages are listed in requirements.txt.

## Main packages include:

pandas
numpy
matplotlib
nltk
vaderSentiment
scikit-learn
networkx
python-louvain
requests
jupyter
Notes

The full raw Reddit dataset and analysed full dataset were retained locally because their file sizes exceeded normal GitHub limits. The repository contains code, notebook outputs, figures, and representative data files sufficient to understand the workflow.

No private API keys, passwords, tokens, or credentials are included.