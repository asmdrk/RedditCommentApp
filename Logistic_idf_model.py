import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

# read the dataset
data = pd.read_csv('data/twitter_sentiments.csv')

#split into train and test
train, test = train_test_split(data, test_size = 0.25, stratify = data['label'], random_state=21)

#converts dataframe into countvector, then gets idf
tfidf_vectorizer = TfidfVectorizer(lowercase= True, max_features=1000, stop_words=list(ENGLISH_STOP_WORDS))

#train or fits model
tfidf_vectorizer.fit(train['tweet'])


# transform the train and test data
train_idf = tfidf_vectorizer.transform(train.tweet)
test_idf  = tfidf_vectorizer.transform(test.tweet)

# create the object of LinearRegression Model
model_LR = LogisticRegression()

# fit the model with the training data
model_LR.fit(train_idf, train.label)

# predict the label on the traning data
predict_train = model_LR.predict(train_idf)

# predict the model on the test data
predict_test = model_LR.predict(test_idf)

# define the stages of the pipeline
pipeline = Pipeline(steps= [('tfidf', TfidfVectorizer(lowercase=True,
                                                      max_features=1000,
                                                      stop_words= list(ENGLISH_STOP_WORDS))),
                            ('model', LogisticRegression())])

# fit the pipeline model with the training data
pipeline.fit(train.tweet, train.label)

# import joblib
from joblib import dump

# dump the pipeline model
dump(pipeline, filename="text_classification.joblib")