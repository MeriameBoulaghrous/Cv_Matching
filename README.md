# AI-Powered CV and Job Offer Matching System

## Description

The traditional approach to matching candidates with job offers is labor-intensive, requiring recruiters to manually review and compare numerous CVs against job requirements. This can lead to inefficiencies and human biases, especially when faced with diverse CV formats and a large volume of applications. The proposed solution is an AI-powered system that automates this process by extracting key information from CVs and job descriptions, generating embeddings, and using cosine similarity to efficiently and accurately match candidates to jobs. This system aims to reduce bias, save time, and improve the overall fairness and accuracy of the recruitment process.

The AI-Powered CV and Job Offer Matching System utilizes Natural Language Processing (NLP) to extract key data and match candidates to jobs by comparing embeddings. It features a Streamlit user interface and uses Qdrant for managing vector embeddings.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Executing the Program](#executing-the-program)
3. [Author](#author)

## Getting Started

### Prerequisites

- *Python 3.x* installed on your system.
- *Virtual Environment* package (venv).
- *Docker* installed and running.
- *Ollama Mistral 7B model* installed.
- *Qdrant* vector database.

### Installation

1. *Create a Virtual Environment*

   Open your terminal and run:

   ```bash
   python3 -m venv your_environment
