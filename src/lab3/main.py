import sys
import os
import names_ranks_parser

# To pass args either:
# - modify launch.json
# - or use command in cmd: python "C:\Users\daniel\Desktop\Uni\4 курс\python\python_labs\src\lab3\main.py" args
def main(file_global_path):
  files_names = sys.argv[1:]
  if not files_names:
    print('Files names not provided')
    sys.exit(1)
  
  for file_name in files_names:
    name_rank_strings = names_ranks_parser.extr_name(file_global_path + file_name)
    print(name_rank_strings)
    print()

  top_10_names = names_ranks_parser.get_top_10_names_from_all_files(file_global_path, files_names)
  for _list in top_10_names:
    print('\nMen\'s TOP 10 names for year ' + str(_list[0]))
    for name in _list[1:]:
      print(name)

  top_10_names = names_ranks_parser.get_top_10_names_from_all_files(file_global_path, files_names, True)
  for _list in top_10_names:
    print('\nWomen\'s TOP 10 names for year ' + str(_list[0]))
    for name in _list[1:]:
      print(name)


if __name__ == '__main__':
  main(os.getcwd() + '\\src\\lab3\\')