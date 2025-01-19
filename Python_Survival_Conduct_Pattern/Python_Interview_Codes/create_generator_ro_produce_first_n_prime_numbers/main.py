
def isprime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
        return True



def prime_generator(n):
    num = 2
    while n:
        if isprime(num):
            '''
            #yield keyword used to return a value and then the code
            is resumed inside the function unlike the return keyword end
            the code when it is called

            #yield keyword will turn any expression that is given with it
            into a generator objects and return it to the caller
            '''

            yield num
            n-=1

        n+=1


x  = int(input("Enter no. of prime numbers required : "))


it = prime_generator(x)

for e in it:
    print(e,  end=" ")
