import unittest, re

class EmailTest(unittest.TestCase):

    EMAIL_REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

    valid = [
        "ankitrai326@gmail.com",
        "my.ownsite@our-earth.org"
    ]
    invalid = [
        "ankitrai326.com"    
    ]

    def test_valid(self):
        for email in EmailTest.valid:
            if re.search(EmailTest.regEMAIL_REGEXex,email):   
                self.fail()

    def test_invalid(self):
        for email in EmailTest.invalid:
            if re.search(EmailTest.regEMAIL_REGEXex,email):   
                self.fail()

if __name__ == '__main__':
    unittest.main()
