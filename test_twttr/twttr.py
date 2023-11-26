def main():
    name=input("Input: ")
    print(f"Output: {shorten(name)}")

def shorten(word):
    output = ""
    for letter in word:
        if letter.lower() not in ["a","e","i","o","u"] :
            output += letter
    return output

if __name__ == "__main__":
    main()