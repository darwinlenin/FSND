import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actors, Movies
from wtforms.ext import dateutil
import babel
from flask_wtf import FlaskForm
from forms import *
from flask.templating import render_template
import sys
from flask.helpers import flash

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  db = setup_db(app)
  CORS(app)

  return app

app = create_app()

# TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')

#  Movies
#  ----------------------------------------------------------------

@app.route('/movies')
def movies():
  # TODO: replace with real movies data.
  #       num_movies should be aggregated based on number of upcoming movies per actor.
  '''data=[{
    "city": "San Francisco",
    "state": "CA",
    "movies": [{
      "id": 1,
      "name": "The Musical Hop",
      "num_upcoming_movies": 0,
    }, {
      "id": 3,
      "name": "Park Square Live Music & Coffee",
      "num_upcoming_movies": 1,
    }]
  }, {
    "city": "New York",
    "state": "NY",
    "movies": [{
      "id": 2,
      "name": "The Dueling Pianos Bar",
      "num_upcoming_movies": 0,
    }]
  }] '''
  data = []
  movies = []

  movie_list = Movies.query.with_entities(
      Movies.id,Movies.title, Movies.release_date).order_by('id').all()
  '''print('movie_list!', movie_list)'''

  for movie in movie_list:
      data.append({"id": movie.id,
        "title": movie.title,
        "release_date": movie.release_date})
    
  #print('data!', data)

  return render_template('pages/movies.html', areas=data);

def function(json_object, name, key):
    for dict in json_object:
        if dict[key] == name:
            return True

#  Create Movie
#  ----------------------------------------------------------------

@app.route('/movies/create', methods=['GET'])
def create_movie_form():
  form = MovieForm()
  return render_template('forms/new_movie.html', form=form)


@app.route('/movies/create', methods=['POST'])
def create_movie_submission():
  # TODO: insert form data as a new Movie record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  title = request.form['title']
  release_date = request.form['release_date']
  facebook_link = request.form['facebook_link']
  image_link = request.form['image_link']
  website = request.form['website']
  seeking_talent = request.form['seeking_talent']
  seeking_description = request.form['seeking_description']
  if(seeking_talent == "True"):
    seeking_talent = bool(seeking_talent)
  else:
    seeking_talent = bool()


  error = False
  try:
    movie = Movies(title=title, release_date=release_date)
    movie.insert()
  except:
    error = True
    print(sys.exc_info())
  if error:
    flash('An error occurred. Movie ' + movie.title + ' could not be listed.')
  else:
    flash('Movie ' + request.form['title'] + ' was successfully listed!')

  # on successful db insert, flash success
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.route('/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  error = False
  try:
    '''Show.query.filter_by(movie_id=movie_id).delete()'''
    Movie.query.filter_by(id=movie_id).delete()
    db.session.commit()
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if error:
    flash('An error occurred. Movie could not be removed.')
    return redirect(url_for('index'))
  else:
    flash('Movie was successfully removed!')
    return redirect(url_for('index'))

  # BONUS CHALLENGE: Implement a button to delete a Movie on a Movie Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return render_template('pages/home.html')


#  Actors
#  ----------------------------------------------------------------

@app.route('/actors')
def actors():
  # TODO: replace with real actors data.
  #       num_actors should be aggregated based on number of upcoming movies per actor.
  '''data=[{
    "city": "San Francisco",
    "state": "CA",
    "actors": [{
      "id": 1,
      "name": "The Musical Hop",
      "num_upcoming_movies": 0,
    }, {
      "id": 3,
      "name": "Park Square Live Music & Coffee",
      "num_upcoming_movies": 1,
    }]
  }, {
    "city": "New York",
    "state": "NY",
    "movies": [{
      "id": 2,
      "name": "The Dueling Pianos Bar",
      "num_upcoming_movies": 0,
    }]
  }] '''
  data = []
  actors = []

  actor_list = Actors.query.with_entities(
      Actors.name, Actors.age, Actors.gender).order_by('id').all()
  #print('actor_list!', actor_list)

  for actor in actor_list:
    if (not function(data, actor.name,"name")):
      actors = []
      data.append({"name": actor.name,
                    "age": actor.age,
                    "gender": actor.gender})

  return render_template('pages/actors.html', areas=data);


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

