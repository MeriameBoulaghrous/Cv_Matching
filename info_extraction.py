import logging
import ollama

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_prompt_response(prompt, model_name):
    """
    Sends the prompt to the AI model and returns the response.
    
    Args:
        prompt (str): The prompt to be sent to the model.
        model_name (str): The name of the model to use.
        
    Returns:
        str: The extracted information or an error message.
    """
    try:
        response = ollama.generate(model=model_name, prompt=prompt)
        if isinstance(response, dict) and "response" in response:
            return response["response"]
        else:
            logger.warning(f"Unexpected response format: {response}")
            return "No text found in response or unexpected format."
    except Exception as e:
        logger.error(f"Error generating response for prompt: {prompt}, Error: {e}")
        return "Error occurred."

def extract_section_information(cv_text, section, prompt, model_name):
    """
    Extracts information for a specific section of the CV text.
    
    Args:
        cv_text (str): The full text of the CV.
        section (str): The section to extract information from.
        prompt (str): The prompt template for the section.
        model_name (str): The name of the model to use.
        
    Returns:
        str: Extracted information for the section.
    """
    logger.info(f"Extracting {section}...")
    full_prompt = f"{prompt}\n\n{cv_text}"
    return generate_prompt_response(full_prompt, model_name)

def extract_information_from_cv(cv_text, model_name="mistral"):
    """
    Extracts detailed information from a CV, such as name, contact info, work experience, education, etc.
    
    Args:
        cv_text (str): The full text of the CV.
        model_name (str): The name of the model to use.
        
    Returns:
        dict: A dictionary containing extracted information for each section.
    """
    logger.info("Starting information extraction from CV...")
    
    prompts = {
        "name": "Extract the candidate's name from the following CV text.",
        "contact_info": "Extract the candidate's contact information from the following CV text.",
        "work_experience": "Extract the work experience from the following CV text.",
        "education": "Extract the education details from the following CV text.",
        "skills": "Extract the skills listed in the following CV text.",
        "extracurricular_activities": "Extract the extracurricular activities from the following CV text.",
        "summary": "Extract the professional summary or objective statement from the following CV text."
    }

    extracted_info = {}
    for section, prompt in prompts.items():
        info = extract_section_information(cv_text, section, prompt, model_name)
        extracted_info[section] = info

    logger.info("Information extraction from CV completed.")
    return extracted_info

def extract_keywords_from_job_offer(job_offer_text, model_name="mistral"):
    """
    Extracts relevant keywords from a job offer, such as job title, qualifications, skills, responsibilities, etc.
    
    Args:
        job_offer_text (str): The full text of the job offer.
        model_name (str): The name of the model to use.
        
    Returns:
        dict: A dictionary containing extracted keywords for each section.
    """
    logger.info("Starting keyword extraction from job offer...")
    
    prompts = {
        "job_title": "Extract the job title keywords from the following job offer text.",
        "company_info": "Extract the company-related keywords from the following job offer text.",
        "responsibilities": "Extract the key responsibilities keywords from the following job offer text.",
        "qualifications": "Extract the keywords related to qualifications and skills from the following job offer text.",
        "benefits": "Extract the benefit-related keywords from the following job offer text.",
        "application_process": "Extract the keywords related to the application process from the following job offer text."
    }

    extracted_keywords = {}
    for section, prompt in prompts.items():
        keywords = extract_section_information(job_offer_text, section, prompt, model_name)
        extracted_keywords[section] = keywords

    logger.info("Keyword extraction from job offer completed.")
    return extracted_keywords
