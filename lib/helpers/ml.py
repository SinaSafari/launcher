import os
import hashlib
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

    # TODO: save the model name and other needed data in database

    return True


def save_plots(model, plot_instance, filename: str) -> bool:
    """
    this function is a helper for saving plots in filesystem for further usage
    also the image title will be stored in database as well.

    Parameters
    ----------
    model
        the model that the plot is related to
    plot_instance
        the image that is going to save in file system
    filename
        filename that will be used in image saving. the filename should be less than 128 character
        also extension should one of `png`, `jpg`, or `jpeg`
    """

    filename_extension = filename.split(".")[1]
    accepted_image_extensions = ["png", "jpg", "jpeg"]
    if len(filename) > 128 or filename_extension not in accepted_image_extensions:
        return False
    plot_instance.savefig(filename)

    # todo: save the filename with required info in database as well

    return True
