def count_words(string, word):
    # Count the occurrences of a word in the string
    return string.lower().count(word)

def same_number_of_occurrences(string, word1, word2):
    count_cat = count_words(string, word1)
    count_dog = count_words(string, word2)

    return count_cat == count_dog

user_input = input("Enter your string: ")
word1 = "cat"
word2 = "dog"

result = same_number_of_occurrences(user_input, word1, word2)
print("Result:", result)
