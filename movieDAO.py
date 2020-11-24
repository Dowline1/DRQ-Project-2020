import mysql.connector

class MovieDao:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'datarepresentation'
        )
        print("Connected")

    def create(self, movie):
        cursor = self.db.cursor()
        sql = "INSERT INTO movies (title, director, releaseyear, tomatoescore) values (%s,%s,%s,%s)"
        values = [
            movie['title'],
            movie['director'],
            movie['releaseyear'],
            movie['tomatoescore']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM movies'
        cursor.execute(sql)
        results = cursor.fetchall()
        
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            
            returnArray.append(resultAsDict)

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
        cursor = self.db.cursor()
        sql = 'SELECT * FROM movies WHERE movieid = %s'
        values = [movieid]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        
        return self.convertToDict(result)

    def update(self, movie):
        cursor = self.db.cursor()
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
        return movie

    def delete(self, movieid):
        cursor = self.db.cursor()
        sql = 'DELETE FROM movies WHERE movieid = %s'
        values = [movieid]
        cursor.execute(sql, values)
        self.db.commit()
        
        return {}




movieDao = MovieDao()