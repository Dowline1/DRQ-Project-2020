import mysql.connector
import dbconfig as cfg

class CastDao:
    db = ""

    def connectToDB(self):
        self.db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['username'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database']
        )
    def __init__(self): 
        self.connectToDB()
    
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    def create(self, cast):
        cursor = self.getCursor()
        sql = "INSERT INTO moviecast (movieid, actor, rating) values (%s,%s,%s)"
        values = [
            cast['movieid'],
            cast['actor'],
            cast['rating']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.getCursor()
        sql = 'SELECT * FROM moviecast'
        cursor.execute(sql)
        results = cursor.fetchall()
        
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            
            returnArray.append(resultAsDict)

        cursor.close()
        return returnArray

    def convertToDict(self, result):
        colnames = ['castid', 'movieid', 'actor', 'rating']
        cast = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                cast[colName] = value
        return cast

    def findById(self, castid):
        cursor = self.getCursor()
        sql = 'SELECT * FROM moviecast WHERE castid = %s'
        values = [castid]
        cursor.execute(sql, values)
        result = cursor.fetchone()

        cursor.close()        
        return self.convertToDict(result)

    def update(self, cast):
        cursor = self.getCursor()
        sql = "UPDATE moviecast SET movieid = %s, actor = %s, rating = %s WHERE castid = %s"
        values = [
            cast['movieid'],
            cast['actor'],
            cast['rating'],
            cast['castid']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cast

    def delete(self, castid):
        cursor = self.getCursor()
        sql = 'DELETE FROM moviecast WHERE castid = %s'
        values = [castid]
        cursor.execute(sql, values)
        self.db.commit()
        
        cursor.close()
        return {}




castDao = CastDao()