# import re
# import pandas as pd
# import spacy  # Ensure to use a custom tokenizer for Amharic if available
# from sklearn.model_selection import train_test_split

# # Load Amharic NLP model (replace 'xx' with Amharic model if available)
# try:
#     nlp = spacy.load("xx_ent_wiki_sm")
# except:
#     nlp = None  # Add custom tokenizer or fallback here

# def preprocess_amharic_text(text):
#     """
#     Cleans and tokenizes Amharic text.
#     Removes irrelevant characters, normalizes text, and tokenizes.
#     """
#     # Normalize Amharic text
#     text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with one
#     text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation

#     # Tokenize
#     if nlp:
#         doc = nlp(text)
#         tokens = [token.text for token in doc]
#     else:
#         tokens = text.split()  # Fallback basic tokenization

#     return tokens

# def process_telegram_data(input_file, output_file):
#     """
#     Reads raw scraped Telegram data, preprocesses it, and saves the cleaned version.
#     """
#     # Load the scraped data (assuming a CSV format)
#     df = pd.read_csv(input_file)

#     # Clean and tokenize each message
#     df['cleaned_message'] = df['Message'].apply(preprocess_amharic_text)

#     # Save the cleaned and tokenized data for labeling
#     df.to_csv(output_file, index=False)

# if __name__ == "__main__":
#     # Path to raw data
#     input_path = 'data/telegram_data.csv'

#     # Path to save cleaned data
#     output_path = 'data/cleaned_telegram_data.csv'

#     process_telegram_data(input_path, output_path)


import re
import pandas as pd
import spacy  # Ensure to use a custom tokenizer for Amharic if available
from sklearn.model_selection import train_test_split

# Load Amharic NLP model (replace 'xx' with Amharic model if available)
try:
    nlp = spacy.load("xx_ent_wiki_sm")
except Exception as e:
    print(f"Error loading model: {e}")
    nlp = None  # Add custom tokenizer or fallback here

def preprocess_amharic_text(text):
    """
    Cleans and tokenizes Amharic text.
    Removes irrelevant characters, normalizes text, and tokenizes.
    """
    if pd.isna(text):  # Check for NaN values
        return ""  # Return an empty string or handle as needed

    # Normalize Amharic text
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with one
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation

    # Tokenize
    if nlp:
        doc = nlp(text)
        tokens = [token.text for token in doc]
    else:
        tokens = text.split()  # Fallback basic tokenization

    return tokens

def process_telegram_data(input_file, output_file):
    """
    Reads raw scraped Telegram data, preprocesses it, and saves the cleaned version.
    """
    # Load the scraped data (assuming a CSV format)
    df = pd.read_csv(input_file)

    # Clean and tokenize each message
    df['cleaned_message'] = df['Message'].apply(preprocess_amharic_text)

    # Save the cleaned and tokenized data for labeling
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Path to raw data
    input_path = '../data/telegram_data.csv'

    # Path to save cleaned data
    output_path = '../data/cleaned_telegram_data.csv'

    process_telegram_data(input_path, output_path)
