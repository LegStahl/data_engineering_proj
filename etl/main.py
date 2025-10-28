import sys
import extract
import transform
import load
from enum import Enum


class DB_CHOOSING(Enum):
    test = "test"
    original = "orig"


MAX_COUNT_ARGUMENTS = 4
MIN_COUNT_ARGUMENTS = 1
THIRD_ARGUMENT = 3
SECOND_ARGUMENT = 2
FIRST_ARGUMENT = 1
COUNT_OF_DATA = 100

def main():

    if len(sys.argv) > MIN_COUNT_ARGUMENTS:
        first_argument = sys.argv[FIRST_ARGUMENT]
        if first_argument == "--help":
            print("=========================================================================")
            print("It is a help command:")
            print("If you want only to download raw data from google drive put 'ext' as first argument and 'FILE_ID' as a second argument")
            print("If you want to download, transform data to parquet and write them to your db put 'all' as first argument and 'FILE_ID' as a second argument, as a third argument put 'test' or 'orig' to write data to certain db")
            print("NOTE: Raw data would be downloaded in every situation and would be left in the code dir with the name: RAW_DATA.csv")
            print("NOTE: Processed data would be placed in code dir with the name: PROCESSED_DATA.parquet")
            print("=========================================================================")
            return 0
        if first_argument == "ext":
            if len(sys.argv) == MAX_COUNT_ARGUMENTS:
                print("Only extracting started")
                second_argument = sys.argv[SECOND_ARGUMENT]
                df = extract.download_data(second_argument)
                if df is None:
                    print("Failure")
                    return None
                return 5
            else:
                print("Error has occured not all arguments were passed, check python3 main.py --help")
        if first_argument == "all":
            if len(sys.argv) == MAX_COUNT_ARGUMENTS:
                print("All stages of data transformation has started. NOTE: To work properly you need to have a special virtual env, check README.md")
                second_argument = sys.argv[SECOND_ARGUMENT]
                df = extract.download_data(second_argument)
                if df is None:
                    print("Failure")
                    return None
                df = transform.transform_data(df)
                df_reduced = df.head(COUNT_OF_DATA).copy()
                third_argument = sys.argv[THIRD_ARGUMENT]
                if third_argument == DB_CHOOSING.test.value or third_argument == DB_CHOOSING.original.value:
                    status = load.load_data(df_reduced, third_argument)
                    if status == True:
                        print("Everything has been written to data base. And file PROCESSED_DATA.parquet has been created.")
                    else:
                        print("Something went wrong in load_data, please check data base. And file PROCESSED_DATA.parquet has been created.")
                    print("=========================================================================")
                else:
                    print("Error has occured, arguments have faults please, check python3 main.py --help")
                    return None
            else:
                print("Error has occured not all arguments were passed, check python3 main.py --help")

    else:
        print("No arguments have been passed, please write python3 main.py --help")





if __name__ == "__main__":
    main()





