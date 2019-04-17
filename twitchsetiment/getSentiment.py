import sklearn
import pandas as pd
from sklearn.datasets import load_files
from sklearn.utils import shuffle

# Import data
twitter_train = pd.read_csv("training_data.csv")
twitter_train = shuffle(twitter_train)

# CountVectorizer Words
from sklearn.feature_extraction.text import CountVectorizer
import nltk


twitter_vec = CountVectorizer(
    min_df=2, 
    tokenizer=nltk.word_tokenize
)  
twitter_counts = twitter_vec.fit_transform(twitter_train.message)

# Convert raw frequency counts into TF-IDF values
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
twitter_tfidf = tfidf_transformer.fit_transform(twitter_counts)

# Training and testing
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

docs_train, docs_test, y_train, y_test = train_test_split(
    twitter_tfidf, twitter_train['rank'], test_size = 0.80, random_state = 1)


clf = MultinomialNB().fit(docs_train, y_train)

y_pred = clf.predict(docs_test)

# from joblib import dump, load
# dump(clf, 'twitchsentiment.chatmodel') 
# print(sklearn.metrics.accuracy_score(y_test, y_pred))


#Testing

import csv
reviews_new = []

with open("../scrapedchat/a_seagull.csv", 'r', encoding='utf8') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        reviews_new.append(row[0])


reviews_new_counts = twitter_vec.transform(reviews_new)
reviews_new_tfidf = tfidf_transformer.transform(reviews_new_counts)

# have classifier make a prediction
pred = clf.predict(reviews_new_tfidf)

positive = 0
negative = 0
# print out results
for review, category in zip(reviews_new, pred):
    # print('%r => %s' % (review, category))
    if(category == "negative" ):
        negative+=1

    if(category == "positive" ):
        positive+=1

print("postive: " + str(positive))
print("negative: " + str(negative))