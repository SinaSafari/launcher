import os
from typing import Callable

APP_BASE_PATH = f"{os.getcwd()}/app"
MODELS_PATH = f"{APP_BASE_PATH}/models"
REPOSITORIES_PATH = f"{APP_BASE_PATH}/repositories"
SERVICES_PATH = f"{APP_BASE_PATH}/services"
CONTROLLERS_PATH = f"{APP_BASE_PATH}/controllers"
API_PATH = f"{APP_BASE_PATH}/api/v1"


def write_to_file(filename: str, content: str):
    try:
        with open(filename, "x") as f:
            f.write(content)
    except FileExistsError:
        print(
            f"a file with provided name already exists. {filename} can't be recreated."
        )
        exit(1)


def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f"{filename} \nfile not found. please check filesystem manually.")
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
        print(f"⌛ creating {instance_name}...")
        func(instance_name)
        print(f"{instance_name} created successfully.")
    else:
        print(f"⌛ deleting {instance_name}...")
        func(instance_name)
        print(f"{instance_name} \n✅deleted successfully.")


def scaffold(name: str) -> bool:
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

    print("✔️ scaffolding was successful.")
    return True


def descaffold(name: str) -> bool:
    if not name:
        print("⚠️ name is required")
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
    print("deleted successfully")
    return True
