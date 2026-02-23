def arabic_tokenize(text):
    # Assuming you want a basic tokenization splitting on spaces
    return text.split() 


def remove_arabic diacritics(text):
    diacritics = {'60', '61', '62', '63', '64', '65', '66', '67', '68', '70'}
    return ''.join(c for c in text if c not in diacritics) 


def preprocess_arabic_text(text):
    text = remove_arabic_diacritics(text)
    tokens = arabic_tokenize(text)
    return tokens
