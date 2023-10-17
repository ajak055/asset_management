import typing as t
from apiflask import HTTPError
from apiflask.types import ResponseHeaderType
# from utils.constants import Constants


class CustomError(Exception):

    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class BusinessValidationError(Exception):

    def __init__(self, message) -> None:
        self.message = message
        self.code =  400 #Constants.httpConstants("BAD_REQUEST")
        super().__init__(self.message)


class NotFoundError(Exception):

    def __init__(self, message) -> None:
        self.message = message
        self.code =  404
        super().__init__(self.message)