import unittest
import controllers

from app import app

client = app.test_client()


class Test(unittest.TestCase):
	def setUp(self):
		pass
	
	@unittest.skip('skip')	
	def test_main(self):
		pass
	
	def test_support_func_slugify(self):
		res1 = controllers.slugify('title test')
		res2 = controllers.slugify('4title4 test!!')
		
		self.assertEqual(res1, 'title-test')
		self.assertEqual(res2, '4title4-test--')
		
		
if __name__ == '__main__':
	print(controllers.slugify(''))
	unittest.main()