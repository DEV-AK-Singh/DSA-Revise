a = 10
b = 7
ans = a ^ b
count = 0

for i in range(0, 32): # O(32) -> S(1)
    if ans & (1<<i) != 0:
        count += 1
print(count)

# while ans > 0: # O(logN) -> S(1)
#     if ans % 2 == 1:
#         count += 1
#     ans = ans // 2
# print(count)