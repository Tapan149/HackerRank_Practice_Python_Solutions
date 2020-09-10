def swap_case(s):
    l =[]
    str1 = ''
    for i in s:
        if i.isupper():

            l.append(i.lower())
        elif i.islower():
            l.append(i.upper())
        else:
            l.append(i)
    return (str1.join(l))
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)