#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            result += int(i)
        print(result)
    else:
        print('0')
