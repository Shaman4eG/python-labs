import business_logic
from flask import Flask, jsonify, abort, request
from diffuculty_level import DiffucultyLevel

app = Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/get_image', methods=['GET'])
def init_game():
  #difficulty_level = DiffucultyLevel.EASY
  difficulty = int(request.args.get('difficulty'))

  b_logic = business_logic.BusinessLogic()
  success = b_logic.init_database()
  if (not success): abort(500)
    
  image_to_guess = b_logic.init_game(difficulty)
  return image_to_guess

@app.route('/check_answer', methods=['POST'])
def check_answer():
  answer = request.get_json()

  b_logic = business_logic.BusinessLogic()
  isCorrect = b_logic.check_answer(answer['answer'])
  return jsonify(result = isCorrect)
  
app.run()