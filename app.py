from flask import Flask, render_template, request
from model import predict_news

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    article_text = request.form['article_text']
    prediction = predict_news(article_text)
    return render_template('index.html', prediction=prediction, article_text=article_text)

if __name__ == '__main__':
    app.run(debug=True)