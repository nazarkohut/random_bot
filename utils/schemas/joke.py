"""
JOKE_SCHEMA is defined here and is used to determine if response received from NINJAS_API is correct.
"""
from cerberus import Validator

JOKE_SCHEMA = {
    "joke": {
        "type": "string",
        "required": True,
        "empty": False
    }
}

joke_validator = Validator(JOKE_SCHEMA)
