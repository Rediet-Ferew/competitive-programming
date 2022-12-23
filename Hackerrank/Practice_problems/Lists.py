if __name__ == '__main__':
    N = int(input())
    list_ = []
    #mapping the string function names to functions onto the list
    commands  = {"insert" : list_.insert, "pop":list_.pop,                  "print":print,"remove": list_.remove, "append": list_.append,         "sort": list_.sort, "reverse": list_.reverse}
    
    for i in range(N):
        
        com = input()
        com = com.split(" ")
        k = com[0]
        
        if len(com) == 1:
            if k == 'print':
                commands[k](list_)
                continue
            commands[k]()
        
        elif len(com) == 2:
            commands[k](int(com[1]))
        
        elif len(com) == 3:
            commands[k](int(com[1]), int(com[2]))
        
