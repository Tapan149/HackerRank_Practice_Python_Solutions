def merge_the_tools(string, k):
    s=string
    for i in range(0, len(s)):
        s1=s[i*k:(i+1)*k]
        j=1
        while j<len(s1):
            s1=s1[0:j]+s1[j:].replace(s1[j-1],"")
            j+=1
        print(s1)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
------------------------------------------------------
-------------------------------------------------------


from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)