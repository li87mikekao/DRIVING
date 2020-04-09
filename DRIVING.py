__county__ = input('國家: ')
__age__ = input('年齡: ')
__age__ = int(__age__)
if __county__ == 'TW':
  if __age__ >= 18:
    print('可以考駕照!')
  else:
    print('不可以考駕照!')
elif __county__ =='US':
  if __age__ >= 16:
    print('可以考駕照!')
  else:
    print('不可以考駕照!')
else:
	print('??')