def times():
    print('Enter two numbers')
    f = input("Enter first number ... ")
    nf = int(f)
    s = input('Enter second number ... ')
    ns = int(s)

    result = nf*ns
    print (nf,"times", ns, "=", result)
    return
    

def main():
    times()
    
    print("Job Done")
    
main()