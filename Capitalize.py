
# Complete the solve function below.
def solve(s):
    s = s.split(' ')
    for i in range(len(s)):
        # if(s[i][0].isalpha()):
        s[i]= s[i].capitalize()
    # s[1]= s[1].capitalize()
    print(s)
    s = ' '.join(s)
    return s

