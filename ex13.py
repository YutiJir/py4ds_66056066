def calculateSum(input):
    count = 0
    for i in input:
        count = count + i

    return count


def calculateProduct(input):
    count = 1
    for i in input:
        count = count * i

    return count


def average(input):
    count = 0
    for i in input:
        count = count + i

    return count / len(input)


def median(input):
    count = input
    n = len(count)
    count.sort()

    if n == 0:
        return None
    elif n % 2 == 0:
        med = n // 2
        return (count[med] + count[med - 1]) / 2
    else:
        med = n // 2
        return count[med]


def mode(input):
    if len(input) == 0:
        return None

    max_count = 0
    mlist = []
    index = 0

    while index < len(input):
        num = input[index]
        count = input.count(num)
        if count > max_count:
            max_count = count
            mlist = [num]
        elif count == max_count:
            mlist.append(num)

    return mlist


if __name__ == '__main__':
    # calculateSum
    print(calculateSum([]) == 0)
    print(calculateSum([2, 4, 6, 8, 10]) == 30)
    print(calculateSum([1, 3, 5, 7, 9]) == 25)

    # calculateProduct
    print(calculateProduct([]) == 1)
    print(calculateProduct([2, 4, 6, 8, 10]) == 3840)

    # calculatrAverage
    print(average([1, 2, 3]) == 2)
    print(average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2)
    print(average([12, 20, 37]) == 23)
    print(average([0, 0, 0, 0, 0]) == 0)

    # calculateMedian(
    print(median([]) == None)
    print(median([1, 2, 3]) == 2)
    print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5)
    print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6)

    # calculateMode
    print(mode([]) == None)
    print(mode([1, 2, 3, 4, 4]) == 4)
    print(mode([1, 1, 2, 3, 4]) == 1)
