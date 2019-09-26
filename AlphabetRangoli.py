def print_rangoli(size):
    # your code goes here
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    p = 2*size-1

    
    for i in range(p//2+1):
        j=i
        x = size -1
        st = a[x]
        while(j>0):
            st+='-'
            x=x-1
            st+=a[x]
            j=j-1
            
            

        while(j<i):
            st+='-'
            x=x+1
            st+=a[x]
            j=j+1


        print(st.center(4*size-3,'-'))
    

    for i in range(p//2-1,-1,-1):
        j=i
        x = size -1
        st = a[x]
        while(j>0):
            st+='-'
            x=x-1
            st+=a[x]
            j=j-1
            
            

        while(j<i):
            st+='-'
            x=x+1
            st+=a[x]
            j=j+1


        print(st.center(4*size-3,'-'))
    


