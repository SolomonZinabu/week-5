# # scripts/labeling.py

# import pandas as pd

# def load_data(file_path):
#     """
#     Loads the scraped Telegram data from a CSV file.
#     """
#     data = pd.read_csv(file_path)
#     return data

# def label_data(data):
#     """
#     Manually label the dataset. Here you would typically go row by row and
#     apply the correct label (e.g., B-PRODUCT, I-PRICE, etc.) based on the message content.
#     """
#     labeled_data = []

#     for idx, row in data.iterrows():
#         message = row['Message']  # Assuming the column is named 'Message'
#         tokens = message.split()  # Simple tokenization, can be enhanced

#         # Placeholder logic for labeling - to be updated manually
#         for token in tokens:
#             if token.isdigit():
#                 label = 'O'  # Example: labeling numbers as 'O' (non-entity)
#             elif token.lower() in ['product_name', 'example']:  # Example logic
#                 label = 'B-PRODUCT'
#             else:
#                 label = 'O'

#             labeled_data.append((token, label))

#     return labeled_data

# def save_conll_format(labeled_data, output_file):
#     """
#     Saves labeled data to a file in CoNLL format.
#     """
#     with open(output_file, 'w', encoding='utf-8') as f:
#         for token, label in labeled_data:
#             f.write(f"{token} {label}\n")
#         f.write("\n")  # Separate each sentence/message with a blank line





import pandas as pd
import numpy as np  # Import numpy to check for NaN values

def load_data(file_path):
    """
    Loads the cleaned Telegram data from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def label_data(data):
    """
    Manually label the dataset. Here you would typically go row by row and
    apply the correct label (e.g., B-PRODUCT, I-PRICE, etc.) based on the message content.
    """
    labeled_data = []

    for idx, row in data.iterrows():
        message = row['cleaned_message']  # Update to use the cleaned message

        # Check for NaN or non-string values
        if pd.isna(message) or not isinstance(message, str):
            continue  # Skip this row if the message is NaN or not a string

        tokens = message.split()  # Simple tokenization, can be enhanced

        # Placeholder logic for labeling - to be updated manually
        for token in tokens:
            if token.isdigit():
                label = 'O'  # Example: labeling numbers as 'O' (non-entity)
            elif token.lower() in ['product_name', 'example']:  # Example logic
                label = 'B-PRODUCT'
            else:
                label = 'O'

            labeled_data.append((token, label))

    return labeled_data

def save_conll_format(labeled_data, output_file):
    """
    Saves labeled data to a file in CoNLL format.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for token, label in labeled_data:
            f.write(f"{token} {label}\n")
        f.write("\n")  # Separate each sentence/message with a blank line
