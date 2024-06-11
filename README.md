# Spam Shield - Phishing Detection System

## Project Overview

Spam Shield is a machine learning-based phishing detection system designed to identify spam in SMS/mail and URLs. The system is built using HTML, CSS, and JavaScript for the frontend, with Python and Flask for backend integration. It also includes a browser extension to provide easy access to the main functionalities.

## Functionalities

1. **SMS/Mail Spam Detection**
2. **URL Spam Detection**

## Datasets

- **SMS/Mail Spam Detection**: Collected from Kaggle, preprocessed, and trained using the Naive Bayes algorithm.
- **URL Spam Detection**: Collected from Kaggle, upgraded using the NLTK framework, and trained using Decision Tree, Random Forest, and Multilayer Perceptron algorithms.

## Models

- **SMS/Mail Spam Detection**: 
  - Algorithm: Multinomial Naive Bayes (best accuracy)
  - Exported Models: `vectorizer.pkl`, `model.pkl`
- **URL Spam Detection**:
  - Algorithms: Decision Tree, Random Forest, Multilayer Perceptron
  - Framework: TensorFlow
  - Exported Model: `model2.pkl`

## Project Structure

### Main Application
- **Main File**: `main.py`
- **Frontend Files**:
  - HTML: `html-spamshield.html`
  - CSS: `css-spamshield.css`
- **Backend Files**:
  - API for URL Detection: `API.py`
  - URL Feature Extraction: `URL_features.py`, `Feature_extract.py`

### Browser Extension
- **Frontend Files**:
  - HTML: `html-popup.html`
  - CSS: `css-styles.css`
  - JavaScript: `js-popup.js`
- **Manifest File**: `manifest.json`

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-repo/spam-shield.git](https://github.com/Janani-m17/SPAM-SHIELD.git)
   cd spam-shield
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**
   ```bash
   python main.py
   ```

4. **Open the Browser Extension**
   - Load the extension in your browser via the developer mode.
   - Select the folder containing `html-popup.html`, `css-styles.css`, `js-popup.js`, and `manifest.json`.

## Usage

1. **SMS/Mail Spam Detection**:
   - Navigate to the website.
   - Input the SMS or mail content in the provided field.
   - Click "Check" to see if the content is spam.

2. **URL Spam Detection**:
   - Navigate to the website.
   - Input the URL in the provided field.
   - Click "Check" to see if the URL is spam.

3. **Browser Extension**:
   - Open the extension.
   - Use the same functionalities as the website for quick access.

## Contributors

https://github.com/RithikaSundaram

https://github.com/skshrinaya

https://www.github.com/swetha5157

## Contact

For any inquiries, please contact janani.mkgs@gmail.com.

---
