if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    if a and b > 1:
        def sum(x,y):
        
            c = x + y
            return c
        def sub(x,y):
            c = x - y
            return c
        def mul(x,y):
            c = x*y
            return c
        print(sum(a,b))
        print(sub(a,b))
        print(mul(a,b))
