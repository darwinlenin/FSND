import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import json

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
CATEGORIES_PER_PAGE = 10

'''
@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
'''
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={r"/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  # CORS Headers
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


  def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

  def paginate_categories(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * CATEGORIES_PER_PAGE
    end = start + CATEGORIES_PER_PAGE

    categories = [category.format() for category in selection]
    current_categories = categories[start:end]

    return current_categories

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def retrieve_questions():
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      if len(current_questions) == 0:
            abort(404)

      return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(Question.query.all())
      })



  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def retrieve_categories():
      selection = Category.query.order_by(Category.id).all()
      current_categories = paginate_questions(request, selection)

      if len(current_categories) == 0:
          abort(404)

      return jsonify({
          'success': True,
          'categories': current_categories,
          'total_categories': len(Category.query.all())
      })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)

      question.delete()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      return jsonify({
          'success': True,
          'deleted': question_id,
          'questions': current_questions,
          'total_questions': len(Question.query.all())
      })

    except:
      abort(422)


  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_questions():
    data = request.form
    new_question = data.get('question', None)
    new_answer = data.get('answer', None)
    new_category = data.get('category', None)
    new_difficulty = data.get('difficulty', None)

    error = False
    try:
      questions = Question(question=new_question, answer=new_answer, category=new_category,
                           difficulty=new_difficulty)
      questions.insert()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      if len(current_questions) == 0:
          abort(404)

      return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(Question.query.all())
      })
    except:
      abort(422)
    
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def search_term_questions():
    data = request.form
    search_term = data.get('searchTerm', '')
    searchQuestions = Question.query.filter(
        Question.question.ilike('%{}%'.format(search_term))).order_by('id').all()
    current_questions = paginate_questions(request, searchQuestions)

    if len(current_questions) == 0:
      abort(404)

    for question in searchQuestions:
      try:
        categories = Category.query.filter_by(id=question.category).order_by('id').all()
        current_categories = paginate_categories(request, categories)
        if categories is None:
          abort(404)

        for category in categories:
          return jsonify({
              'success': True,
              'questions': current_questions,
              'total_questions': len(searchQuestions),
              'current_category': category.type
          })

      except:
        abort(422)


  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def retrieve_questions_categories(category_id):
    category_id = Category.query.filter_by(id=category_id).order_by('id').all()
    if len(category_id) == 0:
        abort(404)
    for category in category_id:
      try:
        selection = Question.query.filter_by(
            category=category.id).order_by('id').all()
        current_questions = paginate_questions(request, selection)
        if len(current_questions) == 0:
          abort(404)
        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'current_category': category.type
        })

      except:
        abort(422)

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route("/quizzes", methods=["POST"])
  def get_question_quizz():
    req = request.form
    previous_questions = req.get('previous_questions', None)
    quiz_category = req.get('quiz_category', None)

    category_id = Category.query.filter_by(
        id=quiz_category).order_by('id').all()
    if len(category_id) == 0:
      abort(404)
    for category in category_id:
      try:
        selection = Question.query.filter(
            (Question.question != previous_questions) & (Question.category == quiz_category)).order_by('id').all()
        current_questions = paginate_questions(request, selection)
        if len(current_questions) == 0:
          abort(404)
        question = random.choice(current_questions)

        return jsonify({
            'success': True,
            'question': question,
            'previousQuestions': previous_questions,
            'currentQuestion': question
        })

      except:
        abort(422)

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
          "success": False,
          "error": 405,
          "message": "Method not Allowed"
      }), 405

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400

  @app.errorhandler(500)
  def bad_request(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500

  @app.errorhandler(503)
  def bad_request(error):
    return jsonify({
        "success": False,
        "error": 503,
        "message": "Service Unavailable"
    }), 503


  return app

    
