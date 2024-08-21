from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Initialize FastAPI app
app = FastAPI()

# Load your pre-trained model and vectorizer from pickle files
with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf_vect = pickle.load(f)

with open("random_forest_model.pkl", "rb") as f:
    rf_classifier = pickle.load(f)

# Define a Pydantic model for the input data
class IngredientsRequest(BaseModel):
    ingredients: list[str]

# Define the prediction endpoint
@app.post("/predict/")
def predict_dish(ingredients_request: IngredientsRequest):
    # Convert the list of ingredients to a format compatible with the TF-IDF vectorizer
    ingredients_list = ingredients_request.ingredients

    # Transform the input data using the TF-IDF vectorizer
    X_input = tfidf_vect.transform([", ".join(ingredients_list)])

    # Predict the dish name using the Random Forest model
    predicted_dish = rf_classifier.predict(X_input)

    # Return the predicted dish name as a response
    return {"predicted_dish": predicted_dish[0]}

# Optional root endpoint
@app.get("/")
async def read_root():
    return {"message": "Dish Prediction API is running!"}

# Running the app with uvicorn
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)