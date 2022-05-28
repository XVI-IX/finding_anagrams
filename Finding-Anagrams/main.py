# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word_adjusted = word.replace(" ", '').lower()

    word_dict = {}
    
    for letter in word_adjusted:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1

    

    anagram_adjusted = anagram.replace(" ", '').lower()
    anagram_dict = {}

    for letter in anagram_adjusted:
        if letter in anagram_dict:
            anagram_dict[letter] += 1
        else:
            anagram_dict[letter] = 1

    for letter in word:
        if word_dict == anagram_dict:
            print(f"\"{word}\" and \"{anagram}\" are anagrams")
            return True
        else:
            print(f"\"{word}\" and \"{anagram}\" are not anagrams.")
            return True



