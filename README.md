# EthioMart NER Project

## Overview

### Business Need

EthioMart aims to become the primary hub for Telegram-based e-commerce activities in Ethiopia. With the increasing popularity of Telegram for business transactions, various independent e-commerce channels have emerged, each facilitating its own operations. However, this decentralization presents challenges for both vendors and customers who need to manage multiple channels for product discovery, order placement, and communication.

To solve this problem, EthioMart plans to create a single centralized platform that consolidates real-time data from multiple e-commerce Telegram channels into one unified channel. This will provide a seamless experience for customers to explore and interact with multiple vendors in one place.

### Project Focus

This project focuses on fine-tuning Large Language Models (LLMs) for an Amharic Named Entity Recognition (NER) system that extracts key business entities such as product names, prices, and locations from text, images, and documents shared across these Telegram channels. The extracted data will populate EthioMart's centralized database, making it a comprehensive e-commerce hub.

## Key Objectives

- Real-time data extraction from Telegram channels.
- Fine-tuning LLMs to extract entities like product names, prices, and locations.

## Possible Entities

- **Product Names or Types**
- **Material or Ingredients**: Specific mentions of materials used in the products.
- **Location Mentions**
- **Monetary Values or Prices**

## Data

- **Source**: Messages and data from Ethiopian-based e-commerce Telegram channels.
- **Sample data**: Collected from the Shageronlinestore and Amharic news labeled NER dataset.
- **Types**: 
  - Text (Amharic language messages)
  - Images (Product images, marketing materials)

## Knowledge and Skills

- **Text Processing**: Handling Amharic text, tokenization, and preprocessing techniques.
- **LLM Fine-tuning**: Adapting large language models for Amharic NER tasks.
- **Model Comparison & Selection**: Evaluating performance using metrics like F1-score, precision, and recall.
- **Model Interpretability**: Using tools such as SHAP (SHapley Additive Explanations) and LIME (Local Interpretable Model-agnostic Explanations) to explain model predictions and outputs.

## Learning Outcomes

By the end of this project, you will have:

- A working pipeline for entity extraction from Amharic Telegram messages.
- A performance analysis of different models and their interpretability.
- Insights into how the extracted entities can be used for business intelligence in e-commerce contexts.

## Competency Mapping

The tasks completed in this project contribute to the following competencies essential for job preparedness in Data Engineering and Machine Learning:

- **Professionalism for a global-level job**: Articulating business values and reporting to stakeholders.
- **Software Development Frameworks**: Using GitHub for CI/CD, writing modular code, and packaging.
- **Python Programming**: Advanced use of Python modules such as Pandas, Matplotlib, Numpy, Scikit-learn, and other relevant packages.
- **SQL Programming**: MySQL database create, read, and write.
- **Data & Analytics Engineering**: Data filtering, transformation, and warehouse management.
- **MLOps & AutoML**: Pipeline design, data and model versioning.
- **Deep Learning and Machine Learning**: NLP, topic modeling, sentiment analysis.
- **Web & Mobile App Programming**: HTML, CSS, Flask, Streamlit.

## Group Work Policy

This project was completed collaboratively in groups, with at least five members in each group. Individual work was also permitted if necessary.

## Team Members

- **Tutors**: Mahlet, Elias, Rediet, Kerod

## Key Dates

- **Discussion on the case**: 09:00 UTC on Wednesday, 25 Sep 2024.
- **Interim Solution**: 20:00 UTC on Friday, 27 Sep 2024.
- **Final Submission**: 20:00 UTC on Tuesday, 01 Oct 2024.

## Tasks Overview

### Task 1: Data Ingestion and Preprocessing

- **Objective**: Set up a data ingestion system to fetch messages from multiple Ethiopian-based Telegram e-commerce channels.
- **Steps**:
  - Identify and connect to relevant Telegram channels using a custom scraper.
  - Implement a message ingestion system to collect text, images, and documents as they are posted in real-time.
  - Preprocess text data by tokenizing, normalizing, and handling Amharic-specific linguistic features.
  - Clean and structure the data into a unified format, separating metadata from message content.
  - Store preprocessed data for further analysis.

### Task 2: Labeling Data in CoNLL Format

- **Objective**: Label a portion of the dataset in CoNLL format for Named Entity Recognition (NER) tasks.
- **Steps**:
  - Label at least 30-50 messages from the provided dataset by identifying entities such as products, prices, and locations in Amharic text.
  - Save the labeled dataset in CoNLL format for use in fine-tuning the NER model.

### Task 3: Fine-Tuning the NER Model

- **Objective**: Fine-tune an NER model using the labeled dataset.
- **Steps**:
  - Load the labeled dataset in CoNLL format and tokenize the data.
  - Fine-tune pre-trained multilingual models using Hugging Face’s Trainer API.
  - Evaluate the model based on accuracy, precision, recall, and F1 score.

### Task 4: Model Comparison and Selection

- **Objective**: Compare different models and select the best-performing one for entity extraction.
- **Steps**:
  - Fine-tune and compare multiple models, including XLM-Roberta, DistilBERT, and mBERT.
  - Use metrics such as precision, recall, F1 score, and accuracy to evaluate the performance of each model.
  - Select the best-performing model based on evaluation metrics.

### Task 5: Model Interpretability

- **Objective**: Explain how the NER model identifies entities using SHAP and LIME.
- **Steps**:
  - Implement SHAP and LIME to interpret the model’s predictions.
  - Analyze difficult cases where the model might struggle to identify entities correctly.
  - Generate reports on the model's decision-making and identify areas for improvement.

## Deliverables

- **Interim Submission**: A data summary that includes your data preparation and labeling steps, submitted in PDF format.
- **Final Submission**: A blog-style PDF outlining your process and exploration results, focusing on data, model selection, and performance on the NER task after fine-tuning.

## References

- Fine-tuning NER Models:
  - [How to fine-tune BERT](https://huggingface.co/transformers/v4.6.0/examples/pytorch/token_classification.html)
  - [Hugging Face Blog on Token Classification](https://huggingface.co/blog/token-classification)
  - [Roberta Multilingual NER](https://huggingface.co/transformers/model_doc/roberta.html)
  - [NER Datasets from Hugging Face](https://huggingface.co/datasets)
  - [How to fine-tune Amharic models](https://github.com/username/amharic-finetuning)
  - [SHAP (SHapley Additive Explanations)](https://github.com/slundberg/shap)
  - [SHAP Official Documentation](https://shap.readthedocs.io/en/latest/)
  - [Tutorial on SHAP](https://shap.readthedocs.io/en/latest/example_notebooks/tabular_examples/Explaining_a_model.html)
  - [How SHAP works](https://towardsdatascience.com/shap-explaining-machine-learning-models-38d632c41861)
  - [LIME (Local Interpretable Model-Agnostic Explanations)](https://github.com/marcotcr/lime)
  - [LIME for Text Models](https://github.com/marcotcr/lime#text)
  - [A Guide to Model Interpretability with SHAP and LIME](https://towardsdatascience.com/interpreting-machine-learning-models-using-shap-and-lime-520ecb1613a2)
  - [Alternative free GPU](https://www.paperspace.com/)
  - [Amazon SageMaker](https://aws.amazon.com/sagemaker/)

## Conclusion

This project provides a comprehensive solution for real-time data extraction from Telegram channels, fine-tuning of LLMs for Amharic NER tasks, and interpretation of model predictions. The results from this work can significantly enhance the e-commerce experience for vendors and customers in Ethiopia, solidifying EthioMart's position as a leading e-commerce platform.

