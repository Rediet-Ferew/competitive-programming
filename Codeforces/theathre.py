def theatreSquare(lines):
    n = lines[0]
    m = lines[1]

    if lines[0] %lines[-1] == 0:
        width = lines[0]//lines[-1]
    if lines[1] %lines[-1] ==0:
        height = lines[1]//lines[-1]
    if lines[0] %lines[-1] !=0:
        width = lines[0]//lines[-1] + 1
    if lines[1] %lines[-1] !=0:
        height = lines[1]//lines[-1] + 1
    flagstone = width * height
    print(flagstone)
    
lines=list(map(int, input().rstrip().split()))
theatreSquare(lines)