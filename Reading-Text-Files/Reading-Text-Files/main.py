# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here    
    with open(filename) as f:
        lines = f.readlines()
        return lines

# this cleans the input from the stroy.txt file
def clean_input(text):
    word_list = []
    full_sentence = ""
    for sentence in text:
        full_sentence += sentence.lower()
    each_word = full_sentence.split(" ")
    for word in each_word:
        word = word.strip("?.\n,")
        if word.isalpha():
            word_list.append(word)
    return word_list

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    word_dict = {}
    each_word = clean_input(text)
    for word in each_word:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict
# read_file_content()
print(count_words())