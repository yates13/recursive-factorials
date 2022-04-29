#! /usr/bin/env python

import sys
import re
from Bio.Seq import translate
from Bio.Seq import Seq


class Sort:
    def __init__(self, sampleID, date, phenotype, sequence):
        self.ID = sampleID
        self.date = date
        self.pheno = phenotype
        self.seq = sequence



def get_factorial_recur(n):
    if n == 1:
        return 1
    else:
        return n * get_factorial_recur(n-1)

def results(fasta_file, p, output, ln, n, blue, orange):
    """
    this scripts generates an out put file called results.txt that uses recurssion to check and input file for how many time the phenotype orange appears in a population
    
    ---------
    Arguments:
        In:
            fasta_file = the first user input
            p = the second user input 
            output = third user input 
            ln = starts at zero and is used as a line number counter
            n = starts at zero and is used for factorials
            blue = an empty list for the blue phenotype
            orange = an empty list for the orange phenotype
        Out:
            output = results.txt which will contain the print statements needed to determine the number of orange phenotypes found 
    --------
    Example:
        Results
    
        p (the frequency of "orange" in the population) = 0.3
        n (the number of sampled individuals) = 100
        k (the number of "orange" individuals in the sample set) = 26

        Probability of collecting 32 individuals with 5 being "orange" (given a population frequency of 0.3) = 0.06126913528290234

    """

    print('Opening' + fasta_file)
    with open(fasta_file, 'r') as in_stream:
        print('opening' + output)
        with open(output, 'w') as out_stream:


            for line in in_stream:
                ln = ln + 1

                if  re.match('>',line):
                    n = n + 1
                    ls = re.split('_|\ |>', line)
                    sampleID = ls[1]
                    date = ls[2]


                else:
                    sequence = line
                    ps = translate(line)
                    if ps[3] == 'R':
                        phenotype = "orange"
                        orange.append(sampleID)
                    if ps[3] == 'S':
                        phenotype = "blue"
                        blue.append(sampleID)
                    globals()[f"{sampleID}_Aubie"] = Sort(sampleID, date, phenotype, sequence)

            q = 1-p
            k = len(orange)
            bern = (get_factorial_recur(n)/(get_factorial_recur(n-k)*get_factorial_recur(k)))*((p**k)*(q**(n-k)))

        #closing the opened files from earlier
            out_stream.write("Results\n\np (the frequency of \"orange\" in the population) = " + str(p))
            out_stream.write("\nn (the number of sampled individuals) = " + str(n))
            out_stream.write("\nk (the number of \"orange\" individuals in the sample set) = " + str(k))
            out_stream.write("\n\nProbability of collecting 32 individuals with 5 being \"orange\" (given a population frequency of 0.3) = " + str(bern) + "\n")

    print("Done!")
    print(sys.argv[1] + ' is closed?', in_stream.closed)
    print(sys.argv[3] + ' is closed?', out_stream.closed)

if __name__ == '__main__':
    fasta_file = (sys.argv[1]) 
    p = float(sys.argv[2])
    output = (sys.argv[3])
    ln = 0
    n = 0
    blue = []
    orange = []
    results(fasta_file, p, output, ln, n, blue, orange)
