# num = 10
# count = 0
# def greet(num, count=0):
#     if count == num:
#         return
#     print("Abhishek")
#     count += 1
#     greet(num, count)
# greet(num, count=count)

# def func(x, n):
#     print(x)
#     if x == n:
#         return
#     func(x-1, n)
# func(11, 4)

def func1ton(n):
    if n==0:
        return
    func1ton(n-1)
    print(n)

func1ton(5)