def print_formatted(number):
    # your code goes here
    b = len(bin(number))-2
    for i in range(1,number+1):
       
        

        print(str.rjust(str(i).format(i),b),str.rjust('{:o}'.format(i),b),str.rjust('{:X}'.format(i),b),str.rjust('{:b}'.format(i),b) )

