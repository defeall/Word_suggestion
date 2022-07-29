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
        if(j not in outcomes and len(j)<len(string)+2 and (len(j)> len(string)-2) and len(j)>1):
           outcomes.append(j)
           iterator+=1
        if(iterator==3):
           return outcomes

@app.route('/result', methods=('GET', 'POST'))
def find_res():
    if request.method == 'POST':
        string = request.form['title']
        res = str(suggestion(string))
    
    return render_template("result.html", res)


