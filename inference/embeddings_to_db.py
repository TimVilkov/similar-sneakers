import torch
import matplotlib.pyplot as plt

import os
import pandas as pd
import numpy as np

from transformers import CLIPProcessor, CLIPModel
from utils import CustomImageDataset

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


def embeddings_to_db(client, model, processor):
    dataset = CustomImageDataset('labelled_sample.csv',
                             'golden_dataset/')

    image_embeddings = model.get_image_features(**processor(images=[dataset[i] for i in range(len(dataset))], 
                                                 return_tensors="pt", 
                                                 padding=True))
    print("starting create collection")
    client.create_collection(
        collection_name="clip_embeddins",
        vectors_config=VectorParams(size=image_embeddings.shape[1], distance=Distance.COSINE),
    )

    points=[
        PointStruct(
            id=idx,
            vector=image_embeddings[idx],
            payload={"description": dataset.img_labels['prompt'].values[idx],
                    "image_id": int(dataset.img_labels['image_id'].values[idx])}
        )
        for idx in range(150)
    ]

    client.upload_points(collection_name="clip_embeddins",
                    points=points)