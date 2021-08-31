import argparse, os, docx
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("example_doc")
parser.add_argument("output_path")
parser.add_argument("fn_range")
args = parser.parse_args()


doc = docx.Document(args.example_doc)
table = doc.tables[0]
print(table)


## TODO: create new docx file with fn_range number of tables
## TODO: add footnote numbers in first cell of each table
## TODO: keep one empty table at the end
