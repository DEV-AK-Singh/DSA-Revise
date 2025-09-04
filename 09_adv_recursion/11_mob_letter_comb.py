key_dict = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

digits = "462"
results = [] 

def backtrack(index, subset):
    if index >= len(digits):
        results.append("".join(subset.copy()))
        return
    digit = digits[index]
    letters = key_dict[digit]
    for i in range(0, len(letters)):
        subset.append(letters[i])
        backtrack(index+1, subset)
        subset.pop()

backtrack(0, [])

print(results)
