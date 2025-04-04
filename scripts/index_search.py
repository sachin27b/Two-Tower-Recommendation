from faiss import write_index, read_index
import pandas as pd
import numpy as np


def retrieve_products(query_emb_np,index_path, top_k=5):
    index = read_index(index_path)
    _, indices = index.search(np.array(query_emb_np), top_k)
    df = pd.read_csv('data/data.csv')
    
    return df.iloc[indices[0]][['product_title', 'product_description','product_brand']]