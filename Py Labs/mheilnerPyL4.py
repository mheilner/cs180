import argparse as ap

def main(array):
    # Write the compute the variance and the mean of a given list of numbers
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    # print(array)
    #Calculate the Mean
    mean = 0
    for n in array:
        mean += n
    mean /= len(array)
    #Calc the STDev
    std = 0 
    for n in array:
        std += (mean-n)**2
    std /= len(array)
    
    print(f'mean = {mean}')
    print(f'variance = {std}')
    return None

if __name__ == "__main__":
    argParse = ap.ArgumentParser("Variance and Mean Calculator")
    argParse.add_argument("--array", nargs="+", type=int, help="Input a list of numbers to compute the variance and mean of")
    parsedArgs = argParse.parse_args()
    main(parsedArgs.array)
