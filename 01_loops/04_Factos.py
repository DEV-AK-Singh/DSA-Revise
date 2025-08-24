num = 20 

# for i in range(1, num+1):
#     if num % i == 0:
#         print(i, end=", ")
 
# for i in range(1, num//2+1):
#     if num % i == 0:
#         print(i, end=", ")
# print(num)

results = []
for i in range(1, int(pow(num, 0.5)) + 1):
    if num % i == 0:
        results.append(int(i))
        if i != num/i:
            results.append(int(num/i))
print(sorted(results))