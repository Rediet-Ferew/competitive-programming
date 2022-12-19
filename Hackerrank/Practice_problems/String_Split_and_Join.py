def split_and_join(line):
    line_s = line.split(" ")
    return "-".join(line_s)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
