import argparse
import numpy as np

def main(documentsTxt):
    # Write the code to compute the One Hot Encodings for various "documents"
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    wList = documentsTxt.split()
    uList = []
    for w in wList:
        if w.lower() not in uList:
            uList.append(w.lower())
    uList.sort()
    
    lns = documentsTxt.split('\n')
    final = np.zeros([len(lns), len(uList)],dtype=int)
    for r in range(len(lns)):
        ln = lns[r].split()
        arr = []
        for c in uList:
            count = 0
            for check in ln:
                if(c.lower()==check.lower()):
                    count += 1
            arr.append(count)
        final[r] = arr

        
    
    # print(documentsTxt)
    # print(uList)
    # np.zeros((len(lns), len(uList)))
    # for r in range(len(final)):
    #     line = lns[r].split()
    #     for c in range(len(final[r])):
    #         final[r][c] = int(final[r][c])
    #         for check in line:
    #             if(uList[c] == check):
    #                 final[r][c] += 1
    
    
    print('# Features: ')
    print(final)


    
    
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())