import nltk
from nltk.corpus import stopwords
import string
import random
import pickle
stop = stopwords.words('english') + [i for i in string.punctuation]

wnl = nltk.WordNetLemmatizer()

sentimentcorpus = nltk.corpus.reader.PlaintextCorpusReader(r"/home/nitrous/data/debate/",
r"tweets.(pos|neg)")

corpora = { "neg": "tweets.neg", "pos": "tweets.pos"  }
docs = []
for a in corpora:
  raw = sentimentcorpus.raw(corpora[a])
  for sent in raw.split("\n"):
    #print sent
    tokens  = [i for i in nltk.word_tokenize(sent.lower()) if i not in stop]
    lemmatised = [wnl.lemmatize(t) for t in tokens]
    index = dict.fromkeys(set(lemmatised), 0)
    for b in lemmatised:
      index[b] += 1.0
    docs.append((dict(index), a))
print len(docs)

random.shuffle(docs)

int(len(docs)*0.75)
train_data = docs[:int(len(docs)*0.75)]
test_data = docs[int(len(docs)*0.75):]

print str(len(train_data))+": "+str(len(test_data))
print(test_data[0])
classifier = nltk.classify.NaiveBayesClassifier.train(train_data)

result = {
  'neg': {'neg': 0, 'pos':0},
  'pos': {'neg': 0, 'pos':0 }

}
for a in test_data:
  b = classifier.classify(a[0])
  result[a[1]][b] = result[a[1]][b]+1

print classifier.show_most_informative_features()

print ("\t\tneg\tpos")
for a in result:
  print str(a)+"\t"+str(result[a]['neg'])+"\t"+str(result[a]['pos'])

f = open('my_classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()