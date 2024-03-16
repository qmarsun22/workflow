
def sequare_digits(n):
    myset = [1]
    while (n not in myset):
        print("doing n =", n)
        n =  sum( int(c) **2 for c in str(n) )
        if(n ==1):
            print("super number")
            return 
        myset.append(n)
        print(f" myset = {myset}")
        print("false")
        return

def sum_sequare(n):
    sum=0
    myset=[1]
    while (n not in myset or n !=1):
        for i in str(n):
            n= int(i)*int(i) + sum
            print(i)
        print(sum)
        if(sum == 1):
            return True
            myset.append(n)
        print(myset)

sequare_digits(23434)
sequare_digits(332)
