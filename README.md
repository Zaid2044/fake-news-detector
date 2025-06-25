# Fake News Detection System

A web-based application that uses a pre-trained BERT model to analyze and classify news articles as real or fake. This project serves as a comprehensive demonstration of a full-stack machine learning pipeline, from data input on a web interface to model inference on the backend.

---

### Core Features

- **Interactive Web UI:** A clean, modern frontend built with Flask and styled with CSS allows users to easily paste and submit news articles.
- **Real-time AI Inference:** Utilizes the Hugging Face `transformers` library to load a pre-trained `bert-base-uncased` model for sequence classification.
- **Dynamic Feedback:** The UI provides instant, color-coded feedback based on the model's prediction ("Real" or "Fake").
- **Production-Ready:** Includes a `Procfile` and `gunicorn` for seamless deployment to cloud platforms like Heroku or Render.

---

### Tech Stack

- **Backend:** Flask, Gunicorn
- **Machine Learning:** PyTorch, Hugging Face Transformers, Scikit-learn
- **NLP Toolkit:** NLTK
- **Frontend:** HTML, CSS
- **Deployment:** Procfile for Heroku/Render

---

### How It Works

1. The user submits article text through the Flask web interface.
2. The `/predict` route receives the text.
3. The text is passed to the `predict_news` function in the `model` module.
4. The BERT tokenizer converts the text into a format suitable for the model.
5. The pre-trained BERT model performs inference on the tokenized input.
6. The model's output (logits) is processed to determine a classification.
7. The result is passed back to the Flask template and displayed to the user with dynamic styling.

---

### Setup and Usage

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd fake-news-detector
   ```

---

1. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application locally:
    ```bash
    python app.py
    ```

The application will be available at http://127.0.0.1:5000.

**Note:** This project uses a pre-trained, non-fine-tuned BERT model. Its predictions are for demonstration of the pipeline and not guaranteed to be accurate. The next logical step would be to fine-tune the model on a labeled dataset like LIAR.