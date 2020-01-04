from typing import TypedDict
import json

class PythonVersion(TypedDict):
    version: str
    release_year: int

def print_dict(d : PythonVersion) -> None:
    print(json.dumps(d, indent=2))

py38 = PythonVersion(version="3.8", release_year=2019)
print_dict(py38)

py37 = PythonVersion(version="3.8", release_year="2019")
print_dict(py37)
