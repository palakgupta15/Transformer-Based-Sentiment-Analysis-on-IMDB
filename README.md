# SentimentScope: IMDB Sentiment Analysis with Transformers

SentimentScope is a sentiment classification project that uses a custom Transformer-based neural network to classify IMDB movie reviews as **positive or negative**. 

I developed this project after completing my **AI Programming with Python Nanodegree from Udacity**, as an application of concepts in natural language processing, tokenization, attention mechanisms, and Transformer architectures.

## Project Overview

The project uses the IMDB Large Movie Review Dataset, which contains labelled positive and negative movie reviews.

The notebook covers the complete workflow:

* Loading and exploring the IMDB movie review dataset
* Analysing review and label distributions
* Tokenizing text using the BERT tokenizer
* Preparing data using PyTorch datasets and data loaders
* Implementing self-attention and multi-head attention
* Building Transformer blocks
* Creating a custom Transformer-based sentiment classifier
* Training and evaluating the model
* Running sentiment predictions on new movie reviews

## Model Architecture

The sentiment classifier is implemented in PyTorch and contains the core components of a Transformer architecture:

* Token embeddings
* Positional embeddings
* Self-attention
* Multi-head attention
* Feed-forward neural networks
* Layer normalization
* Transformer blocks
* Binary classification head

Rather than directly fine-tuning a pre-trained BERT model, the project uses the **BERT tokenizer** for text tokenization while implementing the Transformer model architecture in PyTorch.

## Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

## Dataset

The project uses the **Large Movie Review Dataset (IMDB)** from Stanford, consisting of movie reviews labelled by sentiment.

The dataset is not included directly in this repository due to its size. A download script is provided to retrieve and extract the dataset.

Run:

```bash
python download_imdb.py
```

## Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd SentimentScope
```

### 2. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the IMDB dataset

```bash
python download_imdb.py
```

### 4. Open the Jupyter Notebook

```bash
jupyter notebook SentimentScope_IMDB_Transformer.ipynb
```

Run the notebook cells in order to explore the dataset, build the model, and train or evaluate the sentiment classifier.

## Repository Structure

```text
SentimentScope/
│
├── SentimentScope_IMDB_Transformer.ipynb
├── README.md
├── requirements.txt
└── download_imdb.py
```

## Training

Training a Transformer model can be computationally intensive. A **GPU-enabled environment is recommended** for full model training, although the notebook and model implementation can also be explored in a CPU environment.

## Key Concepts Demonstrated

This project demonstrates practical implementation of:

* Natural Language Processing (NLP)
* Text tokenization
* Word and positional embeddings
* Self-attention
* Multi-head attention
* Transformer architecture
* PyTorch model development
* Sentiment classification
* Model training and evaluation