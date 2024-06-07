import joblib
from Feature_Extract import extract_features
import numpy as np

# This function takes the URL and returns a prediction result
def get_prediction(url, model):
    print("Loading the model...")
    # model = joblib.load(model_path)

    print("Extracting features from URL...")
    url_features = extract_features(url)
    print(url_features)

    print("Making prediction...")
    # Ensure the features are in the correct format for the model
    url_features = np.array(url_features).reshape(1, -1)
    prediction = model.predict(url_features)

    percentage = prediction[0][0] * 100
    percentage = round(percentage, 3)
    print(f"There is {percentage}% chance the URL is malicious!")

    # Assuming a threshold to classify the URL as malicious or not
    threshold = 0.5
    if prediction[0] >= threshold:
        return 'bad', percentage
    else:
        return 'good', percentage
