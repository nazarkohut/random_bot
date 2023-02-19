"""File that contains general constants"""
from config import NINJAS_API_KEY

ERROR_ON_OUR_SIDE = "Something went wrong on our side! We are sorry that this happened!"
NINJAS_API_HEADER = {"X-Api-Key": f"{NINJAS_API_KEY}"}
COMMON_REQUEST_TIMEOUT = 15.0
