def write_to_file(file_path, content):
    """
    Writes new content to a file, overwriting any existing content, and returns the file object.

    :param file_path: Path to the file to be written.
    :param content: Content to write to the file.
    :return: The file object.
    """
    try:
        file = open(file_path, 'w')
        file.write(content)
        file.close()
        return file
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")
        return None

def append_to_file(file_path, content):
    """
    Appends new content to the end of an existing file and returns the file object.

    :param file_path: Path to the file to be appended.
    :param content: Content to append to the file.
    :return: The file object.
    """
    try:
        file = open(file_path, 'a')
        file.write(content)
        file.close()
        return file
    except IOError as e:
        print(f"Error appending to file {file_path}: {e}")
        return None

# # Example usage:
# new_content = "This is the new content.\n"
# append_content = "This content will be appended.\n"
#
# file_obj = write_to_file('example.txt', new_content)
# if file_obj is not None:
#     # Perform additional operations on the file object if needed
#     pass
#
# file_obj = append_to_file('example.txt', append_content)
# if file_obj is not None:
#     # Perform additional operations on the file object if needed
#     pass
