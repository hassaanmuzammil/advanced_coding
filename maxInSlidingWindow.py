from collections import deque

def max_sliding_window(sequence, m):
    q = deque()
    maximums = []
    for i in range(m):
        while q and sequence[i] >= sequence[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(m, len(sequence)):
        maximums.append(sequence[q[0]])
        while q and q[0] <= i-m:
            q.popleft()
        while q and sequence[i] >= sequence[q[-1]]:
            q.pop()
        q.append(i)
    maximums.append(sequence[q[0]])
    return maximums
    
def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums
  
max_sliding_window([9,3,10,7,4,5,6,9,1,2,13],4)
max_sliding_window_naive([9,3,10,7,4,5,6,9,1,2,13],4)

#returns [10, 10, 10, 7, 9, 9, 9, 13]
