word_count_file = raw_input ("what file would you like to count?")
word_count_file = open(word_count_file)

words = {}

for line in word_count_file:
    line = line.strip()
    words_list = line.split()
    for item in words_list:
        item = item.strip(".,/'\"_-?!")
        words[item] = words.get(item, 0) + 1
        # if item in words:
        #     words[item] +=1
        # else:
        #     words[item] = 1


print words 