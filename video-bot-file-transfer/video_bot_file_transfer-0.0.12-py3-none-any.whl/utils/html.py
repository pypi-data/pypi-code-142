import cgi
def unescape_text(text):
    
    extags=cgi.escape(text)
    return extags
  

