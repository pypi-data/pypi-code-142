import bs4

gen_soup = lambda s='', p='html.parser': bs4.BeautifulSoup(s, p)