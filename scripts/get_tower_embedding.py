import requests

def get_query_tower_embedding(query, url):
    
    data = {"inputs": query}

    return requests.post(url, json=data).json()['predictions']