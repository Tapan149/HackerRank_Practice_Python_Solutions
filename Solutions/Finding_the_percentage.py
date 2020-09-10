if __name__ == '__main__':
    N = int(input()) # input() takes the first line of input, int() converts from string to int
    dictionary = {} 
    for i in range(0, N):
        inputArray = input().split() # The inputs from 2nd line onwards gets splitted and stored in a list
        marks = list(map(float, inputArray[1:])) #This line converts indices 1->end of inputArray to floats, puts them in a list
        dictionary[inputArray[0]] = sum(marks)/float(len(marks)) # sum(marks) adds up everything in marks list
    print("%.2f" % dictionary[input()]) # print(output) formatted to 2 decimal places
