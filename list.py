from array import array
scores = array('d')
scores.append(98)
scores.append(99)
print(scores)
print(scores[1])


names = ['Susan','Christopher']
print(len(names))
names.insert(0,'Bill')
print(names)
names.sort()
print(names)


person = {'first': 'Christopher''}
person['last'] = 'Harrison'
          print(person)
          print(person['first'])
