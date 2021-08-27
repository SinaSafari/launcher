import os
from typing import Callable
from termcolor import colored

APP_BASE_PATH = f"{os.getcwd()}/app"
MODELS_PATH = f"{APP_BASE_PATH}/models"
REPOSITORIES_PATH = f"{APP_BASE_PATH}/repositories"
SERVICES_PATH = f"{APP_BASE_PATH}/services"
CONTROLLERS_PATH = f"{APP_BASE_PATH}/controllers"
API_PATH = f"{APP_BASE_PATH}/api/v1"

msg_colors = {
    "error": "red",
    "warning": "yellow",
    "success": "green",
    "info": "grey",
}


def write_to_file(filename: str, content: str):
    try:
        with open(filename, "x") as f:
            f.write(content)
    except FileExistsError:
        print(
            colored(
                f"a file with provided name already exists. {filename} can't be recreated.",
                msg_colors["error"],
                attrs=["bold"],
            )
        )
        exit(1)


def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(
            colored(
                f"{filename} \nfile not found. please check filesystem manually.",
                msg_colors["error"],
                attrs=["bold"],
            )
        )
        exit(1)


def create_model(name: str):
    model_template = f"""class {name.capitalize()}:
        pass
    """
    filename = f"{MODELS_PATH}/{name}.py"
    write_to_file(filename, model_template)


def create_repository(name: str):
    repository_template = f"""
    
    """
    filename = f"{REPOSITORIES_PATH}/{name}_repository.py"
    write_to_file(filename, repository_template)


def create_service(name: str):
    service_template = f"""

    """
    filename = f"{SERVICES_PATH}/{name}_service.py"
    write_to_file(filename, service_template)


def create_controller(name: str):
    controller_template = f"""

    """
    filename = f"{CONTROLLERS_PATH}/{name}_controller.py"
    write_to_file(filename, controller_template)


def create_api_route(name: str):
    api_template = f"""

    """
    filename = f"{API_PATH}/{name}_api.py"
    write_to_file(filename, api_template)


def create_gql_resolver(name: str):
    pass


def scaffold_printer(func: Callable, instance_name, create=True):
    if create:

        print(colored(f"⌛ creating {instance_name}...", msg_colors["info"]))
        func(instance_name)
        print(colored(f"{instance_name} created successfully.", msg_colors["success"]))
    else:
        print(colored(f"⌛ deleting {instance_name}...", msg_colors["info"]))
        func(instance_name)
        print(
            colored(f"{instance_name} \n✅deleted successfully.", msg_colors["success"])
        )


def scaffold(name: str) -> bool:
    """
    this function used for adding regular files for an entity in the accepted launcher web app architecture.
    also these files will be filled with some auto generated boilerplate, like some necessary imports and class
    or function names

    if anythings went wrong, warning or error messages will be shown in the stdout and the app will be exited.
    by the way, it's not revert (or rollback) the operation, so check the file system manually. in future versions
    it could be changed.

    Todo add rollback feature

    Parameters
    ----------
    name
        name of the entity that will be used in name of files and class or function names,

    Returns
    -------
    bool: indicate that everything goes well.
    """
    if not name:
        print("⚠️ name is required")
        exit(1)
    scaffold_printer(create_model, name)
    scaffold_printer(create_repository, name)
    scaffold_printer(create_service, name)
    scaffold_printer(create_controller, name)
    scaffold_printer(create_api_route, name)

    # todo: uncomment this when the structure has been created.
    # scaffold_printer(create_gql_resolver, name)

    print(
        colored("✔️ scaffolding was successful.", msg_colors["success"], attrs=["bold"])
    )
    return True


def descaffold(name: str) -> bool:
    """
    this function used for removing all the generated file using scaffold (-g in cli)

    Parameters
    ----------
    name
        exact name of entity that used in scaffolding

    """
    if not name:
        print(colored("⚠️ name is required", msg_colors["error"]))
        exit(1)

    scaffold_printer(delete_file, f"{MODELS_PATH}/{name}.py", create=False)
    scaffold_printer(
        delete_file, f"{REPOSITORIES_PATH}/{name}_repository.py", create=False
    )
    scaffold_printer(delete_file, f"{SERVICES_PATH}/{name}_service.py", create=False)
    scaffold_printer(
        delete_file, f"{CONTROLLERS_PATH}/{name}_controller.py", create=False
    )
    scaffold_printer(delete_file, f"{API_PATH}/{name}_api.py", create=False)

    # todo: graphql support should be added later

    print(colored("deleted successfully", msg_colors["success"], attrs=["bold"]))
    return True
