def square(a, sym, full=False):
    sym = sym[0]
    if not full:
        for i in range(a):
            for j in range(a):
                if i == 0 or j == 0 or i == (a - 1) or j == (a - 1):
                    print(sym, end="  ")
                else:
                    print("   ", end="")
            print()
    else:
        for i in range(a):
            for j in range(a):
                print(sym, end="  ")
            print()


square(14, "*v", True)
