import re 
from movie import questions

class testquestions(unittest.TestCase):

    def test_user(self): 
        x="qw23"
        y="er45"
        assert re.search(r"^[a-zA-Z]{2}[0-9]{2}",x)
        assert re.search(r"^[a-zA-Z]{2}[0-9]{2}",y)
    def test_nuser(self):
        x="gpn45"
        y="23ty"
        assert not re.search(r"^[a-zA-Z]{2}[0-9]{2}",x)
        assert not re.search(r"^[a-zA-Z]{2}[0-9]{2}",y)

    def test_opinion(self):
