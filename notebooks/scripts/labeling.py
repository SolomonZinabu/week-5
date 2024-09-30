
import pandas as pd
import re  # Import regex for Amharic detection

def load_data(file_path):
    """
    Loads the cleaned Telegram data from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def is_amharic(token):
    """
    Determines if a token is Amharic based on Unicode ranges.
    Amharic characters are mostly in the range U+1200 to U+137F.
    """
    return re.search(r'[\u1200-\u137F]', token) is not None

def label_data(data):
    """
    Manually label the dataset. The function labels tokens in Amharic messages with specific
    entity tags such as B-PRODUCT, I-PRICE, B-LOC, etc., and marks English or non-entity tokens as 'O'.
    """
    labeled_data = []

    # Placeholder lists for identifying products, prices, and locations
    product_keywords = ['ማሳጅ', 'ማድረጊያ']  # Add more product-related words
    location_keywords = ['አዲስ', 'አበባ', 'ቦሌ']  # Add more locations
    price_keywords = ['ብር', 'ዋጋ']  # Add price-related terms

    for idx, row in data.iterrows():
        message = row['cleaned_message']  # Ensure we are using the cleaned message

        # Check for NaN or non-string values
        if pd.isna(message) or not isinstance(message, str):
            continue  # Skip rows where the message is NaN or not a string

        tokens = message.split()  # Tokenize the message

        for token in tokens:
            if not is_amharic(token):
                labeled_data.append((token, 'O'))  # Label non-Amharic tokens as 'O'
                continue

            # Label Amharic tokens with entity labels
            if any(keyword in token for keyword in product_keywords):
                labeled_data.append((token, 'B-PRODUCT'))
            elif any(keyword in token for keyword in price_keywords):
                labeled_data.append((token, 'B-PRICE'))
            elif any(keyword in token for keyword in location_keywords):
                labeled_data.append((token, 'B-LOC'))
            else:
                labeled_data.append((token, 'O'))  # Default label for non-entities

    return labeled_data

def save_conll_format(labeled_data, output_file):
    """
    Saves labeled data to a file in CoNLL format.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for token, label in labeled_data:
            f.write(f"{token} {label}\n")
        f.write("\n")  # Separate each sentence/message with a blank line
