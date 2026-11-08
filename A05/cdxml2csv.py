import csv
import glob
import sys
from pathlib import Path

from openbabel import pybel


def convert_cdxml(arguments):
    output_path = Path("cdxml2csv.csv") #default output file

    for argument in arguments: # check if any argument is a .csv file that does not exist yet
        candidate = Path(argument)
        if candidate.suffix.lower() == ".csv" and not candidate.exists():
            output_path = candidate
            break

    # Find CDXML files matching each input argument or file pattern.
    input_files = []
    for argument in arguments:
        if Path(argument).suffix.lower() == ".csv": #check if the argument is a .csv file, if so skip it
            continue
        input_files.extend( #search for .cdxml files in the argument path and add them to the input_files list
            Path(match)
            for match in glob.glob(argument)
            if Path(match).suffix.lower() == ".cdxml"
        )

    input_files = sorted(set(input_files)) #remove duplicates and sort the list of input files
    if not input_files:
        raise SystemExit("No .cdxml files found.")

    # Each row will contain the filename, its SMILES string, and its MACCS bits.
    rows = []
    for filename in input_files:
        molecule = next(pybel.readfile("cdxml", str(filename)), None) # read the molecule from the .cdxml file
        if molecule is None: # if no molecule is found, raise an error
            raise ValueError(f"No molecule found in {filename}")

        
        smiles_text = molecule.write("smi").strip() # Convert the molecule to SMILES and remove surrounding whitespace.
        if not smiles_text:
            raise ValueError(f"Could not generate SMILES for {filename}")

        smiles = smiles_text.split()[0]
        
        maccs_bits = molecule.calcfp("maccs").bits # Calculate the MACCS fingerprint and keep its active bit indices.
        rows.append((filename.name, smiles, maccs_bits))

    with output_path.open("w", newline="", encoding="utf-8") as csv_file: #write the rows to the output CSV file
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(("name", "smiles", "maccs"))
        writer.writerows(rows)

    most_complex = max(rows, key=lambda row: len(row[2])) #find the row with the most complex molecule based on the length of the maccs fingerprint
    
    print(f"{most_complex[0]} {len(most_complex[2])}") # Print the filename and count of active MACCS bits for the selected molecule.

if __name__ == "__main__": # if the script is run directly, call the convert_cdxml function with command line arguments
    convert_cdxml(sys.argv[1:])