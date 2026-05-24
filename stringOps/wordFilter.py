print("Enter a string:")
user_input = input()
print("Enter a word to filter:")
filter_word = input()
words = user_input.split()
filtered_words = [word for word in words if word != filter_word]    
print("Filtered string:", ' '.join(filtered_words))