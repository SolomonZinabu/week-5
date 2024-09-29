import pandas as pd
import re

def clean_text(text):
    """Basic text cleaning for Amharic e-commerce data."""
    text = str(text).lower()  # Lowercase
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def preprocess_data(df):
    """Preprocess the dataframe by cleaning the message text."""
    df['Cleaned_Message'] = df['Message'].apply(clean_text)
    return df
