import numpy as np
import urllib.request as urllib2
import stringdist

def loadnouns():
    # LOADS nouns
    print('loading nouns')
    url_nouns = 'http://www.desiquintans.com/downloads/nounlist/nounlist.txt'
    bytes_nouns = urllib2.urlopen(url_nouns) # it's a file like object and works just like a file
    nouns = [noun.decode("utf-8").replace('\n','') for noun in bytes_nouns]
    print(len(nouns), 'nouns loaded.')
    return nouns

def loadadjectives():
    # LOADS adjectives
    print('loading adjectives')
    url_adjectives = 'https://www.d.umn.edu/~rave0029/research/adjectives1.txt'
    url_adjectives = 'https://gist.githubusercontent.com/hugsy/8910dc78d208e40de42deb29e62df913/raw/eec99c5597a73f6a9240cab26965a8609fa0f6ea/english-adjectives.txt'
    bytes_adjectives = urllib2.urlopen(url_adjectives) # it's a file like object and works just like a file
    adjectives = [adjective.replace(b'\xa0',b'').decode('utf-8').replace('\n','') for adjective in bytes_adjectives]
    print(len(adjectives), 'adjectives loaded.')
    return adjectives

def loadadverbs():
    print('loading adverbs')
    url_adverbs = 'https://raw.githubusercontent.com/janester/mad_libs/master/List%20of%20Adverbs.txt'
    bytes_adverbs = urllib2.urlopen(url_adverbs) # it's a file like object and works just like a file
    adverbs = [adverb.decode('utf-8').replace('\n','') for adverb in bytes_adverbs]
    print(len(adverbs), 'adverbs loaded.')
    return adverbs

def loadtext():
    print('loading text')
    url_pride = 'https://www.gutenberg.org/files/1342/1342-0.txt'
    bytes_pride = urllib2.urlopen(url_pride) # it's a file like object and works just like a file
    pride = ''.join([str(line.decode('utf-8').strip()+' ') for line in bytes_pride]).replace('  ',' ')
    print(len(pride), 'words of text loaded')
    return pride

def get_noun_adj_adv():
    nouns = loadnouns()
    adjectives = loadadjectives()
    adverbs = loadadverbs()
    print('removing words that can be multiple parts of speech')

    # expanded implementation in case of counting how many words are removed
    nouns_ = [word for word in nouns if word not in adjectives and word not in adverbs]
    adjectives_ = [word for word in adjectives if word not in nouns and word not in adverbs]
    adverbs_ = [word for word in adverbs if word not in nouns and word not in adjectives]
    return nouns_,adjectives_,adverbs_

def generate():
    nouns = loadnouns()
    adjectives = loadadjectives()
    adverbs = loadadverbs()
    print('removing words that can be multiple parts of speech')

    # expanded implementation in case of counting how many words are removed
    nouns_ = [word for word in nouns if word not in adjectives and word not in adverbs]
    adjectives_ = [word for word in adjectives if word not in nouns and word not in adverbs]
    adverbs_ = [word for word in adverbs if word not in nouns and word not in adjectives]
    nouns = nouns_
    adjectives = adjectives_
    adverbs = adverbs_

    #[word for word in adjectives if word in nouns or word in adverbs]

    no = ['you','if','anything','just','well','it','she','he']

    print('filtering crappy words')
    nouns = [noun for noun in nouns if noun not in no]
    adjectives = [adj for adj in adjectives if adj not in no]

    t = loadtext().split(' ')
    print('scanning for adj-noun pairs')
    pairs = [str(t[i]+' '+t[i+1]) for i in range(len(t)-1) if t[i] in adjectives and t[i+1] in nouns]
    print('scan complete,',len(pairs),'pairs found')
    return list(set(pairs))

#pairs = generate()
nouns, adjs, advs = get_noun_adj_adv()
# more texts
# https://www.gutenberg.org/browse/scores/top

# %% Method: Levenshtein distances
goal = 'dectivation rate calculator'
dict_dist_cnames = {}
for a in adjs:
    for n in nouns:
        lev = stringdist.levenshtein(a+n,goal)
        dict_dist_cnames[a+' '+n] = lev

leven_sort = sorted(dict_dist_cnames.items(), key=lambda kv: kv[1])
leven_closest = list(set([i[1] for i in leven_sort]))[0:3]
leven_subset = [i for i in leven_sort if i[1] in leven_closest]
len_sort = sorted([i[0] for i in leven_subset[0:40]],key=lambda kv: len(kv))
len_sort

# %% Method: Starts-with

lim = -1
for a in [a for a in adjs if a[0]=='d' and 'r' in a][0:lim]:
    for n in [n for n in nouns if n[0:3]=='cal'][0:lim]:
        print(a,n)
