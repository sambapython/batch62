import unittest
from app import fun
class FunTestCases(unittest.TestCase):
	def fun(self):
		print("this is fun")
	@classmethod
	def setUpClass(cls):
		print("logging in..")
	@classmethod
	def tearDownClass(cls):
		print("log out..")
	def setUp(self):
		print("this is setup method")
	def tearDown(self):
		print("this is teardown method")
	def test_fun_10_20(self):
		print("test_fun_10_20 executing")
		exp=30
		act=fun(10,20)
		self.assertTrue(exp==act,"test_fun_10_20 failed..")
	def test_fun_10_str2(self):
		print("test_fun_10_str2 execduting..")
		exp="10str2"
		act=fun(10,"str2")
		self.assertTrue(exp==act,"test_fun_10_str2 failed.")
	def test_fun_str1_20(self):
		print("test_fun_str1_20 execduting..")
		exp="str120"
		act=fun("str1",20)
		self.assertTrue(exp==act,"test_fun_str1_20 failed.")
#unittest.main()
