# A05 - Number 2
This script imports the Chemdraw cdxml files and uses Open Babel to create a csv file.

## How to run the script
Clone the repository from GitHub and go to the correct directory.
```bash
git clone git@github.com:amare2004/ci2.git
cd ci2/A05
```
Create and activate a virtual environment and then install the required package from the file; requirements.txt
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Run the script
To run the script write.
```bash
python3 cdxml2csv.py "*.cdxml"
```

The script creates `cdxml2csv.csv` in the A05 folder and prints the filename and the number of active MACCS fingerprint bits for the input molecule with the highest count. The nine cdxml files included in the folder can be used to test the program.