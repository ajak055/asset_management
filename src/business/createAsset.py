import datetime
import uuid
from data.db import CouchDB
import json


db_handler = CouchDB("127.0.0.1", "assetmgmt", "pass123", 5984)
db_handler.connect()

class CreateAsset:

    def __init__(self, data: dict) -> None:
        self.data = data

    def validate_request(self, logger):
        logger.info("Business: CreateAsset: validate_request invoked")

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
            "modifiedDate" : date.isoformat()
        }
        logger.info("Business: CreateAsset: prepare_document exited")
        return document
    
    def add_document_to_db(self, logger):
        logger.info("Business: CreateAsset: add_document_to_db invoked")

        document = self.__prepare_document(logger)
        print(type(document))
        db_handler.insertDocument("test", document, logger)
        return {"message": "asset created successfully"}
    
    def serialize_datetime(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")













