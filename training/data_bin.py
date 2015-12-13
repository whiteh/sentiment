import nltk;

loc = "/home/nitrous/data/debate08_sentiment_tweets.tsv"

f = open(loc, "r")

out_pos = open("/home/nitrous/data/debate/tweets.pos", "w")
out_neg = open("/home/nitrous/data/debate/tweets.neg", "w")

totals = dict.fromkeys(['1','2','3','4', "none"], 0)


for line in f:
  line = line.strip()
  parts = line.split("\t")
  votes = dict.fromkeys(['1','2','3','4'], 0)
  max_votes =0
  max_item = "none"
  for a in parts[5:]:
    votes[a] = votes[a]+1
  for a in votes:
    if votes[a]>max_votes:
      max_votes= votes[a]
      max_item = a
  totals[max_item] = totals[max_item]+1
  if max_item == "1": #Neg
    out_neg.write(parts[2]+"\n")
  elif max_item == "2": #Pos
    out_pos.write(parts[2]+"\n")
for a in totals:
  print a+": "+str(totals[a])
f.close()
out_pos.close();
out_neg.close()


#1 tweet.id
#2 pub.date.GMT
#3 content#author.name
#4 author.nickname
#5 rating.1
#6r"rating.2
#7rating.3
#8rating.4
#9 rating.5
#10 rating.6
#11 rating