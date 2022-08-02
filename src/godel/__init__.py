import os
from fastapi import File

import toml 

from godel.api import GoldenAPI

script_path = os.path.basename(os.path.dirname(__file__))

try:
    pyproject_toml = toml.load(
        os.path.join(
            script_path, 
            os.pardir,
            os.pardir,
            "pyproject.toml"
        )
    )
    version = pyproject_toml["tool"]["poetry"]["version"]
except (FileNotFoundError, KeyError, toml.decoder.TomlDecodeError):
    version = "unknown"
    
