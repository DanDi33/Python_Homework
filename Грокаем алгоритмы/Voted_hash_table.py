voted = {"Tom": True, "Dan": True}


def check_voted(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote !")


check_voted("John")
check_voted("Tom")
print(voted)
