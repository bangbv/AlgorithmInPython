# https://1upnote.me/post/2018/11/ds-ml-bayes-theorem/

import random


def random_kid():
    gender = random.choice(["boy", "girl"])
    birth_date = random.choice(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])
    return gender, birth_date


both_girls = 0
tuesday_girl = 0

random.seed(0)
total = 100000
# total = 100

for _ in range(total):
    first_child = random_kid()
    # print("first_child = ", first_child)
    second_child = random_kid()

    if first_child == ("girl", "tue") or second_child == ("girl", "tue"):
        tuesday_girl += 1
        if first_child[0] == "girl" and second_child[0] == "girl":
            both_girls += 1

print("both_girls = ", both_girls)
print("tuesday_girl = ", tuesday_girl)
print("P(both_girls|tuesday_girl) = ", both_girls / tuesday_girl)
