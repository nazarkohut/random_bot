"""
Use this file to manage error logs.
"""

import logging

from urllib.error import HTTPError as ulibHTTPError
from pymongo.errors import OperationFailure
from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                      CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                      MessageTextIsEmpty, RetryAfter,
                                      CantParseEntities, MessageCantBeDeleted)

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, CantDemoteChatCreator):
        logging.exception("Can't demote chat creator")
        return True

    if isinstance(exception, MessageNotModified):
        logging.exception("Message is not modified")
        return True
    if isinstance(exception, MessageCantBeDeleted):
        logging.exception("Message cant be deleted")
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.exception("Message to delete not found")
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.exception("MessageTextIsEmpty")
        return True

    if isinstance(exception, Unauthorized):
        logging.exception("Unauthorized: %s", exception)
        return True

    if isinstance(exception, InvalidQueryID):
        logging.exception("InvalidQueryID: %s \nUpdate: %s", exception, update)
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception("TelegramAPIError: %s \nUpdate: %s", exception, update)
        return True
    if isinstance(exception, RetryAfter):
        logging.exception("RetryAfter: %s \nUpdate: %s", exception, update)
        return True
    if isinstance(exception, CantParseEntities):
        logging.exception("CantParseEntities: %s \nUpdate: %s", exception, update)
        return True
    if isinstance(exception, ulibHTTPError):
        logging.exception("RequestError: %s", exception)
        return True
    if isinstance(exception, OperationFailure):
        logging.exception("MongoDBError: %s", exception)
        return True

    logging.exception("Update: %s \n%s", update, exception)
