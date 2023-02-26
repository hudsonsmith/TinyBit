from importlib import import_module
import glob
from os.path import dirname, isfile

# import all .py files in the same directory as this __init__.py file
modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

# create a dictionary of function names and functions
functions = {}

for module_name in __all__:
    module = import_module(f".{module_name}", package=__name__)
    for name in dir(module):
        if name.startswith("__"):
            continue
        obj = getattr(module, name)
        if callable(obj):
            functions[f"{name}"] = obj

def get_functions():
    return functions