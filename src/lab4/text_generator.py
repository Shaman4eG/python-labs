import sys
import random

class TextGenerator:
  'Creates text from dictionary. Dictionary is generated from previous text.'
  
  similar_dictionary = {}
  last_generated_text = ''

  def generate_dictionary(self, generate_from_file = False, file_name = ''):
    self.similar_dictionary = {}
    if (generate_from_file):
      try:
        with open(file_name) as f:
          contents = f.read()
      except IOError:
        print("Error: can\'t find file or read data")
        sys.exit(2)
    else:
      contents = self.last_generated_text

    if (contents == ''): return

    words = contents.split()
    for index, word in enumerate(words[:-1]):
      if word not in self.similar_dictionary:
        self.similar_dictionary[word] = words[index + 1:]
    self.similar_dictionary[ words[len(words) - 1] ] = []


  def generate_new_text_from_dictionary(self):
    if not self.similar_dictionary: return

    next_word = random.choice( list( self.similar_dictionary.keys() ) )
    new_text = [next_word]

    while True:
      if not self.similar_dictionary[next_word]: break

      next_word = random.choice(self.similar_dictionary[next_word])
      new_text.append(next_word)
    
    self.last_generated_text = ' '.join(new_text)

