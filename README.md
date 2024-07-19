# Evaluating the Effectiveness of TF-IDF and Word Embedding Models for Predicting Plot Similarity

## Overview

This repository contains the code and datasets used for the research paper **"Evaluating the Effectiveness of TF-IDF and Word Embedding Models with Cosine Similarity to Predict Plot Similarity Between Books and Films"**.

## Abstract

The paper explores novel methods to engage modern audiences with books by predicting their relevance from movies. Using the CMU Movie Summary Corpus and the CMU Book Summary Corpus, we developed a baseline system utilizing Term Frequency-Inverse Document Frequency (TF-IDF) and Cosine similarity. We then enhanced this system by incorporating stricter pre-processing, Jaccard scoring, and word embeddings using Word2Vec and DistilBERT. Our findings indicate that DistilBERT combined with Cosine Similarity significantly outperforms other models in detecting narrative similarities.

## Repository Contents

- CMU Movie Summary Corpus and CMU Book Summary Corpus.
- **/sys.ipynb**: Jupyter notebook used for data preprocessing, model training, and evaluation.
- **/main.py**: Source code implementing TF-IDF, Word2Vec, and DistilBERT models.
- Research paper via pdf.
