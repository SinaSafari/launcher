import sys
import getopt
from lib.launcher.commands import run_format_command, run_serve_app_command, run_tests_command, run_update_requirements_txt_command



def cli(argument_list):
    short_options = "ustf"
    long_options = ["updaterequirements", "serve", "test", "format"]
    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
        print("arguments: ", values)
        for current_argument, current_value in arguments:

            if current_argument in ("-u", "--updaterequirements"):
                run_update_requirements_txt_command()
            elif current_argument in ("-s", "--serve"):
                run_serve_app_command()
            elif current_argument in ("-t", "--test"):
                run_tests_command()
            elif current_argument in ("-f", "--format"):
                print("format")
                run_format_command()
            else:
                print("invalid arguments")
                sys.exit()

    except getopt.error as err:
        # Output error, and return with an error code
        print(str(err))
        sys.exit(2)
