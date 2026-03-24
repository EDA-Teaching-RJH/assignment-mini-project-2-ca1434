import re 
import unittest 
from Movie import questions

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
        g=8
        h=2
        self.assertTrue( 1<=g<=10)
        self.assertTrue( 1<=h<=10)

    def test_notrating(self):
        i=15
        j=0
        self.assertFalse( 1<=i<=10)
        self.assertFalse( 1<=j<=10)

    def test_save(self):
     try:
        s=questions("er66","spiderman","Amazing","10")
        s.save()
        with open("review.txt","r")as f:
            content = f.read()
            self.assertIn("er66",content)
            self.assertIn("spiderman",content)
            self.assertIn("Amazing",content)
            self.assertIn("10",content)
     except FileNotFoundError:
        self.fail("file not found")

    def test_delete(self): 
     try:
        p=questions("fh97","Ironman","good","9")
        p.save()
        p.delete()
        with open ("review.txt","r") as f:
             content = f.read()
             self.assertNotIn("fh97",content)
             self.assertNotIn("Ironman",content)
             self.assertNotIn("good",content)
             self.assertNotIn("9",content)
     except FileNotFoundError:
        print("file not found")

if __name__=="__main__":
    unittest.main()