import os
import joblib


def save_model(model, model_name) -> bool:
    """
    saves the model both in file system and database for further uses.

    Parameters
    ----------
    model
        trained model that is going to saved in filesystem as a file
    model_name: str
        name of the model that is going to be the name of the file also
        the name that stores in database (maybe the url path as well)
    """

    filename = f"{os.getcwd()}/storage/${model_name}.model"
    if os.path.isfile(filename):
        return False
    joblib.dump(model, filename)

    # TODO: save the modelname and other needed data in database

    return True
