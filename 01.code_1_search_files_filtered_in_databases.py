import os
import fitz
import re
import pandas as pd

# Set the folder containing the PDF files
folder_path = 'C:/Users/CarlosMartinsFerreir/OneDrive/####Working on/_Governance - AI Public Sector/_codes/ACM+IEEE_Clean'

# Define the search expressions
expression_words = ['artificial intelligence', 'public sector']

# Define the search words
search_words = ['ethics', 'ethical', 'fair', 'fairness', 'data privacy', 'interpretable', 'interpretability',
                'explainable', 'explainability', 'trust', 'trustworthy', 'trustworthness','responsible AI', 'transparency']

# Initialize an empty list to store the results
results = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Get the full path to the PDF file
        file_path = os.path.join(folder_path, filename)
        # Open the PDF file
        with fitz.open(file_path) as pdf_file:
            # Read the contents of the file
            text = ''
            for page in pdf_file:
                text += page.get_text().lower()
            # Check if the file contains the two expressions and at least one search word
            contains_expressions = all(expression in text for expression in expression_words)
            contains_search_word = any(re.search(word, text) for word in search_words)
            # If contains...
            if contains_expressions and contains_search_word:
                # Add just the filename to the results list by append method
                results.append(os.path.basename(file_path))

# Convert the results list to a DataFrame
df = pd.DataFrame(results, columns=['Filename'])

# Save the results to an Excel file
df.to_excel('01.code_1_results_Clean.xlsx', index=False)

# Print a message indicating that the file was saved
print('Results saved to 01.code_1_results_Clean.xlsx.')
