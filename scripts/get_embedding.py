from sentence_transformers import SentenceTransformer
import torch
from scripts import get_tower_embedding
import requests

def get_embedding_from_model(query,embedding_url):
    
    data = {"inputs": [query],
        }

    response = requests.post(embedding_url, json=data)
    return response.json()['predictions']

