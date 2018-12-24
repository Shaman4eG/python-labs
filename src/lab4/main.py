import sys 
import os
from text_generator import TextGenerator

def main(file_global_path):
  file_name = sys.argv[1:2]
  if not file_name:
    print('File name not provided')
    sys.exit(1)
  file_name = file_name[0]

  text_generator = TextGenerator()
  generate_text_from_file(text_generator, file_global_path + file_name)
  generate_text_from_previous_text(text_generator)

  
def generate_text_from_file(text_generator, file_name):
  text_generator.generate_dictionary(generate_from_file = True, file_name = file_name)  
  text_generator.generate_new_text_from_dictionary()
  
  print('\n############')
  print('Generation 0')
  print('\nGenerated dictionary:')
  for key in text_generator.similar_dictionary.keys():
    print(key + ': ' + str(text_generator.similar_dictionary[key]))

  print('\nGenerated text:\n' + text_generator.last_generated_text)


def generate_text_from_previous_text(text_generator):
  for i in range(1, 3):
    text_generator.generate_dictionary()
    text_generator.generate_new_text_from_dictionary()

    print('\n############')
    print('Generation ' + str(i))
    print('\nGenerated dictionary:')
    for key in text_generator.similar_dictionary.keys():
      print(key + ': ' + str(text_generator.similar_dictionary[key]))

    print('\nGenerated text:\n' + text_generator.last_generated_text)


if __name__ == '__main__':
  main(os.getcwd() + '\\src\\lab4\\')