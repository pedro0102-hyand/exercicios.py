while True:
    try:
        n=int(input())
        if n==0:
            print("Vai ter copa")
        else:
            print("Vai ter duas")
    except EOFError:
        break
