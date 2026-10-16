import sys #Importing the sys module to read the command-line arguments

class Texter: #Defining the class Texter
    def __init__(self, filename): #Setting up the class with a filename
        self.filename = filename

    def run(self): #Defining the run method to process the file
        uppercase_count = 0 #Setting up a counter for lines beginning with a capital letter
        empty_count = 0 #Setting up a counter for empty lines

        with open(self.filename, "r", encoding="utf-8") as f: #Opening the file in read mode with UTF-8 encoding
            for line in f: #Looping through each line in the file
                if line[:1].isupper(): #Checking if the first character of the line is uppercase
                    uppercase_count += 1 #Starting the count of lines beginning with a capital letter
                else:
                    pass #If the line does not begin with a capital letter, do nothing
                
                if not line.strip(): #Checking if the line is empty (after stripping whitespace)
                    empty_count += 1 #Starting the count of empty lines
                else:
                    pass #If the line is not empty, do nothing

        #Printing the counts of lines beginning with a capital letter and empty lines
        print("Lines beginning with a capital letter:", uppercase_count)
        print("Empty lines:", empty_count) 

# Printing help message if no filename is provided
def main():
    if len(sys.argv) < 2:
        print("Correct usage: python3 texter.py <filename>")
    else:
        texter = Texter(sys.argv[1])
        texter.run()

if __name__ == "__main__":
    main() #Calling the main function to start the program