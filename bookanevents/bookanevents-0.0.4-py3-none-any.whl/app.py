
""" THis is a sample code to execute the class for reference"""


from ScrapEvent import ScrapEvent



eve1 = ScrapEvent(location='Dublin',event='Technical')


data = eve1.getData()
print(data.head())