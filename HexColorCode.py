import string

def hex(n):
    col = []
    for i in range(n):
        s = input()
        while ('#' in s):
            
            x=s.find('#')
           
            x=x+1
            s = s[x:]
            if (x==1):
                continue
            if (all(c in string.hexdigits for c in s[:3])):
                if all(c in string.hexdigits for c in s[:6]):
                    print("#"+s[:6])
                else:
                    print("#"+s[:3])
            # print(s)

if __name__ == '__main__':
    n = int(input())
    hex(n)