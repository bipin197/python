print("Enter a string:")
user_input = input()
words = user_input.split()
word_count = len(words) 
print("Number of words in the string:", word_count)

def count_words(input_string):
    words = input_string.split()
    return len(words)

def word_frequency(input_string):
    words = input_string.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def main():
    print("Enter a string:")
    user_input = input()
    word_count = count_words(user_input)
    frequency = word_frequency(user_input)
    print("Number of words in the string:", word_count)
    print("Word frequency:", frequency)

if __name__ == "__main__":
    main()
