import os
from typing import Callable
from termcolor import colored
from config.settings import app_paths, msg_colors


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
    filename = f"{app_paths['models']}/{name}.py"
    write_to_file(filename, model_template)


def create_repository(name: str):
    repository_template = f"""
    
    """
    filename = f"{app_paths['repos']}/{name}_repository.py"
    write_to_file(filename, repository_template)


def create_service(name: str):
    service_template = f"""

    """
    filename = f"{app_paths['services']}/{name}_service.py"
    write_to_file(filename, service_template)


def create_controller(name: str):
    controller_template = f"""

    """
    filename = f"{app_paths['controllers']}/{name}_controller.py"
    write_to_file(filename, controller_template)


def create_api_route(name: str):
    api_template = f"""

    """
    filename = f"{app_paths['api']}/{name}_api.py"
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
    scaffold_printer(create_model, f"{name}")
    scaffold_printer(create_repository, f"{name}")
    scaffold_printer(create_service, f"{name}")
    scaffold_printer(create_controller, f"{name}")
    scaffold_printer(create_api_route, f"{name}")

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

    scaffold_printer(delete_file, f"{app_paths['models']}/{name}.py", create=False)
    scaffold_printer(
        delete_file, f"{app_paths['repos']}/{name}_repository.py", create=False
    )
    scaffold_printer(
        delete_file, f"{app_paths['services']}/{name}_service.py", create=False
    )
    scaffold_printer(
        delete_file, f"{app_paths['controllers']}/{name}_controller.py", create=False
    )
    scaffold_printer(delete_file, f"{app_paths['api']}/{name}_api.py", create=False)

    # todo: graphql support should be added later

    print(colored("deleted successfully", msg_colors["success"], attrs=["bold"]))
    return True
