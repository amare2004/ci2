# A06 - Number 4
This script imports the Excel csv file and uses Pandas and
Matplotlib to create a graph PNG file.

## How to run the script
Clone the repository from GitHub and go to the correct directory.
```bash
git clone git@github.com:amare2004/ci2.git
cd ci2/A06
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
python3 graph.py graph.csv graph.png
```

The script creates `graph.png` in the A06 folder and plots the graph of y=1/x in function of x. The graph.csv file included in the folder can be used to test the program. If no CSV or PNG file name is provided then an instruction message will be printed.