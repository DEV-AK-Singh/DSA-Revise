# brute -> O(n2) - S(n)
# def lengthOfLongestSubstring(word):
#     n = len(word)
#     max_length = 0
#     for i in range(0, n):
#         letters = set()
#         length = 0
#         for j in range(i, n):
#             if word[j] not in letters:
#                 letters.add(word[j])
#                 length += 1
#                 max_length = max(length, max_length)
#             else:
#                 break
#     return max_length

# optimal
def lengthOfLongestSubstring(word):
    n = len(word)
    max_length = 0
    length = 0
    l = 0 
    r = 0
    letters_dict = dict()
    while r < n:
        if word[r] in letters_dict:
            l = max(l, letters_dict[word[r]]+1)   
        letters_dict[word[r]] = r
        max_length = max(r-l+1, max_length)
        r += 1
    return max_length

print(lengthOfLongestSubstring("pwwkew"))

