
def Solve(stack):
    for i in range(len(stack)):
        temp = stack[i]
        if temp != 0 and temp != 1:
            stack[i] = temp // 2
            stack.insert(i + 1, temp % 2)
            stack.insert(i + 2, temp // 2)

            Solve(stack)
    return stack


def countOnes(stack, l, r):
    count = 0
    for i in range(l, r + 1):
        if stack[i] == 1:
            count += 1
    return count
if __name__ == '__main__':
    n, l, r = map(int, input("Enter three values\n").split(', '))
    # print("\nThe value of a is {}, b is {} and c is {}".format(a, b, c))
    stack = Solve([n])
    count = countOnes(stack, 1, r)
    print(count)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
