# EthioMart: Amharic NER System for Telegram-Based E-Commerce

## Overview

EthioMart aims to create a centralized platform that consolidates real-time data from multiple e-commerce Telegram channels in Ethiopia. The project focuses on fine-tuning large language models (LLMs) for Amharic Named Entity Recognition (NER), extracting key business entities like product names, prices, and locations from messages shared across these Telegram channels. The ultimate goal is to populate EthioMart's centralized database, making it a comprehensive e-commerce hub.

## Project Tasks

### Task 1: Data Ingestion and Preprocessing
- **Objective**: Ingest and preprocess real-time data from Ethiopian Telegram channels.
- **Steps**:
  - Scrape Telegram channels using a custom script.
  - Tokenize, normalize, and clean the text data for Amharic linguistic features.
  - Save the preprocessed data for further use.

```python
# eda_task_1.ipynb
import pandas as pd
from scripts.preprocess_data import process_telegram_data

input_file = '../data/telegram_data.csv'
output_file = '../data/cleaned_telegram_data_new.csv'

# Process and clean the data
process_telegram_data(input_file, output_file)

# Load and inspect the cleaned data
cleaned_data = pd.read_csv(output_file)
cleaned_data.head()


### Task 2: Data Labeling in CoNLL Format
- **Objective**: Label a subset of the preprocessed dataset in CoNLL format.
  Entity Types: Product (B-PRODUCT, I-PRODUCT), Location (B-LOC, I-LOC), Price (B-PRICE, I-PRICE), and O (Outside any entities).
- **Steps**:
   - Label Amharic text data with entity tags.
   - Save the labeled data in CoNLL format for model fine-tuning.