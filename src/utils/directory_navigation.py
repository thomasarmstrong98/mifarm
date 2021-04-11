from pathlib import Path

def get_path_to_rel_location(directory_to_find):
    """Goes up in directory heirarchy until it finds directory that contains
    `directory_to_find` and returns Path object of `directory_to_find`"""
    path = Path.cwd()
    num_tries = 5
    for num_up_folder in range(num_tries):
        path = path.parent
        if path / directory_to_find in path.iterdir():
            break

    if num_tries == num_up_folder:
        raise FileNotFoundError(f"The directory {directory_to_find} could not be found in the {num_tries}"
                                f" directories above this file's location.")
    return path / directory_to_find