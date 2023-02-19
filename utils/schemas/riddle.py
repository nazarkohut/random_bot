"""
RIDDLE_SCHEMA is defined here and is used to determine if response received from NINJAS_API is correct.
"""
from cerberus import Validator

RIDDLE_SCHEMA = {
    "title": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "question": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "answer": {
        "type": "string",
        "required": True,
        "empty": False
    },
}

riddle_validator = Validator(RIDDLE_SCHEMA)
