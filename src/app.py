from flask import Flask, request, jsonify
from utils.logger import Logger
from business.createAsset import CreateAsset
from business.fetchAsset import FetchAsset
from business.fetchAssetById import FetchAssetById
from business.updateAsset import UpdateAsset
from business.deleteAsset import DeleteAsset
from data.db import CouchDB
import utils.env_constants as const
from utils.response import success_response, failure_response

app = Flask(__name__)

db_handler = CouchDB(const.URL, const.USERNAME, const.PASSWORD, 5984)
db_handler.connect()

@app.route("/v1/assetmanagement", methods = ['POST'])
def createAsset():
   try:
      logger = Logger("asset_management")
      if request.method == 'POST':
         logger.info("API: create asset invoked")
         input = request.get_json()
         result = CreateAsset(input, db_handler).add_document_to_db(logger)
         return jsonify(result)
   except Exception as e:
      return failure_response(e)

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
   try:
      print("fetch id is ", str(id))
      logger = Logger("asset_management")
      logger.info("API: fetch asset by id invoked")
      response = FetchAssetById(id, db_handler).fetchDocument(logger)
      return success_response(response)
   except Exception as e:
      return failure_response(e)

@app.route("/v1/assetmanagement/<id>", methods = ['PUT'])
def updateAsset(id):
   try:
      logger = Logger("asset_management")
      logger.info("API: update asset invoked")
      input = request.get_json()
      response = UpdateAsset(id, db_handler, input).update_asset(logger)
      return success_response(response)
   except Exception as err:
      return failure_response(err)
     


@app.route("/v1/assetmanagement/<id>", methods = ['DELETE'])
def deleteAsset(id):
   logger = Logger("asset_management")
   logger.info("API: delete asset invoked")
   response = DeleteAsset(id, db_handler).deleteAsset(logger)
   return success_response(response)

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port=8000, debug=False)