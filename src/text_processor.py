import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def to_lower(word):
    result = word.lower()
    return result

def remove_hyperlink(word):
    return  re.sub(r"http\S+", "", word)

def remove_mentions(word):
    return re.sub(r"@\S+", "", word)

def remove_number(word):
    result = re.sub(r'\d+', '', word)
    return result

def remove_punctuation(word):
    result = re.sub('[^A-Za-z]+', ' ', word)
    return result

def remove_whitespace(word):
    result = word.strip()
    return result

def replace_newline(word):
    return word.replace('\n','')

def remove_stopwords(word):
    return ' '.join(word for word in i.split() if word not in stopwords)
    
def remove_security_symbol(tickers):
    result = []
    for ticker in tickers:
        result.append(ticker.replace('#','').replace('$',''))
    return result

def clean_up_pipeline(sentence):
    cleaning_data = [remove_hyperlink,
                      replace_newline,
                      to_lower,
                      remove_number,
                      remove_punctuation,
                      remove_whitespace]
    for func in cleaning_data:
        
        sentence = func(sentence)
    return sentence

def sentiments_with_nltk(rawtext):
    text = clean_up_pipeline(rawtext)
    sia = SentimentIntensityAnalyzer()
    clean_text = clean_up_pipeline(text)
    score = sia.polarity_scores(clean_text)["compound"]
    label =""
    if(score > 0):
        label = 'positive'
    elif(score == 0):
        label = 'neutral'
    else:
        label = 'negative'
    result = {"score":score,"label":label}     
    return result

# need language detector and translator

