
# 🎬 Movie Recommendation System (Content-Based Filtering)

This project is a **content-based movie recommendation system** that suggests movies similar to a user-selected title by analyzing the movie's content such as genres, keywords, cast, and overview.



## 🚀 Features

- Suggests similar movies based on textual content
- Uses TF-IDF vectorization and cosine similarity
- Interactive frontend built with Streamlit
- Fast and easy recommendations
- Deployed model for real-time use


## 🧠 How It Works

1. **Data Cleaning** – Processed metadata to extract relevant features
2. **Feature Extraction** – Combined genres, keywords, cast, and overview
3. **Text Vectorization** – Used `TfidfVectorizer` to convert text into vectors
4. **Similarity Computation** – Applied `cosine_similarity` to find similar movies
5. **Frontend** – Built an interactive UI using Streamlit



## 🛠️ Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn** (TF-IDF, Cosine Similarity)
- **Streamlit**
- **Pickle** (model serialization)
- **Git & GitHub**


## 📁 Project Structure


movie\_recommendation\_system/
│
├── app.py                    # Streamlit app
├── movie\_dict.pkl            # Serialized movie dictionary
├── similarity.pkl            # Serialized similarity matrix
├── movies.csv                # Dataset
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation



## ▶️ How to Run Locally

1. **Clone the repository**

git clone https://github.com/navinyadav8919/Movie_Recomendation-System.git
cd movie_recommendation_system


2. **Install dependencies**

pip install -r requirements.txt

3. **Run the app**

streamlit run app.p


## 📚 Dataset

The dataset used is from [TMDB Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata).



## 📬 Feedback

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/navinyadav-ai) or raise issues and suggestions via GitHub!



## 📌 License

This project is open-source and available under the [MIT License](LICENSE).

