memory = 1000
used = {}

while True:
    print("\n1.Allocate  2.Free  3.Display  4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        p = input("Process ID: ")
        s = int(input("Size: "))
        if s > 0 and s <= memory:
            used[p] = s
            memory -= s
            print("Allocated!")
        else:
            print("Not enough memory!")

    elif ch == "2":
        p = input("Process ID: ")
        if p in used:
            memory += used.pop(p)
            print("Memory freed!")
        else:
            print("Process not found!")

    elif ch == "3":
        print("Free memory:", memory, "KB")
        print("Used memory:", 1000 - memory, "KB")
        print("Processes:", used)

    elif ch == "4":
        break
