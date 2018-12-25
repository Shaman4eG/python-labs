import os
import sqlite3
import glob
import random
import base64
from google_images_download import google_images_download
from diffuculty_level import DiffucultyLevel


class BusinessLogic:

  def init_database(self):
    try:
      with open(os.getcwd() + '\\src\\lab5\\back_end\\guess.txt') as f:
        names = f.read()
    except IOError:
      return False

    self.create_tables_and_add_initial_data(names)

    return True


  def init_game(self, difficulty):
    name_to_guess = self.create_name_to_guess(difficulty)
    self.find_and_save_images(name_to_guess)
    image_path = self.get_random_image_path_of_given_person(name_to_guess)
    base64_encoded_string = self.convert_to_base64_string(image_path)

    return base64_encoded_string


  def check_answer(self, answer):
    name_to_guess = self.get_name_to_guess()[0].lower()
    answer = answer.lower()

    return answer == name_to_guess

  def create_tables_and_add_initial_data(self, names):
    os.chdir(os.getcwd() + '\\src\\lab5\\database')
    connectionToDb = sqlite3.connect('names.db')
    cursor = connectionToDb.cursor()

    cursor.execute('DROP TABLE IF EXISTS names')
    cursor.execute('CREATE TABLE names (rank, name)')
    for rank, name in enumerate(names.split('\n')):
      rank += 1
      cursor.execute('INSERT INTO names VALUES (' + str(rank) + ', "' + name + '")')

    cursor.execute('DROP TABLE IF EXISTS name_to_guess')
    cursor.execute('CREATE TABLE name_to_guess (name)')

    connectionToDb.commit()
    connectionToDb.close()
    os.chdir(os.getcwd() + '\\..\\..\\..')


  def create_name_to_guess(self, difficulty):
    os.chdir(os.getcwd() + '\\src\\lab5\\database')
    connectionToDb = sqlite3.connect('names.db')
    cursor = connectionToDb.cursor()

    if (difficulty == DiffucultyLevel.EASY.value): rankLimit = 11
    elif (difficulty == DiffucultyLevel.MEDIUM.value): rankLimit = 51
    else: rankLimit = 101
      
    cursor.execute('SELECT name FROM names WHERE rank < ' + str(rankLimit))
    all_names_for_given_difficulty = cursor.fetchall()
    name_to_guess = random.choice(all_names_for_given_difficulty)

    cursor.execute('INSERT INTO name_to_guess VALUES ("' + name_to_guess[0] + '")')

    connectionToDb.commit()
    connectionToDb.close()
    os.chdir(os.getcwd() + '\\..\\..\\..')

    return name_to_guess[0]


  def find_and_save_images(self, name):
    # Если картинки уже закэшированы для этого человека, то не скачиваем их.
    if (os.path.isdir(os.getcwd() + '\\src\\lab5\\downloaded_images\\' + name)):
      return

    images_loader = google_images_download.googleimagesdownload()

    arguments = {
      "keywords": name,
      "limit": 3,
      "output_directory": os.getcwd() + '\\src\\lab5\\downloaded_images',
      "delay": 0.1,
      "format": 'jpg'
    }   
    images_loader.download(arguments)


  def get_random_image_path_of_given_person(self, name):
    images = glob.glob(os.getcwd() + '\\src\\lab5\\downloaded_images\\' + name + '\\*')
    return str(random.choice(images))
    

  def convert_to_base64_string(self, image_path):
    with open(image_path, "rb") as image_file:
      encoded_data = str(base64.b64encode(image_file.read()))[2:-1]

    base64_encoded_string = (
      "data:" + 
      "image/jpeg;" +
      "charset=utf-8;" +
      "base64," + encoded_data
    )

    return base64_encoded_string


  def get_name_to_guess(self):
    os.chdir(os.getcwd() + '\\src\\lab5\\database')
    connectionToDb = sqlite3.connect('names.db')
    cursor = connectionToDb.cursor()

    cursor.execute('SELECT name FROM name_to_guess')
    name_to_guess = cursor.fetchone()

    connectionToDb.close()
    os.chdir(os.getcwd() + '\\..\\..\\..')

    return name_to_guess