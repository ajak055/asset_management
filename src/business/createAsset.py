import datetime
import uuid
class CreateAsset:

    def __init__(self, data: dict, db_object) -> None:
        self.data = data
        self.db_object = db_object

    def validate_request(self, logger):
        logger.info("Business: CreateAsset: validate_request invoked")
        #

        logger.info("Business: CreateAsset: validate_request exited")

    def __prepare_document(self, logger):
        logger.info("Business: CreateAsset: prepare_document invoked")

        id = uuid.uuid4()
        date = datetime.datetime.now()

        document = {
            "assetId": str(id),
            "name": self.data['name'],
            "category": self.data['category'],
            "location": self.data['location'],
            "description": "asset management service" if self.data['description'] is not None else self.data['description'],
            "createDate": date.isoformat(),
            "modifiedDate" : date.isoformat(),
            "etag" : str(uuid.uuid4())
        }
        logger.info("Business: CreateAsset: prepare_document exited")
        return document
    
    def add_document_to_db(self, logger):
        logger.info("Business: CreateAsset: add_document_to_db invoked")

        document = self.__prepare_document(logger)
        self.db_object.insertDocument("test", document, logger)
        return {"message": "asset created successfully", "id": document["assetId"]}
    
    def serialize_datetime(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")
