answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").replace("-","").replace(" ","").lower()

if "42" == answer or "fortytwo" == answer:
    print("Yes")
else:
    print("No")