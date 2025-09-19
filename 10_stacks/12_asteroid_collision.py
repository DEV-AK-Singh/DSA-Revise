asteroids = [8,-8, -8]

def asteroidCollision(asteroids):
    stack = []
    for asteroid in asteroids:
        if asteroid >= 0:
            stack.append(asteroid)
        else:
            while len(stack) != 0 and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            if len(stack) != 0 and stack[-1] == abs(asteroid):
                stack.pop() 
            elif len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroid)
    return stack

print(asteroidCollision(asteroids))
