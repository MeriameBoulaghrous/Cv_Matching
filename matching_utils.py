import numpy as np
from scipy.spatial.distance import cosine

def calculate_cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors."""
    return 1 - cosine(vec1, vec2)

def match_cv_to_job_offer(cv_embeddings, job_offer_keywords_embeddings):
    """
    Match CV embeddings to job offer keywords embeddings by combining all sections and return match percentage.
    
    Args:
        cv_embeddings (dict): A dictionary with sections (e.g., 'skills', 'experience') as keys and their corresponding embeddings as values.
        job_offer_keywords_embeddings (dict): A dictionary with sections (e.g., 'qualifications', 'responsibilities') as keys and their corresponding embeddings as values.
        
    Returns:
        float: The overall match percentage between the CV and the job offer.
    """
    # Combine all CV embeddings into a single vector
    combined_cv_embeddings = np.mean([embedding for embedding in cv_embeddings.values()], axis=0)

    # Combine all job offer keywords embeddings into a single vector
    combined_job_offer_embeddings = np.mean([embedding for embedding in job_offer_keywords_embeddings.values()], axis=0)

    # Calculate cosine similarity between the combined vectors
    match_percentage = calculate_cosine_similarity(combined_cv_embeddings, combined_job_offer_embeddings) * 100

    return match_percentage

# Example usage:
# cv_embeddings = {'skills': cv_skills_embedding, 'experience': cv_experience_embedding, ...}
# job_offer_keywords_embeddings = {'qualifications': job_qualifications_embedding, 'responsibilities': job_responsibilities_embedding, ...}
# match_percentage = match_cv_to_job_offer(cv_embeddings, job_offer_keywords_embeddings)
