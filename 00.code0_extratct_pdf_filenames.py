import os
import pandas as pd

# Set the path to the folder containing the PDF files
folder_path = "C:/Users/CarlosMartinsFerreir/Desktop/ICEGOV 2023/_codes/ACM"

# Get a list of the names of all PDF files in the folder
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

# Create a pandas DataFrame from the list of PDF file names
df = pd.DataFrame(pdf_files, columns=["Filename"])

# Write the DataFrame to an Excel file
output_file = "pdf_filenames.xlsx"
df.to_excel(output_file, index=False)

# Print a message indicating that the file was saved
print('Results saved to pdf_filenames.xlsx.')
