from faiss import write_index, read_index
import pandas as pd
import numpy as np
import sqlite3


def retrieve_products(query_emb_np,conn, index_path, top_k=5):
    index = read_index(index_path)
    _, indices = index.search(np.array(query_emb_np), top_k)
    query = f"SELECT * FROM product_query WHERE id IN {tuple(indices[0].tolist())}"
    df = pd.read_sql(query, conn)
    return df[['product_title', 'product_description','product_brand']]