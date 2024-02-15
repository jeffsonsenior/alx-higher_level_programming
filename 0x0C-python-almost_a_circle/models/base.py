#!/usr/bin/python3
'''modules for base class'''

class Base:
        ''' a representation of the to our OOP hierarchy'''
      
	_nb_objects = 0

	def_int_(self, id=None):
	'''contractor'''
	if id is not None:
 		self.id =id
	else:
		Base._nb_objects += 1
		self.id = Base._nb_objects

