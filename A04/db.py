import csv
import sqlite3
import sys
from pathlib import Path


class WorldDatabase: #Creates a database from the CSV files
    def __init__(self, csv_filenames):
        self.folder = Path(__file__).resolve().parent
        self.database_path = self.folder / "db.sqlite"
        if not csv_filenames and not self.database_path.exists(): # Stop if no CSV files were provided and the database does not exist yet.
            raise FileNotFoundError( # Raise an error with instructions for creating the database.
                "Correct usage on the first run: "
                "python3 db.py country.csv city.csv countrylanguage.csv"
            )

        self.connection = sqlite3.connect(self.database_path) #Creates a connection to the database.

        try:
            for csv_filename in csv_filenames:
                self.import_csv(csv_filename)

            self.print_french_countries() #Prints the countries that officially use French.
        finally:
            self.connection.close()

    def import_csv(self, csv_filename): #Imports a CSV file into the database.
        csv_path = Path(csv_filename)

        if not csv_path.is_absolute(): #Checks if the CSV file path is absolute.
            csv_path = self.folder / csv_path

        table_name = csv_path.stem

        if self.table_exists(table_name): #Checks if the table already exists in the database.
            return

        with self.connection:
            with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file: #Opens the CSV file for reading.
                reader = csv.reader(csv_file, delimiter=";")
                columns = next(reader, None)

                if not columns: #Raises an error if the CSV file is empty or has no header.
                    raise ValueError(f"{csv_path.name} is empty or has no header.")

                quoted_table = self.quote_identifier(table_name) # Escape and quote the table name so SQLite can use it as an identifier.
                quoted_columns = [
                    self.quote_identifier(column) for column in columns
                ]
                column_definitions = ", ".join( #Creates the column definitions for the CREATE TABLE statement.
                    f"{column} TEXT" for column in quoted_columns
                )

                self.connection.execute( #Creates the table in the database with the specified column definitions.
                    f"CREATE TABLE {quoted_table} ({column_definitions})"
                )

                placeholders = ", ".join(["?"] * len(columns)) #Creates a string of placeholders for the INSERT statement, one for each column.
                insert_columns = ", ".join(quoted_columns)

                self.connection.executemany( #Inserts the data from the CSV file into the newly created table in the database.
                    f"INSERT INTO {quoted_table} ({insert_columns}) "
                    f"VALUES ({placeholders})",
                    reader,
                )

    def table_exists(self, table_name): #Checks if a table with the specified name exists in the database.
        result = self.connection.execute(
            "SELECT 1 FROM sqlite_master "
            "WHERE type = 'table' AND name = ?",
            (table_name,),
        )
        return result.fetchone() is not None #Returns True if the table exists, False otherwise.

    def quote_identifier(self, identifier):
        escaped_identifier = identifier.replace('"', '""')
        return f'"{escaped_identifier}"'

    def print_french_countries(self): #Prints the countries where Frence is the official language, sorted alphabetically.
        question = (
            "10. Which countries officially use French? "
            "Provide their full names, sorted alphabetically."
        )

        results = self.connection.execute( #Executes the SQL query to retrieve the list of countries where French is the official language.
            """
            SELECT DISTINCT country.Name
            FROM country
            JOIN countrylanguage
                ON country.Code = countrylanguage.CountryCode
            WHERE countrylanguage.Language = 'French'
                AND countrylanguage.IsOfficial = 'T'
            ORDER BY country.Name
            """
        ).fetchall()

        print(question) #Prints the question to the console.
        for result in results:
            print(result[0])

    @staticmethod #Defines a static method that can be called without creating an instance of the class.
    def main(arguments):
        WorldDatabase(arguments)


if __name__ == "__main__": #Checks if the script is being run directly (not imported as a module) and calls the main method with command-line arguments.
    WorldDatabase.main(sys.argv[1:]) #Passes the command-line arguments (excluding the script name) to the main method of the WorldDatabase class.