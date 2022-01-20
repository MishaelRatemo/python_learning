import unittest # Importing the unittest module
from contact import Contact # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_contact = Contact("Maxwell","Mishael","0712345678","mishael@ms.com") # create contact object


    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''

            self.assertEqual(self.new_contact.first_name,"Maxwell")
            self.assertEqual(self.new_contact.last_name,"Mishael")
            self.assertEqual(self.new_contact.phone_number,"0712345678")
            self.assertEqual(self.new_contact.email,"mishael@ms.com")


if __name__ == '__main__':
     unittest.main()