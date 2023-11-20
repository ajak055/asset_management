from utils.error import *
import datetime
import utils.env_constants as const

class UpdateAsset:

    def __init__(self, id, db_object, request) -> None:
        self.id = id
        self.request = request
        self.db_object = db_object

    def __validateRequest(self, logger):
        get_doc_query = { "selector": {"assetId" : {"$eq": self.id}}}
        result = self.db_object.findSingleDocument(const.DB_NAME, get_doc_query, logger)
        return self.__prepare_query(self.request, result)
        


    def __prepare_query(self, request, result):
        result["name"] = request["name"]
        result["category"] = request["category"]
        result["location"] = request["location"]
        result["description"] = request["description"]
        result["modifiedDate"] = datetime.datetime.now().isoformat()
        return result

    def update_asset(self, logger):
        update_query = self.__validateRequest(logger);
        self.db_object.insertDocument("test", update_query, logger)
        return {"message": "asset updated successfully", "id": self.id}