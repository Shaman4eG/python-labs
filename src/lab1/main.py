import string2
import list1

def main():
  test_string2_v()
  test_string2_nb()
  test_list1_me()
  test_list1_fx()
  test_list1_sort_list_by_last_element_of_tuple()
  
def test_string2_v():
  print()
  print()
  print('#############################################')
  print('============ TESTING "string2.v" ============')
  print('=============================================')
  print('In: ing -> Out: ' + string2.v('ing'))
  print('In: war -> Out: ' + string2.v('war'))
  print('In: starting -> Out: ' + string2.v('starting'))
  print('In: finish -> Out: ' + string2.v('finish'))

def test_string2_nb():
  print()
  print()
  print('#############################################')
  print('============ TESTING "string2.nb" ===========')
  print('=============================================')
  print('In: This music is not so bad! -> Out: ' + string2.nb('This music is not so bad!'))

def test_list1_me():
  list = ['itmoi', 'is', 'thet', 'capital', 'of', 'Great', 'Britain']
  
  print()
  print()
  print('#############################################')
  print('============ TESTING "list1.me" ============')
  print('=============================================')
  print('In: [' +  ', '.join(list) + '] -> Out: ' + str(list1.me(list)))

def test_list1_fx():
  list = ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']

  print()
  print()
  print('#############################################')
  print('============ TESTING "list1.fx" ============')
  print('=============================================')
  print('In: [' +  ', '.join(list) + '] -> Out: [' +  ', '.join(list1.fx(list)) + ']')

def test_list1_sort_list_by_last_element_of_tuple():
  list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

  print()
  print()
  print('###########################################################################')
  print('============ TESTING "list1.sort_list_by_last_element_of_tuple" ===========')
  print('===========================================================================')
  print('In: [' +  ', '.join(map(str, list)) + '] -> Out: [' +  ', '.join(map(str, list1.sort_list_by_last_element_of_tuple(list))) + ']')

if __name__ == '__main__':
  main()