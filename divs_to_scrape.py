






from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<div class="notranslate ratingNum">4.4</div>'
'<div class="empInfo cf p notranslate"> <strong>Size</strong> <span class="empData">10000+ Employees</span> </div>'
'<div class="empInfo cf p notranslate"> <strong>Founded</strong> <span class="empData"> 1998</span> </div>'
'<div class="empInfo cf p notranslate"> <strong>Revenue</strong> <span class="empData"> $10+ billion (USD) per year</span> </div>')
