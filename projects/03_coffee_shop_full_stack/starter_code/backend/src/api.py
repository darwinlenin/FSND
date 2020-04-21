import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
#db_drop_and_create_all()


## ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks')
def retrieve_drinks():
    drinks = Drink.query.all()

    if drinks is None:
        abort(404)
    
    return jsonify({
        "success": True,
        "drinks": [drink.short() for drink in drinks]
    }), 200

'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def retrieve_drinks_detail():
    drinks_detail = Drink.query.all()

    return jsonify({
        "suceess": True,
        "drinks": [drink.short() for drink in drinks_detail]
    }), 200

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drinks():
    data = request.get_json()
    print(data)
    recipe = data['recipe']

    if isinstance(recipe, dict):
        recipe = [recipe]

    drink = Drink()
    drink.title = data['title']
    drink.recipe = json.dumps(recipe)
    drink.insert()
    return jsonify({
        'success': True,
        'drinks': [drink.long()]})

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(id):
    data = request.get_json()

    drink = Drink.query.filter(Drink.id == id).one_or_none()

    if not drink:
        abort(404)

    drink.recipe = data.get("recipe", drink.recipe)
    drink.title = data.get("title", drink.title)

    if isinstance(drink.recipe, list):
        drink.recipe = json.dumps(drink.recipe)

    drink.update()
    return jsonify({
        "success": True,
        "drinks": drink.long()
    }),  200

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(id):
    drink = Drink.query.filter(Drink.id == id).one_or_none()
    if not drink:
        abort(404)

    drink.delete()

    return jsonify({
        "success": True,
        "delete": id
    })

## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
@app.errorhandler(405)
def method_not_allowed(error):
      return jsonify({
          "success": False,
          "error": 405,
          "message": "Method not Allowed"
      }), 405

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

'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''
@app.errorhandler(401)
def permission_error(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Authentication error"
    }), 401


@app.errorhandler(401)
def permission_error(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Authentication error"
    }), 401

@app.errorhandler(403)
def user_error(error):
    return jsonify({
        "sucess": False,
        "error": 403,
        "message": error.description
    }), 403
