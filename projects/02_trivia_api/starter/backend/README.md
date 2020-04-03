# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET '/questions'
DELETE '/questions/<int:question_id>'
POST '/questions'
POST '/questions/search'
GET '/categories/<int:category_id>/questions'
POST '/quizzes'

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Fetches a dictionary of questions in which the keys are the ids and the values is the corresponding string of the question, string of the answer, integer of category and integer of difficulty
- Request Arguments: None
- Returns: An object with a key, success, that contains a object of boolean: success_boolean key:value pairs a key, a total_questions, that contains a object of id: total_questions_id key:value pairs. And a object of key: questions_array where of this inner array contains a object of question: question_string key:value pairs, answer: answer_string key:value pairs, category: category_id key:value pairs, difficulty: difficulty_id key:value pairs.
{
  "questions": [
    {
      "answer": "answer",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "hello"
    },
    {
      "answer": "second answer",
      "category": 1,
      "difficulty": 1,
      "id": 2,
      "question": "second question"
    },
    {
      "answer": "four answer",
      "category": 1,
      "difficulty": 1,
      "id": 3,
      "question": "four question"
    },
    {
      "answer": "In the year 1400",
      "category": 3,
      "difficulty": 4,
      "id": 4,
      "question": "When discover America?"
    }
  ],
  "success": true,
  "total_questions": 4
}

DELETE '/questions/<int:question_id>'
- Delete a question item in which the keys are the ids is the corresponding string of the question and fetches a dictionary of all questions in which the keys are the ids and the values is the corresponding integer of the deleted item, string of the question, string of the answer, integer of category and integer of difficulty
- Request Arguments: int:question_id
- Returns: An object with a key, success, that contains a object of boolean: success_boolean key:value pairs a key, a deleted, that contains a object of id: deleted_id key:value pairs, a key, a total_questions, that contains a object of id: total_questions_id key:value pairs. And a object of key: questions_array where of this inner array contains a object of question: question_string key:value pairs, answer: answer_string key:value pairs, category: category_id key:value pairs, difficulty: difficulty_id key:value pairs.
{
  "deleted": 3,
  "questions": [
    {
      "answer": "answer",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "hello"
    },
    {
      "answer": "second answer",
      "category": 1,
      "difficulty": 1,
      "id": 2,
      "question": "second question"
    },
    {
      "answer": "In the year 1400",
      "category": 3,
      "difficulty": 4,
      "id": 4,
      "question": "When discover America?"
    }
  ],
  "success": true,
  "total_questions": 3
}

POST '/questions'
- Fetches a dictionary of questions in which the keys are the ids and the values is the corresponding string of the question, string of the answer, integer of category and integer of difficulty
- Request Arguments: An object with a key, question, answer, category, difficulty, that contains a object of question: question_string key:value pairs, answer: answer_string key:value pairs, category: category_id key:value pairs, difficulty: difficulty_id key:value pairs.  
- Returns: An object with a success key that contains a key:success_boolean and a single total_questions element, that contains a object of key: total_questions_string key:value pairs a object of key: questions_array where of this inner array contains a object of question: question_string key:value pairs, answer: answer_string key:value pairs, category: category_id key:value pairs, difficulty: difficulty_id key:value pairs.
{
  "questions": [
    {
      "answer": "answer",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "hello"
    },
    {
      "answer": "second answer",
      "category": 1,
      "difficulty": 1,
      "id": 2,
      "question": "second question"
    },
    {
      "answer": "In the year 1400",
      "category": 3,
      "difficulty": 4,
      "id": 3,
      "question": "When discover America?"
    },
    {
      "answer": "Thomas Edison",
      "category": 6,
      "difficulty": 2,
      "id": 4,
      "question": "Who invent the incandescent bulb?"
    }
  ],
  "success": true,
  "total_questions": 4
}


POST '/questions/search'
- Fetches a dictionary of questions in which the keys are the ids and the values is the corresponding string of the question search term and listing the current category of this questions listed.
- Request Arguments: An object with a key, question that contains a object of question: question_string key:value pairs.  
- Returns: An object with a success key that contains a key:success_boolean and a key and a single current_category element, that contains a object of key: current_category_string key:value pairs a single total_questions element, that contains a object of key: total_questions_string key:value pairs a object of key: questions_array where of this inner array contains a object of question: question_string key:value pairs, answer: answer_string key:value pairs, category: category_id key:value pairs, difficulty: difficulty_id key:value pairs. 
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "second answer",
      "category": 1,
      "difficulty": 1,
      "id": 2,
      "question": "second question"
    },
    {
      "answer": "four answer",
      "category": 1,
      "difficulty": 1,
      "id": 4,
      "question": "four question"
    }
  ],
  "success": true,
  "total_questions": 2
}

GET '/categories/<int:category_id>/questions'
- Fetches a dictionary of questions based on category, only questions of that category to be shown.
- Request Arguments: An object with a key, category that contains id of the category of the questions to liest: category_id key:value pairs.  
- Returns: An object with a success key that contains a key:success_boolean and a key and a single current_category element, that contains a object of key: current_category_string key:value pairs a single total_questions element, that contains a object of key: total_questions_string key:value pairs a object of key: questions_array where of this inner array contains a object of question: question_string key:value pairs, answer: answer_string key:value pairs, category: category_id key:value pairs, difficulty: difficulty_id key:value pairs. 
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "second answer",
      "category": 1,
      "difficulty": 1,
      "id": 2,
      "question": "second question"
    },
    {
      "answer": "four answer",
      "category": 1,
      "difficulty": 1,
      "id": 4,
      "question": "four question"
    }
  ],
  "success": true,
  "total_questions": 2
}


POST '/quizzes'
- Fetches a dictionary of questions based on take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
- Request Arguments: An object with a key, category that contains id of the category of the questions to list: category_id key:value pairs and previous question parameter that contains key of the previous_question of the questions to list: previous_question_string key:value pairs.
- Returns: An object with a success key that contains a key:success_boolean and a key. A single previousQuestions element, that contains a object of key: previousQuestions_string key:value pairs. A object of key: questions_array where of this inner array contains a object of question: question_string key:value pairs, answer: answer_string key:value pairs, category: category_id key:value pairs, difficulty: difficulty_id key:value pairs. A object of key: currentQuestion_array where of this inner array contains a object of question: question_string key:value pairs, answer: answer_string key:value pairs, category: category_id key:value pairs, difficulty: difficulty_id key:value pairs. 
{
  "currentQuestion": {
    "answer": "book",
    "category": 6,
    "difficulty": 2,
    "id": 5,
    "question": "object to read many pages?"
  },
  "previousQuestions": "second question",
  "question": {
    "answer": "sea",
    "category": 6,
    "difficulty": 2,
    "id": 6,
    "question": "place to travel in a ship"
  },
  "success": true
}


```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```