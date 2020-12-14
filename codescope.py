from codescope_functions import file_check, insert_into_file, query


def main():
    print("Initializing CodeScope... ")

    CS_COMMAND = file_check()

    if CS_COMMAND == "":
        print("No proper commands found!")
        return

    ANSWER = query(CS_COMMAND)

    insert_into_file(str(ANSWER))


while True:
    if __name__ == '__main__':
        main()
