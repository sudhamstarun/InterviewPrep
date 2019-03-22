def getInput():
    test_cases = int(input())
    counter = 0
    input_line_one = []
    input_line_two = []
    num_items_bag = []
    redip_values = []
    valueList = [[]]

    while counter < test_cases:
        input_line_one = int(input())
        num_items_bag.append(input_line_one[0])
        redip_values.append(input_line_one[1])
        input_line_two = int(input())
        valueList[counter].append(input_line_two)
        counter += 1

    return num_items_bag, redip_values, valueList
