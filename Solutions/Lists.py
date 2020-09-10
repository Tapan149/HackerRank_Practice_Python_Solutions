if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(0,N):
        cmds=input().split()
        if cmds[0] == 'insert':
            L.insert(int(cmds[1]), int(cmds[2]))
        elif cmds[0] == 'print':
            print(L)
        elif cmds[0] == 'remove':
            L.remove(int(cmds[1]))
        elif cmds[0] == 'append':
            L.append(int(cmds[1]))
        elif cmds[0] == 'sort':
            L.sort()
        elif cmds[0] == 'pop':
            L.pop()
        elif cmds[0] == 'reverse':
            L.reverse()
