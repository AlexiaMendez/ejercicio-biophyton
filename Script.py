
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

filename = #dirección del archivo genbank en tu computador


def summarize_contents(filename):
        file = []
        file = os.path.split(filename)
        todo=[]
        records = list(SeqIO.parse(filename, "genbank"))
        print("File: ", file[1])
        print ("Path: ", file[0])
        print("Num_records = %i records" % len(records))
        print("Records:\n" )
        for seq_record in SeqIO.parse(filename, "genbank"):
                todo.append(seq_record.name)
                print("- ID:",seq_record.id)
                print("Name: ", seq_record.name)
                print("Description: ", seq_record.description, "\n")
#Aquí se llama a la función
summarize_contents(filename)
