punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
   
def strip_punctuation(input_str):
    for ele in input_str:
        if ele in punctuation_chars:
            input_str = input_str.replace(ele, '')
    return input_str


def get_neg(input_tweet):
    input_tweet = input_tweet.lower()
    input_tweet = strip_punctuation(input_tweet)
    input_tweet = input_tweet.split()
    neg_score = 0
    for word in input_tweet:
        if word in negative_words:
            neg_score += 1
    return neg_score


def get_pos(input_tweet):
    input_tweet = input_tweet.lower()
    input_tweet = strip_punctuation(input_tweet)
    input_tweet = input_tweet.split()
    pos_score = 0
    for word in input_tweet:
        if word in positive_words:
            pos_score += 1
    return pos_score
