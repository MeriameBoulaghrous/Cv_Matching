import streamlit as st
import uuid
import logging

from qdrant_utils import (
    initialize_qdrant_client, 
    create_qdrant_collection, 
    store_embeddings_in_qdrant
)
from pdf_utils import extract_text_from_pdf
from embedding_utils import (
    initialize_embedding_model, 
    generate_embeddings
)
from info_extraction import (
    extract_information_from_cv, 
    extract_keywords_from_job_offer
)
from matching_utils import match_cv_to_job_offer

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Qdrant client and collection
qdrant_client = initialize_qdrant_client()
embedding_model = initialize_embedding_model()

collection_name = "cv_embeddings"
create_qdrant_collection(qdrant_client, collection_name, embedding_model.get_sentence_embedding_dimension())

# Streamlit app layout
st.title("CV and Job Offer Matching System")

# Section for uploading CV PDFs
st.header("Upload CVs")
uploaded_files = st.file_uploader("Upload up to 50 CV PDF files", type="pdf", accept_multiple_files=True)

cv_embeddings_list = []

if uploaded_files:
    if len(uploaded_files) > 50:
        st.error("Please upload a maximum of 50 PDF files.")
    else:
        for file_num, uploaded_file in enumerate(uploaded_files, start=1):
            st.info(f"Processing CV file {file_num}/{len(uploaded_files)}: {uploaded_file.name}")
            
            try:
                # Process the uploaded CV PDF file
                cv_text = extract_text_from_pdf(uploaded_file)
                cv_info = extract_information_from_cv(cv_text, model_name="mistral")

                st.success(f"Extracted information from {uploaded_file.name}")

                # Generate embeddings for the CV
                cv_embeddings = generate_embeddings(embedding_model, cv_info)
                cv_embeddings_list.append((cv_info, cv_embeddings))  # Store both the info and embeddings for matching later

                # Store the embeddings in Qdrant with a unique CV ID
                cv_id = str(uuid.uuid4())
                store_embeddings_in_qdrant(qdrant_client, cv_embeddings, cv_id, collection_name)

                st.success(f"CV file {uploaded_file.name} processed and stored.")
            except Exception as e:
                logger.error(f"Error processing {uploaded_file.name}: {e}")
                st.error(f"An error occurred while processing {uploaded_file.name}. Please check the logs for details.")

# Section for uploading a Job Offer PDF
st.header("Upload Job Offer")
job_offer_file = st.file_uploader("Upload a Job Offer PDF file", type="pdf", key="job_offer", accept_multiple_files=False)

if job_offer_file:
    st.info(f"Processing Job Offer file: {job_offer_file.name}")
    
    try:
        # Process the uploaded Job Offer PDF file
        job_offer_text = extract_text_from_pdf(job_offer_file)
        job_offer_keywords = extract_keywords_from_job_offer(job_offer_text, model_name="mistral")

        st.success(f"Extracted keywords from {job_offer_file.name}")

        # Generate embeddings for the job offer
        job_offer_embeddings = generate_embeddings(embedding_model, job_offer_keywords)

        # Store the embeddings in Qdrant with a unique Job Offer ID
        job_offer_id = str(uuid.uuid4())
        store_embeddings_in_qdrant(qdrant_client, job_offer_embeddings, job_offer_id, collection_name)

        st.success(f"Job Offer file {job_offer_file.name} processed and stored.")

        # Match each CV with the job offer
        best_match_percentage = 0
        best_match_cv_info = None

        st.header("Matching Results")
        for cv_info, cv_embeddings in cv_embeddings_list:
            # Match CV to the job offer using the combined embeddings approach
            match_percentage = match_cv_to_job_offer(cv_embeddings, job_offer_embeddings)
            st.write(f"Match Percentage between CV and Job Offer: {match_percentage:.2f}%")

            if match_percentage > best_match_percentage:
                best_match_percentage = match_percentage
                best_match_cv_info = cv_info

        # Display only the Contact Info and Summary of the best match in the Streamlit app
        if best_match_cv_info:
            st.subheader("Best Matching CV Details")
            contact_info = best_match_cv_info.get("contact_info", "Contact info not available")
            summary = best_match_cv_info.get("summary", "Summary not available")
            
            st.write("### Contact Information")
            st.write(contact_info)

            st.write("### Summary")
            st.write(summary)

            st.write(f"**Best Match Percentage:** {best_match_percentage:.2f}%")
        else:
            st.warning("No suitable CV matches found.")
    except Exception as e:
        logger.error(f"Error processing job offer file {job_offer_file.name}: {e}")
        st.error(f"An error occurred while processing {job_offer_file.name}. Please check the logs for details.")
