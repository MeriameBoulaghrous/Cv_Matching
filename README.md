# Title :
AI-Powered CV and Job Offer Matching System
# Description :
The traditional approach to matching candidates with job offers is labor-intensive, requiring recruiters to manually review and compare numerous CVs against job requirements, which can lead to inefficiencies and human biases. This process becomes even more challenging when faced with diverse CV formats and a large volume of applications, making it difficult to ensure thorough evaluations. The proposed solution is to develop an AI-powered system that automates this process by extracting key information from CVs and job descriptions, generating embeddings, and using cosine similarity to efficiently and accurately match candidates to jobs. This system aims to reduce bias, save time, and improve the overall fairness and accuracy of the recruitment process.
The AI-Powered CV and Job Offer Matching System uses NLP to extract key data and match candidates to jobs by comparing embeddings. It features a Streamlit UI and Qdrant for managing.
## Table of Contents
  1. Getting started
  2. Executing program 
  3. Author


# Getting Started:
1- we first start bby creating an environment in the terminal using the command : 
python3 -m venv your_environment

then activate the Virtual Environment:

 On Linux/macOS:

source env/bin/activate

On Windows:
.\env\Scripts\activate
Dependencies : 
The requirements.txt file for the project contains all the necessary Python libraries, along with their respective versions that are compatible with each other. This ensures the project runs smoothly without version conflicts. 

After activating the environment, install the dependencies from requirements.txt by running:

pip install -r requirements.txt

To install and run the AI model used Ollama Mistral 7B model, you'll need to follow the steps in the ollama website for linux or windows or MacOS: https://ollama.com/download 
Once the ollama is installed, you can download and install the Mistral 7B model by running in the terminal:

ollama pull mistral
To set up Qdrant (a vector database optimized for storing and searching embeddings):
If you don't have Docker installed, you can follow the installation steps from the official Docker website: Docker Install Guide.
Log into Docker Hub:
Use the following command to log in to Docker Hub (or any other Docker registry):

docker login

You will be prompted to enter your Docker Hub username and password.
Once Docker is installed, you can run the Qdrant service locally with the following command:

docker run -p 6333:6333 qdrant/qdrant
If Docker is not running, you can start it with:

sudo systemctl start docker

# Executing program :
When the machine is turned off, the Qdrant service running in Docker stops,
herefore, when you open a new session, you'll need to restart the Qdrant service by executing the following command:

docker start qdrant

When you open the project folder in a code editor like VS Code, you can start the project by running the following command in the terminal:

python main.py

After that, to view the Streamlit app in your browser, execute the command:

streamlit run main.py

This will launch the Streamlit app and provide a URL in the terminal where you can access it in your web browser.

# Author:
MERIAME BOULAGHROUS
boulaghrous.meriame@gmail.com
