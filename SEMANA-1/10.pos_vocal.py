def main():
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    n=input("digite una letra del abecedario")
    x=0
    for rep in a:
        x+=1
        if rep == n:
            print("esta en la posicion", x)
main()