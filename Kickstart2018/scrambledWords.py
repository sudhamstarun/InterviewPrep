# solving this to device a common format to solve the questions

# Import required to required libraries here
import sys

# Name of the test files
fileName = 'small'
#fileName = 'large'

# Type of question
question = 'C'

# Global Variables
results = []


def solve(s1, s2, A, B, C, D, N, a, n):
    s = ['']*N
    s[0], s[1] = s1, s2
    x = [0]*N

    x[0], x[1] = ord(s1), ord(s2)

    for i in range(2, N):
        x[i] = (A*x[i-1]+B*x[i-2]+C) % D
        s[i] = chr(97+x[i] % 26)

    s = ''.join(s)

    ret = 0

    for substring in a:
        for i in range(len(s)-len(ss)+1):
            st = s[i:i+len(ss)]
            if st[0] == ss[0] and st[-1] == ss[-1] and (len(ss) <= 2 or sorted(ss[1:-1]) == sorted(st[1:-1])):
                ret += 1
                break
    return ret


sys.stdin = open('%s-%s-practice.txt' % (question, fileName), 'r')
cases = int(input())
for i_ in range(cases):
    n = int(input())
    a = input().strip().split(' ')
    b = input().strip().split(' ')
    s1, s2, N, A, B, C, D = b[0], b[1], int(b[2]), int(
        b[3]), int(b[4]), int(b[5]), int(b[6])
    res.append(slove(a, n, s1, s2, N, A, B, C, D))

fp = open('%s-%s-practice.out' % (question, fileName), 'w')
for i_, c in enumerate(res):
    fp.write('Case #%d: %d\n' % (i_+1, c))
