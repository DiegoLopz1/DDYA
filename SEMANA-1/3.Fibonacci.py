def main():    
    n = int(input("Digite su número: "))
    a = 0
    b = 1
    fib = False
    while a <= n:
        print(a, end=" ")
        if a == n:
            fib = True
            
        a,b = b,a + b
    if fib:
        
        print(a,b, end=" ")
        print("su numero pertenece ")

    else:
        print(a,b, end=" ")
        print(" \n su numero no pertenece ")

main()


    
