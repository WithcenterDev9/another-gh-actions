import os
import sys

def main():
    sum1 = int(sys.argv[1])
    sum2 = int(sys.argv[2])
    result = sum1 + sum2
    print(f"result={result}")
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f"result={result}", file=fh)

if __name__ == "__main__":
    main()