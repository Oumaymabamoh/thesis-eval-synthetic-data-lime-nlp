import pandas as pd

def reverse_word_chars(text):
    if isinstance(text, str):
        words = text.split()
        # Reverse each individual word then join them
        return " ".join([word[::-1] for word in words])
    return text

# Load the data
data = pd.read_csv('../data/processed.csv')

# Identify the review column
column_to_reverse = 'review'

# Apply the function and OVERWRITE the original column
# By using the same name, the original 'review' is replaced
data[column_to_reverse] = [reverse_word_chars(str(text)) for text in data[column_to_reverse]]

# View the results shows only  the modified column
print(data[[column_to_reverse]].head())

# 5. Save the results
# The original text is gone; only the reversed version remains in 'review'
data.to_csv('../data/noisy_reversal.csv', index=False)

print("Process complete! File saved successfully!")






