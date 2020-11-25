# web_app/services/basilica_service.py

import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

def basilica_api_client():
    connection = basilica.Connection(API_KEY)
    print(type(connection))  
    return connection


if __name__ == "__main__":

    connection = basilica_api_client()

    print("---------")
    sentence = "Hello world!"
    sent_embeddings = connection.embed_sentence(sentence) # return a generator
    print(list(sent_embeddings)) # show as list

    print("---------")
    sentences = ["Hello world!", "How are you?", "I spotted a yellow flower!"]
    print(sentences)
    # it is more efficient to make a single request for all sentences...
    embeddings = list(connection.embed_sentence(sentences)) # 
    print("EMBEDDINGS...")
    print(embeddings)  # a list of list [[0.8556405305862427, ...], ...]
    print(type(embeddings)) # class 'generator'
    print(len(embeddings))
    print(len(embeddings[0]), len(embeddings[1]), len(embeddings[2]))