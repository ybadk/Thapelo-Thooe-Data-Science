# globals function returns dictionary
# You can use the globals() function to access or modify global variables
#within a functon code block

x = 5 #global variable


def fun():
    x = 10 #local function
    d = globals() #d is a dictionary
    #d['x'] = 15 # x is the key in dictionary d which assigns value to global varible
    print("local x=%d global x=%d"%(x,d['x']))



fun()
