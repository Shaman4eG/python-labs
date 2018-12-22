# 1. 
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему
def me(words):
  count = 0
  for word in words:
    if (len(word) > 2 and word[0] == word[len(word) - 1]):
      count += 1
  return count

# 2. 
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
  result_list = words
  xlist = []

  for word in result_list:
    if word[0] == 'x':
      xlist.append(word)
      result_list.remove(word)

  xlist.sort()
  result_list.sort()
  xlist.extend(result_list)

  return xlist

# 3. 
# Вх: список непустых кортежей, 
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def sort_list_by_last_element_of_tuple(list_of_tuples):
  list_of_tuples.sort(key = lambda e: e[len(e) - 1])
  return list_of_tuples