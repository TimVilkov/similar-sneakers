import logging
import pandas as pd
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import CLIPProcessor, CLIPModel
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


from dowload_model import download_clip
from embeddings_to_db import embeddings_to_db


#download_clip('clip/')
local_processor = CLIPProcessor.from_pretrained('clip/', local_files_only=True)
local_model = CLIPModel.from_pretrained('clip/', local_files_only=True)
client = QdrantClient(host="db", port=6333)

app = FastAPI()

app.mount("/golden_dataset", StaticFiles(directory="golden_dataset"), name='golden_dataset')

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

class Item(BaseModel):
    text: str

    def predict(self):
        pass

class Items(BaseModel):
    objects: List[Item]

@app.get('/')
async def root():
    return {'message': 'start page'}


@app.get("/calculate_text_embeddings")
async def calculate_text_embeddings(text: str) -> List[float]:
    # Log the request
    logging.info(f"Received request: {text}")

    inputs = local_processor(text=list([text]),
                   return_tensors="pt", padding=True)
    outputs = local_model.get_text_features(**inputs).tolist()[0]
 
    return outputs

@app.get("/find_similar_ids", response_class=HTMLResponse)
async def find_similar_ids(text: str) -> List[str]:

    inputs = local_processor(text=[text],
                   return_tensors="pt", padding=True)
    text_embeddings = local_model.get_text_features(**inputs)
    hits = client.search(
        collection_name="clip_embeddins",
        query_vector=text_embeddings.tolist()[0],
        limit=3 
    )
    return [hit.payload['image_id'] for hit in hits]


@app.get("/find_similar_images", response_class=HTMLResponse)
async def find_similar_images(text: str) -> HTMLResponse:
    inputs = local_processor(text=[text],
                   return_tensors="pt", padding=True)
    text_embeddings = local_model.get_text_features(**inputs)
    image_id = client.search(
        collection_name="clip_embeddins",
        query_vector=text_embeddings.tolist()[0],
        limit=1
    )[0].payload['image_id']
    return f"""
    <html>
        <head>
            <title></title>
        </head>
        <body>
        <img src="golden_dataset/{image_id}.png">
        </body>
    </html>
    """


@app.get("/create_collection")
async def create_collection() -> List[float]:
    embeddings_to_db(client, local_model, local_processor)