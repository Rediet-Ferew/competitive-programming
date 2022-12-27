import textwrap

def wrap(string, max_width):
    n = len(string)
    wraps = len(string)//max_width
    left = 0
    ans = ""
    new_line = 0
    
    while left < wraps:
        ans += string[new_line:new_line+max_width]
        ans += "\n"
        left += 1
        new_line += max_width
        
    if new_line < len(string):
        ans+= string[new_line:]
        
    return ans        


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
