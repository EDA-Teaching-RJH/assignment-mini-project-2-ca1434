import re 
from movie import questions

class testquestions(unittest.TestCase):

    def test_user(self): 
        x="qw23"
        y="er45"
        assert re.search(r"^[a-zA-Z]{2}[0-9]{2}",x)
        assert re.search(r"^[a-zA-Z]{2}[0-9]{2}",y)
    def test_notuser(self):
        a="gpn45"
        b="23ty"
        assert not re.search(r"^[a-zA-Z]{2}[0-9]{2}",a)
        assert not re.search(r"^[a-zA-Z]{2}[0-9]{2}",b)

    def test_opinion(self):
        c="Amazing"
        d="ok"
        assert re.search(r"^[a-zA-Z]",c)
        assert re.search(r"^[a-zA-Z]",d)
    def test_notopinion(self):
        e="12345567"
        f=""
        assert not re.search(r"^[a-zA-Z]",e)
        assert not re.search(r"^[a-zA-Z]",f)
