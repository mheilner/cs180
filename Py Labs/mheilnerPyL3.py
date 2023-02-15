import argparse
import numpy
import os
import math

def main(number: int):
    # Write the code to sum up cubed numbers here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    # def cube(number):
        sum = 0
        if number <=1 :
            return 0
        for n in range(2,number+1):
            dig = n**3
            while dig//10 > 0:
                dig = dig // 10
            if dig % 2 == 0:
                sum += n*n*n
        print(f'cube({number}) = {sum}')
        # return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    main(arguments.n)