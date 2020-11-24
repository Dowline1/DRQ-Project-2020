from flask import Flask, url_for, request, redirect, abort, jsonify
from movieDAO import movieDao

app = Flask(__name__, static_url_path = '', static_folder = 'staticpages')

@app.route('/')
def index():
    return "Hello"

# Get All
@app.route('/movies')
def getAll():
    return jsonify(movieDao.getAll())

# Find by ID
@app.route('/movies/<int:movieid>')
def findById(movieid):
    return jsonify(movieDao.findById(movieid))

# Create
@app.route('/movies', methods = ['POST'])
def create():
    if not request.json:
        abort(400)

    movie = {
        "title": request.json["title"],
        "director": request.json["director"],
        "releaseyear": request.json["releaseyear"],
        "tomatoescore": request.json["tomatoescore"],
    }
    return jsonify(movieDao.create(movie))

# Update
@app.route('/movies/<int:movieid>', methods = ['PUT'])
def update(movieid):
    foundmovie = movieDao.findById(movieid)
    if foundmovie == {}:
        return jsonify({}), 404
    currentMovie = foundmovie
    if 'title' in request.json:
        currentMovie['title'] = request.json['title']
    if 'director' in request.json:
        currentMovie['director'] = request.json['director']
    if 'releaseyear' in request.json:
        currentMovie['releaseyear'] = request.json['releaseyear']
    if 'tomatoescore' in request.json:
        currentMovie['tomatoescore'] = request.json['tomatoescore']
    movieDao.update(currentMovie)

    return jsonify(currentMovie)
    
# Delete
@app.route('/movies/<int:movieid>', methods = ['DELETE'])
def delete(movieid):
    movieDao.delete(movieid)

    return jsonify({"Done": True})


if __name__ == "__main__":
    app.run(debug = True)
    