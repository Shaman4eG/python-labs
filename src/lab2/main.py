import string1
import list2

def main():
  test_string1_num_of_items()
  test_string1_start_end_symbols()
  test_string1_replace_char()
  test_string1_str_mix()
  test_list2_rm_adj()
  test_list2_merge_lists_and_sort_in_ascending_order()

def test_string1_num_of_items():
  print()
  print()
  print('#######################################################')
  print('============ TESTING "string1.num_of_items" ===========')
  print('=======================================================')
  print('In: 5 -> Out: ' + string1.num_of_items(5))
  print('In: 10 -> Out: ' + string1.num_of_items(10))

def test_string1_start_end_symbols():
  print()
  print()
  print('#########################################################################')
  print('============ TESTING "string1.test_string1_start_end_symbols" ===========')
  print('=========================================================================')
  print('In: welcome -> Out: ' + string1.start_end_symbols('welcome'))

def test_string1_replace_char():
  print()
  print()
  print('#######################################################')
  print('============ TESTING "string1.replace_char" ===========')
  print('=======================================================')
  print('In: bibble -> Out: ' + string1.replace_char('bibble'))

def test_string1_str_mix():
  print()
  print()
  print('##################################################')
  print('============ TESTING "string1.str_mix" ===========')
  print('==================================================')
  print('In: max, pid -> Out: ' + string1.str_mix('max', 'pid'))
  print('In: dog, dinner -> Out: ' + string1.str_mix('dog', 'dinner'))

def test_list2_rm_adj():
  list = [0, 2, 2, 3]
  
  print()
  print()
  print('################################################')
  print('============ TESTING "list2.rm_adj" ============')
  print('================================================')
  print('In: ' +  str(list) + ' -> Out: ' + str(list2.rm_adj(list)))

def test_list2_merge_lists_and_sort_in_ascending_order():
  list0 = [1, 5, 7]
  list1 = [2, 3, 6]
  
  print()
  print()
  print('#################################################################################')
  print('============ TESTING "list2.merge_lists_and_sort_in_ascending_order" ============')
  print('=================================================================================')
  print('In: list1: ' +  str(list0) + ' list2: '+ str(list1) + ' -> Out: ' + str(list2.merge_lists_and_sort_in_ascending_order(list0, list1)))

main()