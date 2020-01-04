from pprint import pprint
from typing import Dict, Any

def print_dict(d : Dict[str, Any]) -> None:
	pprint(d)

py38 = {"version": "3.8", "release_year": 2019}
print_dict(py38)

py37 = {"version": "3.8", "release_year": "2019"}
print_dict(py37)
