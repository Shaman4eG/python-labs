import business_logic
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/cache_rss_and_return_it', methods=['POST'])
def cache_rss_and_return_it():
  link = request.get_json()

  b_logic = business_logic.BusinessLogic()
  rss_feed = b_logic.cache_rss_and_return_it(link['link'])

  return jsonify(articles = rss_feed)
  #difficulty_level = DiffucultyLevel.EASY
  # difficulty = int(request.args.get('difficulty'))

  # b_logic = business_logic.BusinessLogic()
  # success = b_logic.init_database()
  # if (not success): abort(500)
    
  # image_to_guess = b_logic.init_game(difficulty)
  # return image_to_guess

@app.route('/check_answer', methods=['POST'])
def check_answer():
  answer = request.get_json()

  b_logic = business_logic.BusinessLogic()
  isCorrect = b_logic.check_answer(answer['answer'])
  return jsonify(result = isCorrect)
  
app.run()