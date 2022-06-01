# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

#runs on O(n) time
def find_anagrams(word_one, word_two):
    # [assignment] Add your code here
    if len(word_one) == len(word_two):
        word_one = word_one.lower()
        word_two = word_two.lower()
        word_one_dict = {}
        word_two_dict = {}
        for each_letter in word_one:
            if each_letter not in word_one_dict:
                word_one_dict[each_letter] = 1
            else:
                 word_one_dict[each_letter] += 1
        for each_letter in word_two:
            if each_letter not in word_two_dict:
                word_two_dict[each_letter] = 1
            else:
                 word_two_dict[each_letter] += 1
        return word_one_dict == word_two_dict
    else:
        return False

print(find_anagrams("Binary", "BRAinnY"))