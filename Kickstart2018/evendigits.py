def getInput():
    test_cases = int(input())
    counter = 0
    input_numbers = []

    while counter < test_cases:
        input_numbers.append(input())
        counter += 1

    return input_numbers


def checkIfOddDigitPresent(number):
    for digit in str(number):
        if int(digit) % 2 != 0:
            return True


def minimum_press(number):
    minus_presses = 0
    add_presses = 0
    new_value_minus = int(number)
    new_value_add = int(number)

    while checkIfOddDigitPresent(new_value_minus):
        new_value_minus = new_value_minus - 1
        minus_presses += 1

    while checkIfOddDigitPresent(new_value_add):
        new_value_add = new_value_add + 1
        add_presses += 1

    return min(minus_presses, add_presses)


def smallDataset():
    input = getInput()
    counter = 1
    for number in input:
        print("Case #"+"{}".format(counter) +
              "{}".format(":"), minimum_press(number))
        counter += 1
