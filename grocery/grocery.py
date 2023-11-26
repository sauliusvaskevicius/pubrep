def main():
    items=[]
    count={}
    while True:
        try:
            items.append(input().upper())
        except EOFError:
            break
        else:
            continue
    sortedItems = sorted(items)
    for item in sortedItems:
        if item in count:
            count[item] += 1
        else:
            count[item]= 1

    for key,value in count.items():
        print(f"{value} {key}")

main()