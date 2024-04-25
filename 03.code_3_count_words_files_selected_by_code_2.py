import os
import pandas as pd
import fitz

# Set the folder containing the PDF files
folder_path = 'C:/Users/CarlosMartinsFerreir/OneDrive/####Working on/_Governance - AI Public Sector/_codes/ACM+IEEE_searched_selection_Clean'

# Define the search words
search_words = ['ethics', 'ethical', 'fair', 'fairness', 'data privacy', 'interpretable', 'interpretability',
                'explainable', 'explainability', 'trust', 'trustworthy', 'trustworthiness','responsible AI', 'transparency']

# Create an empty dictionary to store the results
results = {}

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Open the PDF file
        with fitz.open(os.path.join(folder_path, filename)) as doc:
            # Read the contents of the file
            text = ''
            for page in doc:
                text += page.get_text()
            # Search for occurrences of the search words in the text
            for word in search_words:
                count = text.lower().count(word.lower())
                # Add the count to the dictionary
                if word in results:
                    results[word] += count
                else:
                    results[word] = count

# Create a pandas DataFrame from the results dictionary
df = pd.DataFrame(list(results.items()), columns=['Word', 'Occurrences'])

# Save the DataFrame to an Excel file
df.to_excel('03.code_3_results_Clean.xlsx', index=False)

# Print a message indicating that the file was saved
print('Results saved to 03.code_3_results_Clean.xlsx.')
