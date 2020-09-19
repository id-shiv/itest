import os

def create_dir(directory: str):
    """ Create a directory
    :param directory: directory path and name
    :Return: 
        True, if directory exists or created
        False, if directory does not exist and could not be created
    """

    # create if directory does not exist in specified path
    if not os.path.exists(directory):
        print(f'creating directory: {directory}')
        try:
            os.makedirs(directory)
            print(f'directory {directory} successfully created')
            return True
        except Exception as e:
            print(e)
            print(f'failed to create directory {directory}')
            return False
    else:
        print(f'directory {directory} already exists')
        return True

def file_write(path: str, content):
    """ Writes the content to a file
    :param path: file path
    :param content: content to be written to file
    :Return:
        True, if content is succssfully written
        False, if content could not be written
    """

    try:  # Write to file
        print(f'writing to file {path}')
        with open(path, 'a') as f:
            f.write('\n' + content)
    except Exception as e:
        print(e)
        print(f'failed to write the content to {path}')
        return False
    print(f'write to file {path} successful')
    return True

if __name__ == "__main__":
    # Test above methods
    # create_dir('out/test')
    # file_write('out/test/test.txt', 'test content')