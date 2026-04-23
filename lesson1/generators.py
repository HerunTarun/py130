# question 1
reciprocals = (1 / x for x in range(1, 11))

for value in reciprocals:
    print(value)

# question 2
def reciprocal(num):
    counter = 1

    while counter <= num:
        yield 1 / counter
        counter += 1

reciprocal_generator = reciprocal(10)
for num in reciprocal_generator:
    print(num)

# question 3
word_list = ['cat', 'dog', 'fish', 'bird', 'monkey']

capitalized = (word.capitalize() for word in word_list)
print(tuple(capitalized))

# question 4
def capitalized_words(words):
    for word in words:
        yield word.capitalize()

word_list = ['cat', 'dog', 'fish', 'bird', 'monkey']
capitalized = capitalized_words(word_list)
print(tuple(capitalized))

# question 5
word_list = ['cat', 'dog', 'fish', 'bird', 'monkey']
capitalized = (word.capitalize() for word in word_list if len(word) >= 5)
print(set(capitalized))

# question 6
def capitalize_under_five(words):
    for word in words:
        if len(word) < 5:
            yield word.capitalize()

word_list = ['cat', 'dog', 'fish', 'bird', 'monkey']
capitalized = capitalize_under_five(word_list)
print(set(capitalized))
