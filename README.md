# Movie Recommendation System (Content-Based)

![DatabaseSchema](https://github.com/INDDRSINGH/Movie-recommendation-system/blob/main/movie%20logo.jpg)

##  Project Overview
A content-based movie recommender that suggests **5 similar movies** when a user selects one from a predefined list. This project demonstrates the entire workflow of data merging, text processing, similarity modeling, model deployment, and serving via a web interface.

##  Live Demo
Try it live on Render:  **[Movie Recommender Demo](https://movie-recommendation-system-pn9j.onrender.com/)**

##  Tools & Technologies
- **Python**  
- **Jupyter Notebook** for exploratory modeling  
- **Pandas** for data merging and preprocessing  
- **TF-IDF Vectorizer** for feature extraction  
- **Cosine Similarity** algorithm to compute similarities  
- **scikit-learn** for modeling  
- **Streamlit** (`app.py`) for building the web interface  
- **Render** for deployment  
- **Pickle** for serializing model artifacts (`vector.pkl`, `movies.pkl`)

##  Project Workflow
1. **Data Preparation**  
   - Merged multiple movie files into a single DataFrame  
   - Cleaned and consolidated textual data (title, genres, overview)  
2. **Feature Engineering**  
   - Vectorized combined text using TF-IDF  
3. **Similarity Modeling**  
   - Computed pairwise similarities using Cosine Similarity  
   - Built a lookup to retrieve top 5 similar movies  
4. **Web App Development**  
   - Created a Streamlit app (`app.py`) to serve recommendations  
   - Deployed the model and web interface on Render

## Dataset
- The dataset derives from a Kaggle movie dataset [here](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data). It comprises movie titles, genres, and descriptions used for computing textual similarity.

## Key Insights
- Content-based recommendation effectively suggests relevant movies based on text similarity.
- TF-IDF provides meaningful feature vectors, enabling efficient similarity scoring.
- An interactive, deployable app enhances portfolio impact and demonstrates real-world readiness.

## What I Learned
- End-to-end machine learning implementation: data ingestion → model → deployment
- Feature engineering for NLP using combined movie metadata
- Building lightweight web applications using Flask
- Deploying ML-powered applications with Render.com
- Serialization and reusability of Python objects via pickle



