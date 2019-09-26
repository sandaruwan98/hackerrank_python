# Enter your code here. Read input from STDIN. Print output to STDOUT
# if __name__== '__main__':
s = input()
s = s.split()
s = [int(i) for i in s]
n,m=s[0],s[1]
c ='.|.'
for i in range(1,(n//2+1)):
    print((c*(2*i-1)).center(m,'-'))

print('WELCOME'.center(m,'-'))

# for j in range((n//2+1),1):
#     print((c*(2*j-1)).center(m,'-'))

for i in range(1,(n//2+1)):
    j = (n//2+1)-i
    print((c*(2*j-1)).center(m,'-'))
