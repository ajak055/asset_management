from utils.error import *

class FetchAssetById:

    def __init__(self, assetid, db_object) -> None:
        self.assetId = assetid
        self.db_object = db_object


    def __prepare_query(self):
        return { "selector": {"assetId" : {"$eq": self.assetId}}}
       

    def fetchDocument(self, logger):
        logger.info("Business: fetchDocument by id invoked")
        self.__validate_request()
        query = self.__prepare_query()
        result = self.db_object.findSingleDocument("test", query, logger)
        return result

    
    def __validate_request(self):
        if self.assetId is None:
            raise BusinessValidationError(message='assetid is required')
