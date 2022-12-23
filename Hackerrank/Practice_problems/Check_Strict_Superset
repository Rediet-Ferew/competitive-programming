# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(input().split(" "))
n = int(input())
isSuperscript = False

#checking if the set is in A, then comparing their length
def isSuperScript():
    for i in range(n):
        sub_set = set(input().split(" "))
        
        if sub_set.issubset(set_A):
            
            if len(set_A) > len(sub_set):
                isSuperscript = True
                
            else:
                isSuperscript = False
                print(isSuperscript)
                return
                
        else:
            isSuperscript = False
            print(isSuperscript)
            return

    print(isSuperscript)
isSuperScript()
