import random

print(random.randint(5, 20))  # line 1
# first run: 16
# second run: 19
# third run: 17
# the smallest possible is 5 and largest 20 as .randint is inclusive

print(random.randrange(3, 10, 2))  # line 2
# first run: 9
# second run: 5
# third run: 7
# the smallest is 3 and largest 9
# it could not have produced a 4 as the range starts at 3 and steps up 2 at a time

print(random.uniform(2.5, 5.5))  # line 3
# first run: 3.9708922128524837
# second run: 4.093278087722366
# third run: 3.6407926821663636
# the smallest is 2.5 and largest 5.5
# due to how floating point numbers work it is extremely unlikely for either end point to be hit exactly

# produces a random number between 1 and 100 (inclusive)
print(random.randint(1, 100))
