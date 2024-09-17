'''
884. Uncommon Words from Two Sentences - Easy
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.


Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"] 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
'''

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        dictionary_solution = {}

        def string_to_list(string: str):
            return string.lower().split()
        
        s1, s2 = string_to_list(s1), string_to_list(s2)

        def dict_count(dictionary, sentence):
            '''
            Arguments:
                dictionary must be dict
                sentence must be LIST
            Returns:
                Edited dictionary
            '''
            for word in range(len(sentence)):
                if sentence[word] not in dictionary:
                    dictionary[sentence[word]] = 1

                elif sentence[word] in dictionary:
                    dictionary[sentence[word]] += 1

            return dictionary
        
        dict_count(dictionary_solution, s1)
        dict_count(dictionary_solution, s2)

        return [uncommon_word for uncommon_word in dictionary_solution if dictionary_solution[uncommon_word]==1]
        

frog = "Hello there Im mister frog hello"
apple = "Hello there Im mister apple hello"
a = ''