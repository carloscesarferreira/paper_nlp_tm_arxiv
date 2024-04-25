import os
import fitz
import pandas as pd

# List of words to search for
search_words = ['ethics', 'ethical', 'fair', 'fairness', 'data privacy', 'interpretable', 'interpretability',
                'explainable', 'explainability', 'trust', 'trustworthy', 'trustworthiness', 'responsible AI', 'transparency']

# Function to search for occurrences of search_words in a single PDF file
def search_file(file_path):
    doc = fitz.open(file_path)
    occurrences = [0] * len(search_words)
    for page in doc:
        text = page.get_text()
        for i, word in enumerate(search_words):
            count = text.lower().count(word.lower())
            occurrences[i] += count
    doc.close()
    return occurrences

# Create a list to hold the results for each file
results = []

# Iterate over all PDF files in the specified directory
directory = 'C:/Users/CarlosMartinsFerreir/OneDrive/####Working on/_Governance - AI Public Sector/_codes/ACM+IEEE_searched_Clean'
for file_name in os.listdir(directory):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(directory, file_name)
        occurrences = search_file(file_path)
        results.append([file_name] + occurrences)

# Convert the results list to a pandas DataFrame
df = pd.DataFrame(results, columns=['File'] + search_words)

# Calculate the averages
averages = {}
for word in search_words:
    word_occurrences = df[word].values
    word_averages = word_occurrences[word_occurrences > 0].mean()
    averages[word] = round(word_averages, 0)

# Create a new DataFrame to hold the filtered results
filtered_results = []
for index, row in df.iterrows():
    file_name = row['File']
    for word in search_words:
        if row[word] >= averages[word]:
            filtered_results.append([file_name, word, row[word]])

# Convert the filtered results list to a pandas DataFrame
filtered_df = pd.DataFrame(filtered_results, columns=['File', 'Word', 'Occurrences'])

# Save the filtered results to an Excel file
filtered_df.to_excel('02.code_2_results_Clean.xlsx', index=False)

# Print a message indicating that the file was saved
print('Results saved to 02.code_2_results_Clean.xlsx.')


