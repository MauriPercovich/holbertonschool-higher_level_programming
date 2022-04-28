#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print(f"{argc}: {argv[argc]}")
    else:
        print(f"{argc} arguments:")
        for x in range(1, argc + 1):
            print(f"{x}: {argv[x]}")
