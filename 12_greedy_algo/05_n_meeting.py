start = [1, 3, 0, 5, 8, 5] 
end =  [2, 4, 6, 7, 9, 9]

def maximumMeetings(start, end):
    n = len(start)
    meetings = [(start[i], end[i], i) for i in range(0, n)]
    meetings.sort(key=lambda meeting:(meeting[1], meeting[0]))
    count = 1
    lastTime = meetings[0][1]
    for i in range(1, n):
        if lastTime < meetings[i][0]:
            count += 1
            lastTime = meetings[i][1]
    return count

print(maximumMeetings(start, end))