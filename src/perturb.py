import random
import pandas as pd
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


nltk.download('vader_lexicon', quiet=True)


df = pd.read_csv('../data/processed.csv')

column_to_process = 'review'


sia = SentimentIntensityAnalyzer()


def shuffle_word_chars(word):
    """Shuffles internal characters of a word while keeping first/last letters."""
    if len(word) <= 3:
        return word
    # Split punctuation from the word to avoid shuffling symbols
    match = re.match(r"(\w+)([^\w]*)", word)
    if not match: return word

    actual_word, punctuation = match.groups()
    if len(actual_word) <= 3: return word

    char_list = list(actual_word)
    first, middle, last = char_list[0], char_list[1:-1], char_list[-1]
    random.shuffle(middle)
    return first + "".join(middle) + last + punctuation


def apply_sentiment_noise(text, random_buffer=0.1):
    if not isinstance(text, str) or not text.strip():
        return text

    words = text.split()
    new_words = []

    for word in words:
        # 1. Clean the word for checking
        clean_word = re.sub(r'[^\w]', '', word).lower()

        # 2. Check sentiment score
        # Using polarity_scores on a single word
        scores = sia.polarity_scores(clean_word)
        compound_score = scores['compound']

        # 3. Logic: Lowered threshold (0.01) to catch "low sentiment" words
        # Also specifically check if 'pos' or 'neg' is non-zero
        has_any_sentiment = abs(compound_score) > 0.01 or scores['pos'] > 0 or scores['neg'] > 0

        # Exclude capitalized words that aren't at the start (potential brand names)
        is_capitalized = word[0].isupper() and not text.startswith(word)

        if has_any_sentiment and not is_capitalized:
            # This will now catch "never", "poorly", "better", and "disaster"
            new_words.append(shuffle_word_chars(word))
        elif random.random() < random_buffer:
            # Small chance to shuffle even if neutral
            new_words.append(shuffle_word_chars(word))
        else:
            new_words.append(word)

    return " ".join(new_words)


# Example Test
test_sentence = "this movie was a total disaster. I'll never go back"
print(f"Original: {test_sentence}")
print(f"Shuffled: {apply_sentiment_noise(test_sentence)}")

# --- Execution ---

if column_to_process in df.columns:
    df[column_to_process] = df[column_to_process].apply(apply_sentiment_noise)
else:
    print(f"Error: Column '{column_to_process}' not found in DataFrame.")

# 3. Verify uniqueness
print(f"Total Rows: {len(df)}")
print(f"Unique IDs: {df['id'].nunique()}") # Change 'id' to your ID column name

# --- Execution ---
#df[column_name] = df[column_name].apply(apply_sentiment_noise)


df.to_csv('../data/noisy.csv')
print("Process complete!")