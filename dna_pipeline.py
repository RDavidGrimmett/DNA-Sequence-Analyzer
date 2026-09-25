#this is dna_pipeline.py
#Python-based bioinformatics pipeline by using reusable functions and Python libraries like pandas or NumPy.


#imported libraries
import pandas as pd
#import NumPy

target_file = "sequences.fasta"

#created the dictionary to hold file contents
genes_and_sequences = {}

#Create a function to read DNA sequences from a provided FASTA file
    #(/home/rbif/week5/sequences.fasta) into a Python data structure. 
#You may use a list or dictionary to store your data clearly.
def load_data():

    #open the target .fasta
    with open (target_file, "r") as file:
        
        #created the key and value variables for the dictionary
        gene_name = ""
        sequence = ""
        
        for line in file:
            #creating a loop for each line in the open file
            line = line.strip()

            #using ">" to target the gene name
            if line.startswith(">"):
                #save previous gene
                if gene_name:
                    genes_and_sequences[gene_name] = sequence

                #starts new gene
                gene_name = line[1:]
                sequence = ""
            
            else:
                #add the sequence to the current gene
                sequence += line

        #used to capture last gene
        if gene_name:
            genes_and_sequences[gene_name] = sequence
    
    print(genes_and_sequences)


#implement a function to filter the sequences, 
    #keeping only those sequences longer than 100 nucleotides.
def filter_sequences():
    for gene_name, sequence in list(genes_and_sequences.items()):
        if len(sequence) <= 100:
            del genes_and_sequences[gene_name]

    print(genes_and_sequences)

#write a function to calculate the GC-content 
    #(percentage of nucleotides that are either G or C) for each sequence.
def get_gc_content():
    for gene_name, sequence in genes_and_sequences.items():
        gc_count = sequence.count("G") + sequence.count("C")
        gc_percentage = (gc_count / len(sequence)) * 100
        print(f"{gene_name}: GC-content = {gc_percentage:.2f}%")

    
#Write a function that generates a summary table or dataframe (use pandas)
    #showing the sequence ID, length, and GC-content for each filtered sequence.
    #Save the summary table into a CSV file named sequence_summary.csv.
def summary_and_saving_results():
    data = {'sequence ID': [], 'length': [], 'GC-content': []}

    data['sequence ID'] = list(genes_and_sequences.keys())
    data['length'] = [len(seq) for seq in genes_and_sequences.values()]
    data['GC-content'] = [get_gc_content(gene_name, seq) for gene_name, seq in genes_and_sequences.items()]

    df = pd.DataFrame(data)
    df.to_csv("sequence_summary.csv", index=False)

#Your script should clearly indicate the order of steps (pipeline) 
    #by calling these functions sequentially in a main function or
    #a clearly structured code block (if __name__ == "__main__":).


if __name__ == "__main__":
    load_data()
    filter_sequences()
    get_gc_content()
    summary_and_saving_results()