#7, 9, 12, 13, 15, 17, 23, 26
import nltk, pylab, random
from nltk.corpus import gutenberg
from collections import Counter
from nltk.corpus import wordnet as wn
from nltk.corpus import brown

def exercise7():
    moby_dick = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
    moby_dick.concordance("however")

def exercise8():
    names = nltk.corpus.names
    #male = names.words('male.txt')
    #female = names.words('female.txt')
    cfd = nltk.ConditionalFreqDist((gender, name[0]) for gender in names.fileids() for name in names.words(gender))
    cfd.plot()

def exercise9():
    moby_dick = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
    emma = nltk.corpus.gutenberg.words('austen-emma.txt')
    print(len(set(moby_dick)), ", ", len(set(emma)))
    print((len(set(moby_dick)) / len(moby_dick)), ", ", (len(set(emma)) / len(emma)))

def exercise12():
    entries = nltk.corpus.cmudict.entries()
    s = set()
    l = []
    for entry in entries:
        s.add(entry[0])
        l.append(entry[0])
    print(len(s))
    counts = Counter(l)
    count = 0
    for word in s:
        if counts[word] > 1:
            count+=1
    print(count)

def exercise13():
    print(len([word for word in wn.all_synsets('n') if not word.hyponyms()]))
    print(len([word for word in wn.all_synsets('n')]))

def exercise15():
    fdist = nltk.FreqDist(nltk.corpus.brown.words())
    filtered = [word for (word, frequency) in fdist.items() if frequency >= 3]
    print(filtered)

def exercise17(text):
    stopwords = nltk.corpus.stopwords.words('english')
    minus_stopwords = [w for w in text if w.lower not in stopwords]
    fdist = nltk.FreqDist(minus_stopwords)
    print(list(fdist.keys())[:50])

def exercise23():
    random_string = ""
    for i in range(100000):
        random_string += random.choice('abcdefg ')
    random_text = random_string.split()
    fdist = nltk.FreqDist(random_text)
    pylab.plot(range(1, fdist.B() + 1), fdist.values())
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.show()

def exercise26():
    num_nouns = num_hyponyms = 0
    for noun in wn.all_synsets('n'):
        num = len(noun.hyponyms())
        if num>0:
            num_hyponyms += num
            num_nouns += 1
    print(num_nouns)
    print(num_hyponyms)

exercise9()
