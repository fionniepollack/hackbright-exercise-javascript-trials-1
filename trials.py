"""Python functions for JavaScript Trials 1."""


def output_all_items(items):

    for item in items:
        print(item)

output_all_items([1, 'hello', 'true'])

def get_all_evens(nums):
    
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums

get_all_evens([1, 2, 3, 4, 5, 6])


def get_odd_indices(items):

    odd_items = []


    for i in range(len(items)):
        if i % 2 != 0:
            odd_items.append(items[i])
    
    return odd_items

get_odd_indices([1, 'hello', True, 500])


def print_as_numbered_list(items):
    
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):

    range_list = []

    num = start

    # Define start
    # Keep adding num until stop
    while num < stop:
        range_list.append(num)
        num += 1

def censor_vowels(word):
    
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    
    return "".join(chars)

result = censor_vowels('hello world')
print(result)

def snake_to_camel(string):
    
    camel_case = []

    for word in string.split("_"):
        titled_word = word.title()
        camel_case.append(titled_word)

    return "".join(camel_case)

result = snake_to_camel('hello_world')
print(result)

def longest_word_length(words):
    
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest


def truncate(string):

    result = []

    for char in string:
        if char not in result:
            result.append(char)

    return "".join(result)

result = truncate('aaaabbbbcccca')
print(result)

def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
