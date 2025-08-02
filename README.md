# 🎬 Movie Recommendation System

This is a **Content-Based Movie Recommendation System** that suggests similar movies using only movie metadata — without needing user history or ratings.

---

## 📌 Project Overview

This system helps users discover similar content by analyzing:
- Genres
- Keywords
- Cast
- Director
- Overview (Plot)

> Example: Enter `Inception` → get back 5 most similar movies based on metadata.

---

## 🔧 Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn** (CountVectorizer, Cosine Similarity)
- **NLTK** (Stemming)
- **Jupyter Notebook**
- **TMDb 5000 Movie Dataset**

---

## 💡 Features

- Combines key text-based features into a single `tags` column
- Applies stemming for noise reduction
- Vectorizes text using CountVectorizer
- Calculates similarity using cosine similarity
- Provides top-5 movie recommendations based on similarity scores

---

## 🧠 How it Works

1. Preprocess movie metadata
2. Merge features (cast, crew, genres, keywords)
3. Stem text to normalize vocabulary
4. Convert tags into vectors using `CountVectorizer`
5. Compute similarity using `cosine_similarity`
6. Recommend top similar movies

---

## 🚀 How to Run

1. Clone this repo  
2. Open `recommendation_system.ipynb` in Jupyter  
3. Run all cells  
4. Call `recommend("Movie Name")` to get suggestions!

---

## 📂 Dataset

TMDb 5000 Movie Dataset from Kaggle  
*You must download and place it in the same directory as the notebook*

---

## 📃 License

This project is licensed under the **MIT License** — feel free to use or modify it for educational and learning purposes.

---

## 🙋‍♀️ Author

**Shreya Rao**  
Data Science Undergraduate | Python & ML Enthusiast  
[GitHub Profile](https://github.com/rao-shreya)
