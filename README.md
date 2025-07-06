<h1 align="center">📰 Fake News Detector</h1>
<p align="center">
  A machine learning-powered classifier that detects fake news articles with high accuracy using NLP and Scikit-learn pipelines.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLP-9C27B0?style=flat"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/TfidfVectorizer-4CAF50?style=flat"/>
</p>

---

## 🧠 Overview

**Fake News Detector** is a binary text classification system trained to differentiate between real and fake news articles. It uses NLP preprocessing and Scikit-learn pipelines to clean, vectorize, and classify news headlines and content using a logistic regression model.

Built as an interactive web app using Streamlit.

---

## ✨ Features

* 🧹 Text preprocessing (cleaning, stemming, stopword removal)
* 🔤 TF-IDF Vectorization
* 🤖 Logistic Regression classifier
* 📄 Streamlit frontend for testing articles live
* 💯 Accuracy over 92% on test set

---

## 🔍 Tech Stack

* **Language:** Python 3.9+
* **Libraries:** Pandas, NumPy, Scikit-learn, NLTK
* **Frontend:** Streamlit
* **ML Model:** Logistic Regression
* **Vectorization:** TfidfVectorizer

---

## 📊 Performance

| Metric    | Value     |
| --------- | --------- |
| Accuracy  | **92.2%** |
| Precision | 93%       |
| Recall    | 91%       |
| F1-Score  | 92%       |

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

* Python 3.9+
* Git
* A terminal with internet access

### 📦 Installation

```bash
git clone https://github.com/Zaid2044/fake-news-detector.git
cd fake-news-detector
python -m venv venv
.\venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Go to: [http://localhost:8501](http://localhost:8501)
Paste a news article or headline — the app will tell you if it’s **Real** or **Fake**.

---

## 📁 File Structure

```
fake-news-detector/
├── app.py
├── model/
│   └── logistic_model.pkl
├── vectorizer/
│   └── tfidf.pkl
├── utils/
│   └── text_cleaner.py
├── requirements.txt
├── README.md
```

---

## 📈 Model Pipeline

* Clean & normalize text
* Tokenize and remove stopwords
* Convert to TF-IDF vectors
* Predict using logistic regression

---

## 🧩 Future Improvements

* Add SVM and ensemble models (Random Forest, XGBoost)
* Include news source bias detection
* Store classification history
* Deploy to Hugging Face Spaces or Streamlit Cloud

---

## 🧑‍💻 Author

**MOHAMMED ZAID AHMED**
