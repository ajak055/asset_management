
class DeleteAsset:

    def __init__(self, assetid, db_object) -> None:
        self.assetId = assetid
        self.db_object = db_object

    def __prepare_query(self):
        return { "selector": {"assetId" : {"$eq": self.assetId}}}

    def deleteAsset(self, logger):
        query = self.__prepare_query()
        fetch_result = self.db_object.findSingleDocument("test", query, logger)
        print("fetch_result", fetch_result["_id"])
        result = self.db_object.deleteDocument("test", fetch_result, logger)
        print(result)
        return self.__deleteResponse()

    def __deleteResponse(self):
        return {"message": "asset deleted successfully"}
