# 1. 
# Вх: строка. Если длина > 3, добавить в конец "ing", 
# если в конце нет уже "ing", иначе добавить "ly".
def v(s):
  if (len(s) > 3 and s[-3:] != 'ing'):
    return s + 'ing'
  else:
    return s + 'ly'


# 2. 
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!
def nb(s):
  not_position = s.find('not')
  bad_position = s.find('bad')
  return s[:not_position] + 'good' + s[bad_position + 3:]