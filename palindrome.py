# def is_palindrome(string):
#     reversed_string = string[::-1]
#     if string == reversed_string:
#         return True
#     else:
#         return False
# word = input("Enter a word: ")
# if is_palindrome(word):
#     print(f"'{word}' is a Palindrome")
# else:
#     print(f"'{word}' is not a Palindrome")


















def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False
word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}'It is a palindrome")
else:
    print("It is not a palindrome")

