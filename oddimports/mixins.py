import sys
import os
import json
from importlib.abc import MetaPathFinder as BaseMetaPathFinder, Loader as BaseLoader
from importlib.util import spec_from_loader

from .errors import ValidationError


class Loader(BaseLoader):
    def __init__(self, full_path, filename):
        self._full_path = full_path
        self._filename = filename

    def create_module(self, spec):
        with open(self._full_path) as file:
            self._data = self.get_data_from_file(file)

    def get_data_from_file(self, file):
        raise ValidationError(
            """
            Override this function and return a dict contains
            the data you want to store in the module
            """
        )

    def exec_module(self, module):
        module.__dict__.update(self._data)


class MetaPathFinder(BaseMetaPathFinder):
    file_extension = None
    loader = None

    def find_spec(self, fullname, paths, target=None):
        mod_name = fullname.split(".")[-1]
        paths = paths or [os.path.abspath(os.curdir)]
        filename = "%s.%s" % (mod_name, self.file_extension)

        for check_path in paths:
            full_path = os.path.join(check_path, filename)

            if os.path.exists(full_path):
                return spec_from_loader(fullname, self.loader(full_path, filename))

        return None
