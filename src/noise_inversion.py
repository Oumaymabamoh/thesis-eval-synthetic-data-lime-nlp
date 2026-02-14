import pandas as pd

# Load the data
df = pd.read_csv('../data/processed.csv')

column_name = 'review'

def reverse_words(text):
    # This reverses the order of words
    if isinstance(text, str):
        return " ".join(text.split()[::-1])
    return text

def preprocess_data(df, column_name, apply_noise=False):
    # We use .copy() to avoid SettingWithCopy warnings
    df_processed = df.copy()
    if apply_noise:
        df_processed[column_name] = df_processed[column_name].apply(reverse_words)
    return df_processed

# Execute the processing
df_new = preprocess_data(df, column_name, apply_noise=True)

# Save to a new file
df_new.to_csv('../../data/noisy_inversion.csv', index=False)

print("File saved successfully!")