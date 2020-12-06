def get_data_from_fail(filename, split_string) -> list:
    try:
        return open(filename, 'r').read().split(split_string)
    except FileNotFoundError:
        print("Fail not found")
