import itertools


def getInputAndProcess():
    res = []
    test_cases = int(input())

    for i_ in range(test_cases):
        num_items_bag, redip_values = list(
            map(int, input().strip().split(' ')))
        valueList = list(map(int, input().strip().split(' ')))
        res.append(expectedValue(num_items_bag, redip_values, valueList))
    return res


def expectedValue(num_items_bag, redip_values, valueList):
    if redip_values == 0:
        return sum(valueList)/num_items_bag

    valueList.sort()
    accumulated = [0] + list(itertools.accumulate(valueList))
    p = 0

    element = [0]*(redip_values+1)
    element[0] = sum(valueList)/num_items_bag

    for i in range(1, redip_values+1):
        while p < num_items_bag and valueList[p] <= element[i-1]:
            p += 1
        element[i] = (accumulated[-1]-accumulated[p] +
                      element[i-1]*p)/num_items_bag

    return element[-1]


if __name__ == "__main__":

    res = []
    res = getInputAndProcess()

    for i_, c in enumerate(res):
        print('Case #%d: %.7f\n' % (i_+1, c))
