from sklearn.datasets import fetch_20newsgroups

train = fetch_20newsgroups(data_home="E:/Sharan.S folder/7th Semester/ML lab/Executables/Lab",subset="train")
test = fetch_20newsgroups(data_home="E:/Sharan.S folder/7th Semester/ML lab/Executables/Lab",subset="test")

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
cv = CountVectorizer()
tfidf = TfidfTransformer()

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()

train_cv = cv.fit_transform(train.data)
train_tfidf = tfidf.fit_transform(train_cv)
model.fit(train_tfidf,train.target)

test_cv = cv.transform(test.data)
test_tfidf = tfidf.transform(test_cv)
pred = model.predict(test_tfidf)

from sklearn.metrics import accuracy_score
print(accuracy_score(pred,test.target))
