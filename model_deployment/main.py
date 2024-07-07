# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model
with open("artifacts/model/logreg_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Define the input data model
class ModelInput(BaseModel):
    Temperature: float
    Oxygen: float
    Humidity: float

# Define the prediction endpoint
@app.post("/predict")
def predict(data: ModelInput):
    # Convert input data to numpy array
    input_data = np.array([[data.Temperature, data.Oxygen, data.Humidity]])
    # Make prediction
    prediction = model.predict(input_data)
    # Return the result
    return {"prediction": int(prediction[0])}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
