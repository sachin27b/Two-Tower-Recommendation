# Two-Tower Model for Product Search

## Overview
This repository implements a two-tower model for product search using contrastive loss. The model consists of a **query tower** and a **product tower**, trained to generate embeddings that can be efficiently searched using FAISS.

## Dataset
The dataset used for training is from [Amazon Science - ESCI Data](https://github.com/amazon-science/esci-data).

## Embeddings
The embeddings are generated using [Alibaba-NLP/gte-multilingual-base](https://huggingface.co/Alibaba-NLP/gte-multilingual-base).

Please refer [embeddings.ipynb](https://github.com/sachin27b/Two-Tower-Recommendation/blob/master/notebook/embeddings.ipynb) for more details.

## Model Architecture
- The **query tower** and **product tower** are trained using contrastive loss to map queries and products into a shared embedding space.
- After training, the **product tower embeddings** are indexed using FAISS for efficient similarity search.

Please refere the notebook [training2.ipynb](https://github.com/sachin27b/Two-Tower-Recommendation/blob/master/notebook/training2.ipynb) for more details.

## Workflow of user queries
1. **Embed query** using the embedding model →
2. **Pass through query tower** →
3. **Query tower output** →
4. **FAISS search** using indexed product embeddings →
5. **Retrieve ranked product indexes** →
6. **Return recommended products**

## Model Logging
All models are logged to mlflow and served using mlfow model serving endpoints. Please nefer the notebook [training2.ipynb](https://github.com/sachin27b/Two-Tower-Recommendation/blob/master/notebook/training2.ipynb) for more details.

## Installation & Setup
```sh
pip install -r requirements.txt
```
Train models, log to mlflow, register models and serve. Save the FAISS index to assets.
```sh
# Start mlflow server at port 5000 by default
mlflow ui
```
```sh
# in another terminal
export MLFLOW_TRACKING_URI=http://localhost:5000
mlflow models serve -m 'runs:/<run_id>/Query Tower' -p 5001
```
```sh
# in another terminal
export MLFLOW_TRACKING_URI=http://localhost:5000
mlflow models serve -m 'runs:/<run_id>/Embedding model' -p 5002
```

Now create a SQLite DB for product-Query details so that recommended products can be queried in real time and save DB in assets.

## Usage
```sh
streamlit run app.py
````


