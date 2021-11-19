#!/usr/bin/python3

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
    except getopt.GetoptError:
        print ('03_arguments.py -i <inputfile> -o <outputfile>')
        sys.exit()

    for opt, arg in opts:
        if opt == "-h":
            print ('03_arguments.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    
    if not inputfile or not outputfile:
        print ('03_arguments.py -i <inputfile> -o <outputfile>')
        sys.exit()
    else:
        print("Input file is: ", inputfile)
        print("Output file is: ", outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])