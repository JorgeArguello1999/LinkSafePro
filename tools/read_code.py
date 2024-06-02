def read_code(path: str = None) -> str:
    if path is None:
        raise ValueError("A file path must be provided")

    try:
        with open(f"./tools/{path}", 'r') as file:
            return file.read()

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path {path} does not exist")

    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")