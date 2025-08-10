print("Welcome to your to-do list application")
t = {}

print("How many to-do lists do you want to create?")
n = int(input())

for a in range(1, n + 1):
    print("Give a to-do list")
    t[a] = input()
    print("Your to-do list has been created")

i = 0
while i == 0:    
    print("If you want to add a to-do list, type 1")
    print("If you want to see your to-do list, type 2")
    print("If you want to remove tasks from to-do list, type 3")
    op = int(input())

    if op == 1:
        c = len(t)
        print("How many to-do lists do you want to add to the list?")
        n = int(input())
        print("So, you want to add", n, "to-do lists")
        n = n + c
        for a in range(c + 1, n + 1):
            print("Give a to-do list")
            l = input()
            t[a] = l
        print("Your to-do list's has been added")
        print(t)

    if op == 2:
        print("Do you want to see your to-do list")
        print("1 for Yes and 0 for No")
        a = int(input())
        if a == 1:
            for e in t:
                print(t[e])
        else:
            print("Okay")
            print("EOP")

    if op == 3:
        print("Do you want to delete some of your to-do's")
        print("1 for Yes and 0 for No")
        o = int(input())
        if o == 1:
            for key, value in t.items():
                print(f"{key}: {value}")
            print("Which one do you want to delete?")
            b = int(input())
            del t[b]
            print("Your new to-do list")
            for key, value in t.items():
                print(f"{key}: {value}")
        else:
            print("Okay")
            print("EOP")

    print("Do you want to continue using this application?")
    print("For Yes, type 0 and for No, type 1")
    i = int(input())
