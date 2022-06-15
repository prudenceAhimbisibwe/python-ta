import sys
import os


def prime(s):
    # your code goes here
    for i in range(2,s):
        if i%s==0:
            return False
        else:
            return True
prime(2) 
   


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))



