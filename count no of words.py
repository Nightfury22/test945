# def count_words(sentence):
#  words = sentence.split()
#  return len(words)
# sentence = input("Enter a sentence: ")
# word_count = count_words(sentence)
# print("Number of words:", word_count)





def count_words(string):
    words = string.split()
    return len(words)
string = input("Enter few words: ")
word = count_words(string)
print("Counts are" , word)
