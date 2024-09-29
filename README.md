# Amharic Named Entity Recognition for EthioMart

## Project Overview

This project aims to develop an Amharic Named Entity Recognition (NER) system for the EthioMart e-commerce platform. The system will extract relevant entities such as product names, prices, and locations from messages within Ethiopian Telegram channels. This README provides an overview of the project's objectives, data collection methods, and analysis processes.

## Objectives

- **Entity Extraction**: Identify and extract entities from messages in the Amharic language.
- **Data Analysis**: Conduct exploratory data analysis (EDA) to understand trends in the e-commerce space.
- **Model Development**: Build and fine-tune a NER model for Amharic text.

## Data Collection

Data was scraped from selected Ethiopian Telegram channels that focus on e-commerce. The data includes messages related to product listings, promotions, and customer interactions. The scraped data is stored in a CSV file located at `../data/telegram_data.csv`.

## Data Cleaning

The data cleaning process involves several steps to ensure the text data is suitable for further analysis. The key function used for cleaning the message text is as follows:

### Clean Text Function

```python
import re
import string
import emoji

def clean_text(text):
    """Cleans Amharic text by removing special characters, emojis, and extra spaces."""
    if not isinstance(text, str):
        return ""
    text = emoji.replace_emoji(text, replace="")
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^\u1200-\u137F\s፡።፣፤፥፦፧፨]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace('፣', ',').replace('።', '.').replace('፡', ' ')
    text = re.sub(r'\d+', '', text)
    return text

Exploratory Data Analysis (EDA)
The EDA is structured into separate scripts to enhance modularity and reusability. The primary analysis includes visualizations that highlight patterns and trends in the data.

Key Visualizations
Distribution of Sales: Analyzes the frequency of product sales.
Promotional Effects: Examines the impact of promotions on sales.
Sales by Store Type: Compares sales performance across different store types.
Competition Effects: Evaluates how competition influences sales.
Conclusion
This project is a step towards building a comprehensive NER system for Amharic text in the e-commerce domain. The insights gained from the exploratory data analysis will guide the model development and refinement process.

pip install -r requirements.txt
