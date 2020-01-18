import sys
if sorted(sys.argv[1]) == sorted(sys.argv[2]):
    print("Is anagram")
else:
    print("Not anagram")
