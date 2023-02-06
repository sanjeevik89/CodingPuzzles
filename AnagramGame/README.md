
# A simple Anagram Game

For a given input String, return the no of anagrams that meets the below conditions.

## Conditions:
    1. Anagrams cannot start with a consonant.
    2. Two vowels can't be next to each other in an Anagram.
    3. Two consonants can't be next to each other in an Anagram.

## Example:

Input : "BAR"  
Output: 2

Log:
```
All possible Anagrams:  ['BAR', 'BRA', 'ABR', 'ARB', 'RBA', 'RAB']
Removing Anagram as it has doubles: BRA
Removing Anagram as it didn't start with consonant:  ABR
Removing Anagram as it didn't start with consonant:  ARB
Removing Anagram as it has doubles: RBA
['BAR', 'RAB']
count:  2
```