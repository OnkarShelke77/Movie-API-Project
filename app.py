from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_database.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    director = db.Column(db.String(100))
    # Add more fields as needed
    
if __name__ == '__main__':
    # Initialize the database inside the application context
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)

from flask import request, jsonify

# List all movies
@app.route('/movies', methods=['GET'])
def list_movies():
    movies = Movie.query.all()
    movie_list = []
    for movie in movies:
        movie_list.append({
            'id': movie.id,
            'title': movie.title,
            'year': movie.year,
            'director': movie.director,
            # Add more fields as needed
        })
    return jsonify({'movies': movie_list})

# Add a new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    new_movie = Movie(**data)
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({'message': 'Movie added successfully'})

# Update an existing movie
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return jsonify({'error': 'Movie not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(movie, key, value)
    db.session.commit()
    return jsonify({'message': 'Movie updated successfully'})

# Delete a movie
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return jsonify({'error': 'Movie not found'}), 404
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted successfully'})
