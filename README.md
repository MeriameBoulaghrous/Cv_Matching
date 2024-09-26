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

- *Python 3.x*: Ensure Python is installed on your system.
- *Virtual Environment*: Python's venv module is required for creating a virtual environment.
- *Docker*: Necessary for running the Qdrant vector database.
- *Ollama Mistral 7B Model*: Used for processing and creating embeddings.
- *Code Editor*: Visual Studio Code or any preferred IDE is recommended.

### Installation Steps

#### 1. Create a Virtual Environment

   ```bash
   python3 -m venv your_environment
   ```
   Replace your_environment with your desired environment name.

#### 2. Activate the Virtual Environment

   Linux/macOS:

   ```bash
   source your_environment/bin/activate
   ```

   Windows:

   ```bash
   your_environment\Scripts\activate
   ```

#### 3. Install Dependencies

   Ensure all dependencies are installed by running:
  
   ```bash
   pip install -r requirements.txt
   ```
   This command installs all necessary Python libraries listed in the requirements.txt file.



#### 4. Download the Ollama Mistral 7B Model
  
  Follow the installation instructions on the Ollama website to install Ollama and download the Mistral 7B model.
   ```bash
   ollama pull mistral
   ```

#### 5. Setup of the Qdrant Vector Database
  
  If Docker is not installed, refer to the Docker Install Guide. Once Docker is running, execute:
   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

## Executing the Program

  When the machine is turned off, the Qdrant service running in Docker stops,
  herefore, when you open a new session, you'll need to restart the Qdrant service by executing the following command:
 ```bash
   docker start qdrant
   ```

### Running the code 
   ```bash
   python main.py
   ```


### Running the Streamlit Application


1. Open the Streamlit application by running the following command:

   ```bash
   streamlit run app.py
   ```

2. The application will open in your default web browser.

3. You can access the application by entering the URL provided in the terminal.



## Author

[MERIAME BOULAGHROUS](https://github.com/MeriameBoulaghrous)
[boulaghrous.meriame@gmail.com]
