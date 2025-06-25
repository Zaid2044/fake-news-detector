from flask import Flask, render_template, request
from model import predict_news

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    article_text = request.form['article_text']
    prediction, prediction_class = predict_news(article_text)
    
    color = 'green' if prediction_class == 'Real' else 'red'
    
    return render_template('index.html', prediction=prediction, article_text=article_text, color=color)

if __name__ == '__main__':
    app.run(debug=True)