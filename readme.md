# oddimports

oddimports is a package that allows you to load a strange file type as normal python files.

## Information

By default, this package only supports json. Before you can load a json file you need to have `oddimports` imported somewhere.

*TAKE CARE: When there is a python file with the same name, it import that file.* 

## Usage
`./settings/config.json`
```json
{
	"TEST": "data",
	"OTHER_INFO": {"YPO":123}
}
```
`./main.py`
```py
import oddimports

from settings import config
import settings.config as settings
from settings.config import OTHER_INFO

print(config.TEST)   # --> "data"
print(settings.TEST) # --> "data"
print(OTHER_INFO)    # --> {"YPO":123}

```

## Create other odd import types

1. Create a new file, for example type_ini.py
2. Copy the code of type_json.py
3. Rename the classes (in this case Json to Ini), also the extension must be changed
4. Rewrite the function `get_data_from_file` from `Loader`, so that the code converts the ini file into a dict
your code looks like this:
```py
import ini_to_dict # this module doesn't exists but you know what i mean haha

from ..mixins import Loader, MetaPathFinder


class IniLoader(Loader):
    def get_data_from_file(self, ini_file):
        return ini_to_dict(ini_file)


class IniMetaPathFinder(MetaPathFinder):
    file_extension = "ini"
    loader = IniLoader

```

5. Add the `IniMetaPathFinder` to the meta_path in the `__init__.py` file
your code looks like this:
```py
import sys

from .types.type_json import JsonMetaPathFinder
from .types.type_ini import IniMetaPathFinder


sys.meta_path.append(JsonMetaPathFinder())
sys.meta_path.append(IniMetaPathFinder())
```

6. You are ready to use your custom loader 

*TAKE CARE: When you have config.json and config.ini, it will take the json file because you've got add that earlier.*
