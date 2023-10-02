import couchdb

class CouchDB:

    def __init__(self, url, username, password, port=5984) -> None:
        self.url = url
        self.port = port
        self.username = username
        self.password = password
        self.dbObject = None

    def connect(self):
        db_url = "http://{user}:{pwd}@{host}:{dbport}/".format(user=self.username, pwd=self.password, host=self.url, dbport=self.port)
        print(db_url)
        self.dbObject = couchdb.Server(db_url) 
    
    def createDb(self, dbname):
        self.dbObject(dbname)

    def insertDocument(self, dbname, document, logger):
        logger.info("Data: insertDocument invoked")
        db = self.dbObject[dbname]
        db.save(document)
        logger.info("Data: insertDocument exited")
