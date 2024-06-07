import re
from urllib.parse import urlparse
import pickle
import joblib
from flask import Flask, request, jsonify, render_template
from Feature_Extract import extract_features
from API import get_prediction
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from flask_cors import CORS


# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

app = Flask(__name__)

cors = CORS(app, resources={
    r"/*": {
        "origins": [
            "chrome-extension://hkadmgpjhifmaoojmdjhocedoniimddm",  
            "brave-extension://hkadmgpjhifmaoojmdjhocedoniimddm"  
        ]
    }
})
CORS(app)

# Load models
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model1 = pickle.load(open('model.pkl', 'rb'))

stopwords_english = set(nltk.corpus.stopwords.words('english'))

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords_english and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


@app.route('/')
def home():
    return render_template('spamshield.html')

@app.route('/predict_sms', methods=['POST'])
def predict_sms():
    data = request.json
    input_sms = data.get('input_sms')
    if input_sms:
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model1.predict(vector_input)[0]
        result_text = "Spam" if result == 1 else "It is safe to proceed"
        return jsonify({'result': result_text})
    return jsonify({'result': 'Please enter some text'})

@app.route('/predict_url', methods=['POST'])
def predict_url():
    data = request.json
    input_url = data.get('input_url')
    if input_url:
        model = joblib.load('model2.pkl')  # Path to your joblib-saved model
        result, percentage = get_prediction(input_url,  model)
        result_text = f"There is {percentage}% chance of being malicious" if result == 'bad' else f"It is safe to proceed"
        return jsonify({'result': result_text})
    return jsonify({'result': 'Please enter some text'})

if __name__ == '__main__':
    app.run(debug=True)











# from flask import Flask, request, jsonify, send_file
# from nltk.corpus import stopwords
# import string
# import nltk
# from nltk.stem.porter import PorterStemmer
# from API import get_prediction
# import pickle

# app = Flask(__name__)

# # Download NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# ps = PorterStemmer()

# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)

#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         y.append(ps.stem(i))

#     return " ".join(y)

# # Load models
# try:
#     tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
#     model1 = pickle.load(open('model.pkl', 'rb'))
# except Exception as e:
#     print(f"Error loading model or vectorizer: {e}")

# @app.route('/')
# def index():
#     return send_file('spamshield.html')

# @app.route('/predict_sms', methods=['POST'])
# def predict_sms():
#     data = request.json
#     input_sms = data['input_sms']
#     transformed_sms = transform_text(input_sms)
#     vector_input = tfidf.transform([transformed_sms])
#     result = model1.predict(vector_input)[0]
#     response = {"result": "Spam" if result == 1 else "It is safe to proceed"}
#     return jsonify(response)

# @app.route('/predict_url', methods=['POST'])
# def predict_url():
#     data = request.json
#     input_url = data['input_url']
#     model_path = 'model2.pkl'  # Path to your joblib-saved model
#     result, percentage = get_prediction(input_url, model_path)
#     response = {"result": f"Spam - There is {percentage}% chance of being malicious" if result == 'bad' else f"It is safe to proceed - There is {percentage}% chance of being malicious"}
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)
