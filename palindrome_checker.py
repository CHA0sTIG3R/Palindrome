# Palindrome Checker

# 1st approach
# easy to read but many unnecessary steps
# also not good for memory especially if checking for a long sentence.


# text = input("Enter a text to check: ")    # input
# text = text.lower()     # do this because Uppercase letter and lowercase are represented differently
# lst = []    # empty list to store characters
# if not text == "":    # checks to make sure input is not empty
#     for ch in text:   # iterate through characters in the input
#         if not ch == " ":   # gets rid of spaces
#             lst.append(ch)   # append to empty list
#     lst2 = lst[::-1]   # reverse list and assign to another list
#     if lst2 == lst:   # check if it's equal to it's reversed self
#         print("it's a palindrome") 
#     else:
#         print("it's not a palindrome")
# else:
#     print("it's not a palindrome")



#second approach
# optimized for memory
#less redundant steps
# also doesn't need a list


text = input("Enter text: ")

text = text.replace(' ','')  # remove all spaces

if len(text) > 1 and text.upper() == text[::-1].upper(): # and check if the word is equal to it's reversed self
    print("It's a palindrome")
else:
    print("It's not a palindrome")