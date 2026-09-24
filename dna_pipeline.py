#this is dna_pipeline.py
#first Python-based bioinformatics pipeline by using reusable functions and Python libraries like pandas or NumPy.

import pandas 
import NumPy

def data_loading():
    #Create a function to read DNA sequences from a provided FASTA file
    #(/home/rbif/week5/sequences.fasta) into a Python data structure. 
    #You may use a list or dictionary to store your data clearly.
    

def sequence_filtering():
    #implement a function to filter the sequences, 
    #keeping only those sequences longer than 100 nucleotides.

def analysis():
    #write a function to calculate the GC-content 
    #(percentage of nucleotides that are either G or C) for each sequence.

def summary_and_saving_results():
    #Write a function that generates a summary table or dataframe (use pandas)
    #showing the sequence ID, length, and GC-content for each filtered sequence.
    #Save the summary table into a CSV file named sequence_summary.csv.

#Your script should clearly indicate the order of steps (pipeline) 
#by calling these functions sequentially in a main function or
#a clearly structured code block (if __name__ == "__main__":).