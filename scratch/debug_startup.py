import time
print("Importing os, json, uuid, pathlib, datetime...")
import os, json, uuid, pathlib
from datetime import datetime, timedelta
print("Importing fastapi...")
from fastapi import FastAPI, HTTPException
print("Importing pydantic...")
from pydantic import BaseModel, Field
print("Importing groq...")
try:
    from groq import Groq
except ImportError:
    print("groq not found")
print("Importing core components...")
start = time.time()
from app.core.knowledge_graph import load_graph_from_csv
print(f"Knowledge Graph imported in {time.time() - start:.2f}s")
start = time.time()
from app.core.rag_pipeline import RAGPipeline
print(f"RAG Pipeline imported in {time.time() - start:.2f}s")
start = time.time()
from app.core.nlp_extractor import SymptomExtractor
print(f"NLP Extractor imported in {time.time() - start:.2f}s")
