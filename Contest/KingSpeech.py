lines = int(input())

for i in range(lines):
    sttuter = ""
    word = input()
    sttuter += (word[:2] + "... " + word + "?")
    print(sttuter)
