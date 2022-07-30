from flask import Flask, render_template, request
import nltk
from nltk.corpus import words
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
import os
import pandas as pd

app = Flask(__name__)
nltk.download('words')
correct_spellings = words.words()
spellings_series = pd.Series(correct_spellings)

@app.route('/')
def index():
    return render_template("index.html")

def suggestion(string, gram_number=3):
    outcomes = []
    spellings = spellings_series[spellings_series.str.startswith(string[0])] 
    distances = ((jaccard_distance(set(ngrams(string, gram_number)), set(ngrams(word, gram_number))), word)
                 for word in spellings)
    
    distances = list(sorted(distances))
    iterator = 0
    for i,j in distances:
        if(j not in outcomes and len(j)<len(string)+3 and (len(j)> len(string)-3) and len(j)>1):
            score = 0
            for k in j:
                if k in string:
                    score+=1
            if(score>2 and len(string)>3) or len(string)<=3:
                outcomes.append(j)
                iterator+=1
        if(iterator==3):
           return outcomes

@app.route('/result', methods=('GET', 'POST'))
def result():
    if request.method == 'GET':
        ans = request.args.getlist('title')
        results = suggestion(ans[0])
    return render_template("result.html", results= results)
