def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        s = string[i:(i+k)]
        s = ''.join(sorted(set(s), key=s.index))
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)