cube = lambda x:x**3   # complete the lambda function 

def fibonacci(n):
    i=2
    x1=0
    x2=1
    if n>1:
        
        l=[x1,x2] 
        while i<n:
            x3=x1+x2
            x1=x2
            x2=x3
            i+=1
            l.append(x3)
        return l

    if n==0:
        l=[]
        return l
    if n==1:
        l=[x1]
        return l
        
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
