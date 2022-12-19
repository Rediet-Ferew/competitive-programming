def swap_case(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i].isalpha and s_list[i].isupper():
            s_list[i] = s_list[i].lower()
        elif s_list[i].isalpha and s_list[i].islower():
            s_list[i] = s_list[i].upper()
        else:
            continue
    return "".join(s_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
