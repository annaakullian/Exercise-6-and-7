from sys import argv
# import sys

script, the_data = argv

reviews_file = open(the_data)
#out_file = open("OUTPUT", "w")

reviews = {}

#for line in sys.stdin.readlines():
for line in reviews_file:  
    line = line.strip()
    restaurant, review = line.split(":")
    # print restaurant, review

    reviews[restaurant] = review

# print reviews

sorted_restaurant_names = sorted(reviews.keys())

for restaurant in sorted_restaurant_names:
    print "%s is rated at %d" % (restaurant, int(reviews[restaurant]))
    #out_file.write("%s is rated at %d\n" % (restaurant, int(reviews[restaurant])))

#out_file.close()
# print sorted_restaurant_names


# print sorted(data.keys)

# for key in sorted(data.keys):
#     print "Restaurant %s is rated at %d" % key, data[key]

