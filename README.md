# Medical-chatbot-using-Gemini


Medical Chatbot

A context-aware medical chatbot that answers user queries based on the content of medical textbooks. Built with Flask, LangChain, Pinecone, and Google Gemini LLM. This project demonstrates retrieval-augmented generation (RAG) for knowledge-based question answering.



Features

Upload and process medical textbooks (PDF) for question answering.

Uses Hugging Face embeddings to convert text into vector representations.

Stores embeddings in Pinecone Vector Database for efficient retrieval.

Implements RAG chain to combine retrieved information with LLM responses.

Web-based interface built with HTML, CSS, and JavaScript.

Powered by Google Gemini LLM for natural language responses.

Tech Stack

Backend: Python, Flask

LLM: Google Gemini via LangChain

Vector Store: Pinecone

Embeddings: Hugging Face Transformers

Frontend: HTML, CSS, JavaScript

Environment Management: dotenv



How It Works

PDF ingestion: Load and split medical books into text chunks.

Embeddings: Convert chunks into vector representations using Hugging Face embeddings.

Vector storage: Upload embeddings to Pinecone for fast similarity search.

Retrieval: User query is matched against stored vectors to find relevant chunks.

Answer generation: Google Gemini LLM uses retrieved chunks to generate accurate responses.


