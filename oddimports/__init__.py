import sys

from .types.type_json import JsonMetaPathFinder


sys.meta_path.append(JsonMetaPathFinder())
