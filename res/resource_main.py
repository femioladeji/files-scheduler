import os.path
def resource_path(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)