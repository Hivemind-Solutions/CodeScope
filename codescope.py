from codescope_functions import startup, startup_flash_splash, capture_file, file_check, query_how2, insert_into_file
import codescope_variables as cs_vars
import time


def main():
    print("Initializing CodeScope... ")
    # startup()
    startup_flash_splash()
    print("Startup complete")
    capture_file()
    print("Capture file complete ")

    while cs_vars.CS_RUNNING:
        cs_command = file_check()
        if cs_command == "":
            print("No proper commands found!")
        else:
            answer = query_how2(cs_command)
            insert_into_file(str(answer))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
