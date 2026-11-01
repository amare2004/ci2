# A04 - Number 10
This script imports the World database CSV files into an SQLite database and lists the countries where French is an official language.

The script uses Python's standard library. No additional Python packages are required. The `requirements.txt` file is therefore empty.

## How to run the script
Clone the repository from GitHub and go to the correct directory.
```bash
git clone git@github.com:amare2004/ci2.git
cd ci2/A04
python3 -m pip install -r requirements.txt
```
Make sure that the CSV files are in the folder.

## Run the script
To run the script for the first time, then you need to import the CSV files like this:
```bash
python3 db.py country.csv city.csv countrylanguage.csv
```

The script creates `db.sqlite` in the A04 folder and prints the answer. The three CSV files included in the folder can be used to test the program. If no file name is provided then a instruction message will be printed instead.

To run the query again using the existing database:
```bash
python3 db.py
```