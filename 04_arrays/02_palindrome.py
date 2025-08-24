def palindrome(start, end, word):
    if start >= end:
        return True
    if word[start] != word[end]:
        return False
    return palindrome(start+1, end-1, word)

word = "moms"

print(palindrome(0, len(word)-1, word=word))