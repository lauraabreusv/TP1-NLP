from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import io

def read_words(filename):
    last = ""
    with open(filename) as inp:
        while True:
            buf = inp.read(10240)
            if not buf:
                break
            words = (last+buf).split()
            last = words.pop()
            for word in words:
                yield word
        yield last

stop_words = set(stopwords.words('english')) 
with open('filtered.txt', 'w') as output:
    for word in read_words('text8'):
        if not word in stop_words:
            output.write("%s " % word)