import sys
from bs4 import BeautifulSoup

def extr_name(filename):
  try:
    with open(filename) as f:
      contents = f.read()
  except IOError:
    print("Error: can\'t find file or read data")
    sys.exit(2)
  
  soup = BeautifulSoup(contents, 'html.parser')
  
  name_rank_strings = [filename[-9:-5]]
  allRows = soup.find_all(align='right')
  for row in allRows:
    name_rank_strings.append(row.contents[1].text + ' ' + row.contents[0].text)
    name_rank_strings.append(row.contents[2].text + ' ' + row.contents[0].text)

  name_rank_strings.sort()
  return name_rank_strings

def get_top_10_names_from_all_files(file_global_path, files_names, woman_names = False):  
  listsOfTopNames = []
  for file_name in files_names:
    listsOfTopNames.append(get_top_10_names_from_file(file_global_path + file_name, woman_names)) 

  return listsOfTopNames
  
def get_top_10_names_from_file(file_full_path, woman_names):
  try:
    with open(file_full_path) as f:
      contents = f.read()
  except IOError:
    print("Error: can\'t find file or read data")
    sys.exit(2)
  
  soup = BeautifulSoup(contents, 'html.parser')
  allRows = soup.find_all(align='right')

  namePosition = 1
  if (woman_names):
    namePosition = 2    

  ranked_names_list = []
  for row in allRows:
    ranked_names_list.append((row.contents[0].text, row.contents[namePosition].text))

  ranked_names_list.sort(key=lambda val: int(val[0]))
  ranked_names_list.insert(0, [file_full_path[-9:-5]]) 
  return ranked_names_list[:11]