# 1. 
# Вх: список чисел, Возвр: список чисел, где 
# повторяющиеся числа урезаны до одного 
# пример [0, 2, 2, 3] returns [0, 2, 3]. 
def rm_adj(nums):
  return list(set(nums))

# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список 
def merge_lists_and_sort_in_ascending_order(list0, list1):
  merged_lists = list0 + list1
  merged_lists.sort()
  return merged_lists