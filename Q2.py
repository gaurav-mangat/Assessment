def paragraph_to_list(paragraph):
    result_list=[]
    words = paragraph.split()
    for word in words:
        if(len(word)>4):
            result_list.append(word)
    return result_list


user_input = input("Enter your paragraph:\n")
result_list = paragraph_to_list(user_input)
print("\nWords with more than 4 letters: ")
print(result_list)

