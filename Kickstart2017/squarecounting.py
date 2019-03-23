import sys

# Name of the test files
fileName = 'small'
# fileName = 'large'

# Type of question
question = 'A'

# Global Variables
results = []


def solve(R, C):
    A = R-1
    B = (R+1)
    E = R/12
    D = (2*C-R)

    num_squares = B*D*E*A
    return num_squares


if __name__ == "__main__":
    sys.stdin = open('Kickstart2017/%s-%s-practice.in' %
                     (question, fileName), 'r')

    # Take input
    cases = int(input())
    for i_ in range(cases):
        R, C = list(map(int, input().strip().split(' ')))
        results.append(solve(R, C))

    fp = open('Kickstart2017/%s-%s-practice.out' % (question, fileName), 'w')
    for i_, c in enumerate(results):
        fp.write('Case #%d: %d\n' % (i_+1, c))
