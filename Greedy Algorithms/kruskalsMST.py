# Picking smallest weight edge that does not form a cycle


def kruskalsMST(startTime, FinishTime):
    n = len(FinishTime)

    iterator = 0
    print("The Value of iterator is: ", iterator)

    for another_iterator in range(n):
        if startTime[another_iterator] >= FinishTime[iterator]:
            print(another_iterator)
            iterator = another_iterator


if __name__ == "__main__":
    startTimeArray = [1, 4, 8, 3, 3, 2]
    FinishTimeArray = [5, 7, 0, 9, 9, 6]

    kruskalsMST(startTimeArray, FinishTimeArray)
