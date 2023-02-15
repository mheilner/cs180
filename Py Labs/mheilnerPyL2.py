import json
import string
import argparse
import os

def main(inputString):
    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"
    lst = inputString.strip().split()
    dict = {}
    for l in lst:
        l = l.translate(str.maketrans('', '', string.punctuation)).lower()
        if l in dict.keys():
            dict[l] = dict[l]+1
        else:
            dict.update({l:1})
    with open('word-count.json', 'w') as f:
        json.dump(dict, f, indent=0)
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)
    