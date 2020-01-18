try:
    f = open("p11b.txt", 'a+')
    s = input("What is your name? ")
    f.seek(0)
    print("Previous names:\n" + f.read())
    f.write(s+"\n")
finally:
    f.close()
