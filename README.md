## Movie Recommender System

[Live Server ](https://movierecommendersystem-303cb052fdba.herokuapp.com/)

### Overview

The Movie Recommender System suggests movies based on user preferences using a content-based recommendation approach. The system analyzes movie attributes to recommend similar films. It's implemented with a focus on movie genres, keywords, cast, and crew to provide accurate recommendations.

### Recommender Systems Explained

A recommender system suggests content based on user preferences. Common examples include:

- **YouTube**: Recommends similar videos related to your interest.
- **Netflix**: Suggests movies of the same genre as those you've watched.
- **Amazon**: Recommends products based on your purchase history.

**Types of Recommender Systems**:

1. **Content-Based Recommendation**:
   - Recommends items similar to those you have shown interest in based on content attributes.

2. **Collaborative Filtering**:
   - Recommends items based on preferences of users with similar tastes.

3. **Hybrid Recommender System**:
   - Combines content-based and collaborative filtering approaches for enhanced accuracy.

### Project Architecture

This project implements a content-based recommender system with the following steps:

1. **Data Collection**:
   - Gather data about items and user preferences.

2. **Feature Extraction**:
   - Identify key attributes of items for comparison.

3. **Similarity Measurement**:
   - Calculate similarity between items based on their features.

4. **Recommendation Generation**:
   - Suggest items similar to those the user has shown interest in.

### Dataset

The project uses the "TMDb 5000 Movie Dataset" from Kaggle, which contains detailed information about 5,000 movies, including attributes like movie ID, titles, cast, and crew. The dataset includes two CSV files:

- **credits.csv**: Contains cast and crew data.
- **movies.csv**: Includes movie budgets, genres, home pages, and overviews.

### Data Processing

1. **Loading Data**:
   - Load `movies.csv` and `credits.csv` into a Jupyter notebook.

2. **Merging Datasets**:
   - Combine the two datasets on the title column to integrate cast and crew information.

3. **Selecting Important Columns**:
   - Retain columns such as `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.

4. **Handling Missing Values**:
   - Drop rows with missing values.

5. **Preprocessing Columns**:
   - Convert genre and keyword strings to lists.
   - Extract the top three cast members and director's name.

6. **Creating Tags**:
   - Combine relevant features into a single "tags" column for recommendation purposes.

### Recommendation Function

1. **Generate Tags**:
   - Combine keywords and genre information into descriptive paragraphs.

2. **Text to Vectors**:
   - Use `CountVectorizer` to convert text into numerical vectors.

3. **Dimensionality Reduction**:
   - Visualize vectors in lower-dimensional space.

4. **Similarity Calculation**:
   - Use cosine similarity to find and recommend similar movies.

5. **Preprocessing with Stemming**:
   - Normalize words using stemming.

### Development Environment

1. **Set Up Environment**:
   - Create and activate a Python virtual environment.

2. **Install Dependencies**:
   - Use `requirements.txt` to list and install necessary packages.

3. **Create Streamlit App**:
   - Build the user interface with Streamlit to interact with the recommender system.

4. **Load Data and Build Interface**:
   - Load movie embeddings and similarity scores, create a movie selection interface, and fetch movie posters using the TMDb API.
