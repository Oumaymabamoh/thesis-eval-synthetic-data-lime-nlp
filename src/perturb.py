import random
import pandas as pd
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# ... your existing imports follow ...
import nltk
nltk.download('vader_lexicon', quiet=True)


df = pd.read_csv('../data/processed.csv')

column_name = 'review'

# Initialize VADER sentiment analyzer
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()


def shuffle_word_chars(word):
    if len(word) <= 3:
        return word
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
        # 1. Clean the word for sentiment checking
        clean_word = re.sub(r'[^\w]', '', word)

        # 2. Check sentiment score (-1.0 to 1.0)
        score = sia.polarity_scores(clean_word)['compound']

        # 3. Logic: Shuffle if sentiment is significant OR a small random chance
        # We skip capitalized words (likely Products/Names) unless they are at the start
        is_capitalized = word[0].isupper() and not text.startswith(word)

        if (abs(score) > 0.1) and not is_capitalized:
            # High sentiment word detected (e.g., 'waste', 'regretted', 'amazing')
            new_words.append(shuffle_word_chars(word))
        elif random.random() < random_buffer:
            # Low random noise to non-sentiment words
            new_words.append(shuffle_word_chars(word))
        else:
            new_words.append(word)

    return " ".join(new_words)

# --- Execution ---
df[column_name] = df[column_name].apply(apply_sentiment_noise)


df.to_csv('../data/perturb.csv')
print("Process complete! The words have been 'shuffled' into typos.")