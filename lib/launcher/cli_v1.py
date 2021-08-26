import sys
import getopt
import threading
from lib.launcher.commands import (
    run_format_command,
    run_serve_app_command,
    run_tests_command,
    run_update_requirements_txt_command,
    run_client_app_dev,
)
from lib.launcher.scaffold import scaffold, descaffold


def cli(argument_list):
    short_options = "ustfcgd"
    long_options = [
        "updaterequirements",
        "serve",
        "test",
        "format",
        "client",
        "generate",
        "descaffold",
    ]
    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
        for current_argument, current_value in arguments:

            if current_argument in ("-u", "--updaterequirements"):
                run_update_requirements_txt_command()
                print("✅ requirements.txt updated successfully")
            elif current_argument in ("-s", "--serve"):
                server_thread = threading.Thread(target=run_serve_app_command)
                server_thread.start()
            elif current_argument in ("-t", "--test"):
                run_tests_command()
            elif current_argument in ("-f", "--format"):
                print("format")
                run_format_command()
            elif current_argument in ("-c", "--client"):
                client_thread = threading.Thread(target=run_client_app_dev)
                client_thread.start()
            elif current_argument in ("-g", "--generate"):
                print(current_value)
                scaffold(values[0])
            elif current_argument in ("-d", "--descaffold"):
                descaffold(values[0])
            else:
                print("invalid arguments")
                sys.exit()

    except getopt.error as err:
        # Output error, and return with an error code
        print(str(err))
        sys.exit(2)
