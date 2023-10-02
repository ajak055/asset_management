from flask import Flask, request, jsonify
from utils.logger import Logger
from business.createAsset import CreateAsset
app = Flask(__name__)


@app.route('/')
def hello_world():
   return "Hello World"


@app.route("/v1/assetmanagement", methods = ['POST'])
def createAsset():
   logger = Logger("asset_management")
   if request.method == 'POST':
      logger.info("API: create asset invoked")
      input = request.get_json()
      print(input)
      result = CreateAsset(input).add_document_to_db(logger)
      return jsonify(result)

@app.route("/v1/assetmanagement", methods = ['GET'])
def fetchAsset():
   logger = Logger("asset_management")
   logger.info("API: fetch asset invoked")
   return jsonify({"asset" : [{
      "assetName" : "test asset"
   }]})

@app.route("/v1/assetmanagement/<id>", methods = ['GET'])
def fetchAssetById(id):
   print("fetch id is ", str(id))
   logger = Logger("asset_management")
   logger.info("API: fetch asset invoked")
   return jsonify({"asset" : [{
      "assetName" : "test asset"
   }]})

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