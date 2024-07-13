import sys

def main():
    string = sys.argv[1]

    res = sum(ord(char) for char in string)
    print(res)

if __name__ == "__main__":
    main()