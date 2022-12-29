test_cases = int(input())

def compareSize(a, b):
    label_size = {
        'S' : -1,
        'M' : 1,
        'L' : 3
    }

    label_a = label_size[a[-1]]
    label_b = label_size[b[-1]]

    if label_a != label_b:
        
        if label_a > label_b:
            print('>')
        elif label_a < label_b:
            print('<')
        else:
            print('=')
            
    else:
        if len(a) == len(b):
            print('=')
            return
        
        x_in_a = len(a) - 1
        x_in_b = len(b) - 1
        
        if (label_a * x_in_a) < (label_b * x_in_b):
            print('<')
        else:
            print('>')
            
for _ in range(test_cases):
    a, b = list(input().split(' '))
    compareSize(a, b)
