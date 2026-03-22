import re 
import unittest 
from movie import questions

class testquestions(unittest.TestCase):

    def test_user(self): 
        x="qw23"
        y="er45"
        self.assertTrue (re.search(r"^[a-zA-Z]{2}[0-9]{2}",x))
        self.assertTrue(re.search(r"^[a-zA-Z]{2}[0-9]{2}",y))
    def test_notuser(self):
        a="gpn45"
        b="23ty"
        self.assertFalse( re.search(r"^[a-zA-Z]{2}[0-9]{2}",a))
        self.assertFalse( re.search(r"^[a-zA-Z]{2}[0-9]{2}",b))

    def test_opinion(self):
        c="Amazing"
        d="ok"
        self.assertTrue (re.search(r"^[a-zA-Z]",c))
        self.assertTrue( re.search(r"^[a-zA-Z]",d))
    def test_notopinion(self):
        e="12345567"
        f=""
        self.assertFalse( re.search(r"^[a-zA-Z]",e))
        self.assertFalse( re.search(r"^[a-zA-Z]",f))
    
    def test_rating(self):
        g="8"
        h="2"
        self.assertTrue( 1<=g<=10)
        self.assertTrue( 1<=h<=10)

    def test_notrating(self):
        i="15"
        j="0"
        self.assertTrue( 1<=i<=10)
        self.assertTrue( 1<=j<=10)
