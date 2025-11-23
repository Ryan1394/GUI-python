import re
import sys

def main():
    print(validate(input("IPv4 address : ")))

def validate(iP):
    try:
        a,b,c,d = iP.split(".")
        if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255:
            return False
        elif re.search(r"^\d+\.{1}^\d+\.{1}^\d+\.{1}^\d+$",iP):
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()