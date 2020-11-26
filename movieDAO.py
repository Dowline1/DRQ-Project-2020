import mysql.connector
import dbconfig as cfg

class MovieDao:
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

    def create(self, movie):
        cursor = self.getCursor()
        sql = "INSERT INTO movies (title, director, releaseyear, tomatoescore) values (%s,%s,%s,%s)"
        values = [
            movie['title'],
            movie['director'],
            movie['releaseyear'],
            movie['tomatoescore']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.getCursor()
        sql = 'SELECT * FROM movies'
        cursor.execute(sql)
        results = cursor.fetchall()
        
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            
            returnArray.append(resultAsDict)

        cursor.close()
        return returnArray

    def convertToDict(self, result):
        colnames = ['movieid', 'title', 'director', 'releaseyear', 'tomatoescore']
        movie = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                movie[colName] = value
        return movie

    def findById(self, movieid):
        cursor = self.getCursor()
        sql = 'SELECT * FROM movies WHERE movieid = %s'
        values = [movieid]
        cursor.execute(sql, values)
        result = cursor.fetchone()

        cursor.close()        
        return self.convertToDict(result)

    def update(self, movie):
        cursor = self.getCursor()
        sql = "UPDATE movies SET title = %s, director = %s, releaseyear = %s, tomatoescore = %s WHERE movieid = %s"
        values = [
            movie['title'],
            movie['director'],
            movie['releaseyear'],
            movie['tomatoescore'],
            movie['movieid']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return movie

    def delete(self, movieid):
        cursor = self.getCursor()
        sql = 'DELETE FROM movies WHERE movieid = %s'
        values = [movieid]
        cursor.execute(sql, values)
        self.db.commit()
        
        cursor.close()
        return {}




movieDao = MovieDao()