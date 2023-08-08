def even_filter(input_list):
    liist=[]
    for i in input_list:
        if i%2!=0:
            liist.append(i)
    return liist

def odd_filter(input_dict):
     dictt=[]
     for i in input_dict.values():
        if i%2==0:
            dictt.append(i)
     return dictt


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # User-defined dictionary with keys and values
numbers_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }

    # Call the even_filter function with the list of numbers
even_numbers = even_filter(numbers_list)
print("Even Filter on the list: ", even_numbers)

    # Call the odd_filter function with the dictionary of numbers
odd_numbers_list = odd_filter(numbers_dict)
print("Odd Filter on  the dictionary: ", odd_numbers_list)
