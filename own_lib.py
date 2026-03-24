import re 

def vuser(user):
 return re.search(r"[a-zA-Z]{2}[0-9]{2}",user)

def vopinion(opinion):
    return re.search(r"[a-zA-Z]",opinion)
