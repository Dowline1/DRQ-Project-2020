from flask import Flask, url_for, request, redirect, abort, jsonify, session
from movieDAO import movieDao
from castDAO import castDao

app = Flask(__name__, static_url_path = '', static_folder = 'staticpages')

# Login Key
app.secret_key = 'dowline1SecureKey'

# Redirects User to index.html
#@app.route('/')
#def home():
#
#    if not 'username' in session:
#        return redirect(url_for('login'))
#    
#    return app.send_static_file('index.html')

@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('loginPage'))
    
    if 'username' in session:
        return app.send_static_file('index.html')


# Redirects User to login.html
@app.route('/login')
def loginPage():
    return app.send_static_file('login.html')

# Update session username
@app.route('/processlogin/<string:myUser>')
def proccess_login(myUser):

    session['username']= myUser
    return redirect(url_for('home'))

# Logout
@app.route('/logout')
def logout():
    session.pop('username',None)
    return app.send_static_file('login.html')


# Movie Get All
@app.route('/movies')
def moviegetAll():
    return jsonify(movieDao.getAll())

# Movie Find by ID
@app.route('/movies/<int:movieid>')
def moviefindById(movieid):
    return jsonify(movieDao.findById(movieid))

# Movie Create
@app.route('/movies', methods = ['POST'])
def moviecreate():
    if not request.json:
        abort(400)

    movie = {
        "title": request.json["title"],
        "director": request.json["director"],
        "releaseyear": request.json["releaseyear"],
        "tomatoescore": request.json["tomatoescore"],
    }
    return jsonify(movieDao.create(movie))

# Movie Update
@app.route('/movies/<int:movieid>', methods = ['PUT'])
def movieupdate(movieid):
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
    
# Movie Delete
@app.route('/movies/<int:movieid>', methods = ['DELETE'])
def moviedelete(movieid):
    movieDao.delete(movieid)

    return jsonify({"Done": True})





# Cast Get All
@app.route('/cast')
def castgetAll():
    return jsonify(castDao.getAll())

# Cast Find by ID
@app.route('/cast/<int:castid>')
def castfindById(castid):
    return jsonify(castDao.findById(castid))

# Cast Create
@app.route('/cast', methods = ['POST'])
def castcreate():
    if not request.json:
        abort(400)

    cast = {
        "movieid": request.json["movieid"],
        "actor": request.json["actor"],
        "rating": request.json["rating"],
    }
    return jsonify(castDao.create(cast))

# Cast Update
@app.route('/cast/<int:castid>', methods = ['PUT'])
def castupdate(castid):
    foundcast = castDao.findById(castid)
    if foundcast == {}:
        return jsonify({}), 404
    currentCast = foundcast
    if 'movieid' in request.json:
        currentCast['movieid'] = request.json['movieid']
    if 'actor' in request.json:
        currentCast['actor'] = request.json['actor']
    if 'rating' in request.json:
        currentCast['rating'] = request.json['rating']
    castDao.update(currentCast)

    return jsonify(currentCast)
    
# Cast Delete
@app.route('/cast/<int:castid>', methods = ['DELETE'])
def castdelete(castid):
    castDao.delete(castid)

    return jsonify({"Done": True})




if __name__ == "__main__":
    app.run(debug = True)
    