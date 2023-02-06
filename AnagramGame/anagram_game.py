'''
Anagram Game
'''

import itertools
vowels = ['A', 'E', 'I', 'O', 'U']

def sliding_window(elements, window_size):
    '''
    Implement Sliding window to check custom anagram conditions
    '''
    
    if len(elements) <= window_size:
        return elements
    for i in range(len(elements)- window_size + 1):
        subst = (elements[i:i+window_size])
        if subst[0] in vowels and subst[1] in vowels:
            return
        if subst[0] not in vowels and subst[1] not in vowels:
            return
        
        return not None

def solution(S):
    '''
    Implement your solution here
    '''
      
    ans = []
    nums = list(S)
    permutations = list(itertools.permutations(nums))

    perm_list = [''.join(permutation) for permutation in permutations]
    print("All possible Anagrams: ", perm_list)
    for anag in  perm_list:
        if anag[0] in vowels:
            print("Removing Anagram as it didn't start with consonant: ", anag)
        elif sliding_window(anag, 2) is None:
            print("Removing Anagram as it has doubles:", anag)
        else:
            ans.append(anag)

    print(ans)
    return len(ans)

if __name__ == "__main__":
    print("count: ", solution("BAR"))
    print("count: ", solution("PARTY"))