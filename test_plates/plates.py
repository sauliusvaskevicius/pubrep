def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0987654321"
    num_pos = 6

    if 2<=len(s)<=6 :
#       print("#plate is correct length")
        for n in range(len(s)):
            if s[n] in cap_letters:
#               print("#its letter")
                if num_pos < n:
#                   print("#letter goes after number")
                    return False
            else :
                if s[n] in numbers :
#                   print("#its number")
                    if s[n]=="0" and num_pos==6:
#                       print("#its 0 and the first number in a plate")
                        return False
                    num_pos = n
                    if n<2 :
#                       print("its in the first two positions")
                        return False
                else:
#                   print("#its nor letter nor number")
                    return False
        return True
    else:
#       print("#plate is NOT correct length")
        return False


if __name__ == "__main__":
    main()
