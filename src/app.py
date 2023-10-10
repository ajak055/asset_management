from flask import Flask, request, jsonify
from utils.logger import Logger
from business.createAsset import CreateAsset
from business.fetchAsset import FetchAsset
from business.fetchAssetById import FetchAssetById
from data.db import CouchDB
from utils.response import success_response, failure_response

app = Flask(__name__)

db_handler = CouchDB("127.0.0.1", "assetmgmt", "pass123", 5984)
db_handler.connect()

@app.route('/')
def hello_world():
   return "Hello World"


@app.route("/v1/assetmanagement", methods = ['POST'])
def createAsset():
   logger = Logger("asset_management")
   if request.method == 'POST':
      logger.info("API: create asset invoked")
      input = request.get_json()
      result = CreateAsset(input, db_handler).add_document_to_db(logger)
      return jsonify(result)

@app.route("/v1/assetmanagement", methods = ['GET'])
def fetchAsset():
   try:
      logger = Logger("asset_management")
      logger.info("API: fetch asset invoked")
      response = FetchAsset(request.args.to_dict(), db_handler).fetchDocument(logger)
      return success_response(response)
   except Exception as e:
      return failure_response(e)

@app.route("/v1/assetmanagement/<id>", methods = ['GET'])
def fetchAssetById(id):
   print("fetch id is ", str(id))
   logger = Logger("asset_management")
   logger.info("API: fetch asset by id invoked")
   response = FetchAssetById(id, db_handler).fetchDocument(logger)
   return success_response(response)

@app.route("/v1/assetmanagement/<id>", methods = ['PUT'])
def updateAsset(id):
   logger = Logger("asset_management")
   logger.info("API: fetch asset invoked")
   logger.info("given id is "+str(id))
   return jsonify({"message" : "asset updated"})

@app.route("/v1/assetmanagement/<id>", methods = ['DELETE'])
def deleteAsset(id):
   logger = Logger("asset_management")
   logger.info("given id is ",id)
   logger.info("API: delete asset invoked")
   return jsonify({"message" : "asset deleted"})


if __name__ == '__main__':
   app.run()