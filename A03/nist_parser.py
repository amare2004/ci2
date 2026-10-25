import sys  #Import the sys module to access command-line arguments and handle errors
from bs4 import BeautifulSoup #Import the BeautifulSoup library for parsing HTML files


def print_compound_names(filename):
    with open(filename, encoding="utf-8") as file: #Open the HTML file using UTF-8 encoding.
        soup = BeautifulSoup(file, "html.parser") #Tells BeautifulSoup to parse the HTML file

    for link in soup.find_all(
        "a", href=lambda href: href and "/cgi/cbook.cgi" in href #Find all anchor tags with href attributes containing "/cgi/cbook.cgi"
    ):
        name = link.get_text(strip=True) #Strip whitespace from the text of the link
        if name:
            print(name) #Print the name of the compound if it is not empty


if __name__ == "__main__":
    if len(sys.argv) < 2: #Check if the user has used the script correctly
        print("Correct usage: python3 nist_parser.py <html-file>", file=sys.stderr)
        sys.exit(1)

    print_compound_names(sys.argv[1]) #Call the function with the filename provided as a command-line argument