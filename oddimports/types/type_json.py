import json

from ..mixins import Loader, MetaPathFinder


class JsonLoader(Loader):
    def get_data_from_file(self, json_file):
        return json.load(json_file, object_hook=self.is_valid_json)


class JsonMetaPathFinder(MetaPathFinder):
    file_extension = "json"
    loader = JsonLoader
