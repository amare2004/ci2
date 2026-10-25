# A03 - number 2
This script reads a saved NIST WebBook search-results page and prints the names of the compounds listed in the results using Beautiful Soup. 

## How to run the script
Clone the repository from GitHub and go to the correct directionary.
```bash
git clone git@github.com:amare2004/ci2.git
cd ci2/A03
```
Create and activate a virtual environment and then install the required package from the file; requirements.txt
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```
## Run the script
```bash
python nist_parser.py nist_benzidine.html
```
The nist_benzidine.html file included in the folder can be used to test the program. If no file name is provided then a instruction message will be printed.