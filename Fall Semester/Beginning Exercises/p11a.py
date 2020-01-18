
try:
    f = open("p11a.txt", 'r')
    s = input("What is your name? ")
    f.seek(0)
    print("Last person's name: " + f.read())
finally:
    f.close()
try:
    f = open("p11a.txt", 'w')
    f.write(s)
finally:
    f.close()
