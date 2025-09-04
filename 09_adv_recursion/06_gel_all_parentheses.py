# n = 2
# brackets = [""]*(n*2)
# results = []
# total = 0

# def backtracing(index, total, brackets):
#     if index >= len(brackets):
#         if total == 0:
#             results.append("".join(brackets))
#         return
#     if total > n or total < 0:
#         return
#     brackets[index] = "("
#     backtracing(index+1, total+1, brackets)
#     brackets[index] = ")"
#     backtracing(index+1, total-1, brackets)

# backtracing(0, 0, brackets)

# print(results)

# ----------------------------

n = 3
brackets = ""
results = []
total = 0

def backtracing(index, total, brackets): 
    if index >= n*2:
        if total == 0:
            results.append(brackets)
        return
    if total > n or total < 0:
        return   
    backtracing(index+1, total+1, brackets+"(")  
    backtracing(index+1, total-1, brackets+")")

backtracing(0, 0, brackets)

print(results)