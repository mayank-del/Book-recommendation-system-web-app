
from fastapi import FastAPI
from pyngrok import ngrok
import pickle

with open('popular.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = FastAPI()

@app.post("/predict/")
async def predict(data: dict):
    # Perform any necessary data preprocessing on the input data
    # Make predictions using your model
    predictions = model.predict(data)
    return {"predictions": predictions}

#public_url = ngrok.connect(port='8000')
#print('FastAPI app is live at:', public_url)

