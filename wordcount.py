word_count_file = open('inputfile.txt')

words = {}
ratings = {}


for line in word_count_file:
    line = line.strip()
    words_list = line.split()
    for word in words_list:
        word = word.strip(".,/'\"_-?!")
        word = word.upper() 
        words[word] = words.get(word, 0) + 1

# This works using .get()
# for key, value in words.iteritems():
#     if ratings.get(value):
#         ratings[value].append(key)
#     else:
#         ratings[value] = [key]

# Same result using .setdefault()
for key, value in words.iteritems():
    ratings.setdefault(value, []).append(key)

# print ratings

ratings_keys = ratings.keys()
# In place!
ratings_keys.sort()
# In place!
ratings_keys.reverse()

for key in ratings_keys:
    for word in sorted(ratings[key]):
        print key, word

# for word in words:
#     if words[word] in ratings:
#         ratings[words[word]] = ratings[words[word]] + " " + word
#     else:
#         ratings[words[word]] = word

# for rating in ratings:
#     words = ratings[rating].split()
#     ordered_words = sorted(words)
#     for word in ordered_words:
#         print rating, word 



# def f(x):
#     return (x[1], x[0])

# for key in sorted(words.keys):
#     print key, words[key]

# words = sorted(words.items(), key=f)




        # if item in words:
        #     words[item] +=1
        # else:
        #     words[item] = 1

