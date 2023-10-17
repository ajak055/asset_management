from utils.error import *
import json

class FetchAsset:

    def __init__(self, query: dict, db_object) -> None:
        self.query = query
        self.db_object = db_object
        self.name_array = ["name", "category", "location", "skip", "limit"]

    def __prepare_query(self):
        fetch_query = { "selector": {}}
        if "name" in self.query:
            fetch_query['selector']['name'] = {"$eq": self.query['name']}
        if "category" in self.query:
            fetch_query['selector']['category'] = {"$eq": self.query['category']}
        if "location" in self.query:
            fetch_query['selector']['location'] = {"$eq": self.query['location']}
        if "limit" in self.query:
            fetch_query['limit'] = int(self.query["limit"])
        if "skip" in self.query:
            fetch_query['skip'] = int(self.query["skip"])
        return fetch_query

    def fetchDocument(self, logger):
        self.validateRequest()
        find_query = self.__prepare_query()
        result = self.db_object.findDocument("test", find_query, logger)
        return self.__prepareResponse(result)
        
    def __prepareResponse(self, result):
        return { "assets" : result}

    def validateRequest(self):
        if self.query is None:
            raise BusinessValidationError(message="minimum one query param is needed")
        else:
            for key in self.query:
                if key not in self.name_array:
                    raise BusinessValidationError(message='this parameter doesnt exists')
