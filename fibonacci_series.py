
def fibonacci_series(num):
    x=0
    print(x)
    y=1
    print(y)
    for a in range(num-2):
        temp=y
        y=x+y
        x = temp
        print(y)
        # yield x12

num=int(input("enter a number :"))
fibonacci_series(num)

    
    