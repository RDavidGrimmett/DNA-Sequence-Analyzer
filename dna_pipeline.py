#this is dna_pipeline.py
#Python-based bioinformatics pipeline by using reusable functions and Python libraries like pandas or NumPy.


#Imported libraries
import pandas as pd

#Variable to hold the target .fasta file
target_file = "sequences.fasta"

#Created the dictionary to hold file contents
genes_and_sequences = {}

#Reads DNA sequences from a provided FASTA file 
def load_data():

    #Open the target .fasta
    with open (target_file, "r") as file:
        
        #Created the key and value variables for the dictionary
        gene_name = ""
        sequence = ""
        
        for line in file:
            #Creating a loop for each line in the open file
            line = line.strip()

            #Using ">" to target the gene name
            if line.startswith(">"):
                #Save previous gene
                if gene_name:
                    genes_and_sequences[gene_name] = sequence

                #Starts new gene
                gene_name = line[1:]
                sequence = ""
            
            else:
                #Add the sequence to the current gene
                sequence += line

        #Captures last gene
        if gene_name:
            genes_and_sequences[gene_name] = sequence
    

#Filters the sequences keeping only sequences longer than 100 nucleotides
def filter_sequences():
    #Iterates through the dictionary removing sequences that are <= 100 nucleotides long
    for gene_name, sequence in list(genes_and_sequences.items()):
        if len(sequence) <= 100:
            del genes_and_sequences[gene_name]


#Calculates the GC-content of a each sequence
def get_gc_content(gene_name, sequence):
    #counts "G" and "C" in the sequence and calculates the percentage
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count / len(sequence)) * 100

    return gc_percentage

    
#Generates a summary table or dataframe (use pandas) and saves it to sequence_summary.csv.
def summary_and_saving_results():
    #setting up the data dictionary to hold the summary information
    data = {'sequence ID': [], 'length': [], 'GC-content': []}
    #adding sequence ID, length, and GC-content for each gene
    data['sequence ID'] = list(genes_and_sequences.keys())
    data['length'] = [len(seq) for seq in genes_and_sequences.values()]
    data['GC-content'] = [get_gc_content(gene_name, sequence) for gene_name, sequence in genes_and_sequences.items()]
    #creating a pandas dataframe and saving it to a CSV file
    df = pd.DataFrame(data)
    df.to_csv("sequence_summary.csv", index=False)

#running the pipeline functions in order
if __name__ == "__main__":
    load_data()
    filter_sequences()
    summary_and_saving_results()