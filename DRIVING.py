__county__ = input('國家: ')
__age__ = input('年齡: ')
__age__ = int(__age__)
if __county__ == '台灣':
  if __age__ >= 18:
    print('可以考駕照!')
  else:
    print('不可以考駕照!')
