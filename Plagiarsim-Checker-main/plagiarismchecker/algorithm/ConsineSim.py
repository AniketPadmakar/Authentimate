
import re
import math
from collections import Counter

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())

    matchWords = {}
    for i in intersection:
        if(vec1[i] > vec2[i]):
            matchWords[i] = vec2[i]
        else:
            matchWords[i] = vec1[i]
       
    numerator = sum([vec1[x] * matchWords[x] for x in intersection])
   
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([matchWords[x]**2 for x in matchWords.keys()])

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if denominator == 0:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):

    words = WORD.findall(text)

    return Counter(words)


def cosineSim(text1, text2):
    t1 = text1.lower()
    t2 = text2.lower()
    vector1 = text_to_vector(t1)
    vector2 = text_to_vector(t2)
    cosine = get_cosine(vector1, vector2)
    return cosine