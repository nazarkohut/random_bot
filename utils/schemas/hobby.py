"""
HOBBY_SCHEMA is defined here and is used to determine if response received from NINJAS_API is correct.
"""
from cerberus import Validator

HOBBY_SCHEMA = {
    "hobby": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "link": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "category": {
        "type": "string",
        "required": True,
        "empty": False
    },
}

hobby_validator = Validator(HOBBY_SCHEMA)
