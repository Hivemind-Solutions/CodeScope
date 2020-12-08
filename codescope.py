from codescope_functions import file_check, insert_into_file, query
import time as t

def main():
    print("Initializing CodeScope... ")

    CS_COMMAND = "how2" + file_check()

    if CS_COMMAND == "":
        print("No proper commands found!")
        return

    """query(CS_COMMAND="how2" + file_check())"""

    ANSWER = """text from answer"""""
    insert_into_file(str(ANSWER))

if __name__ == "__main__":
    main()
