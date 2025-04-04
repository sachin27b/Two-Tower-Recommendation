import streamlit as st
import pandas as pd
from scripts import get_embedding, get_tower_embedding, index_search
import sqlite3

st.set_page_config(layout="wide")

st.title("Ecommerce Website")

query = st.text_input("Search for a product:")

query_tower_url = "http://localhost:5001/invocations"
embedding_model_url = "http://localhost:5002/invocations"

conn = sqlite3.connect("assets/amazon_database.db")

if st.button("Search", type="primary") or query:
    if query: 
        with st.spinner("Searching products..."):
            q_embedding = get_embedding.get_embedding_from_model(query, embedding_model_url)
            q_tower_embedding = get_tower_embedding.get_query_tower_embedding(q_embedding, query_tower_url)
            recommendations = index_search.retrieve_products(q_tower_embedding, conn, index_path='assets/product_tower_embedding.index', top_k=10)
        
        if recommendations.empty:
            st.warning("No products found. Try a different search term.")
        else:
            st.subheader(f"Found {len(recommendations)} matching products")
            
            # Create a container for each product with better styling
            for i, row in recommendations.iterrows():
                with st.container():
                    col1, col2 = st.columns([1, 3])
                    
                    with col1:
                        st.markdown(':tada:')
                    
                    with col2:
                        st.markdown(f"### {row['product_title']}")
                        st.markdown(f"**Brand**: {row['product_brand']}")
                        
                        
                    with st.expander("See full details"):
                        st.markdown(f"**Complete Description**:\n{row['product_description']}")
                        
                        # Display all other columns that might be in the dataframe
                        for col in row.index:
                            if col not in ['product_title', 'product_description', 'product_brand']:
                                st.markdown(f"**{col}**: {row[col]}")
                    
                    st.divider()  # Add a divider between products

else:
    st.info("Enter a search term and click 'Search' to find products.")

# Add a footer
st.markdown("---")
st.markdown("© 2025 Ecommerce Search Demo")