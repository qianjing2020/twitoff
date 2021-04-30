# web_app/services/basilica_service.py

import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

basilica_api_client= basilica.Connection(API_KEY)

print(type(basilica_api_client))  

if __name__ == "__main__":

    # Note that basilica methods:  embed_sentence for one sentence, and embed_sentences for a list of sentences
    
    print("---------")
    sentence = "Hello world!"
    sent_embeddings = basilica_api_client.embed_sentence(
        sentence)  # return a generator
    print(list(sent_embeddings)) # show as list

    print("---------")
    sentences = ["Hello world!", "How are you?", "I spotted a yellow flower!"]
    print(sentences)
    # it is more efficient to make a single request for all sentences...
    embeddings = list(basilica_api_client.embed_sentences(sentences))
    print("EMBEDDINGS...")
    print(embeddings)  # a list of list [[0.8556405305862427, ...], ...]
    print(type(embeddings)) # class 'generator'
    print(len(embeddings))
    print(len(embeddings[0]), len(embeddings[1]), len(embeddings[2]))
