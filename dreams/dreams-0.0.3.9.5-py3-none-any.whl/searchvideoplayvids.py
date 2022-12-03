from bs4 import BeautifulSoup as bs
import requests as rq

import mechanicalsoup as mec
import re

br = mec.StatefulBrowser()
#br.set_handle_robots(False)
#user_agent = {
#        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) >
#                      'Chrome/61.0.3163.100 Safari/537.36'}

#br.set_user_agent(
#url_test='https://yandex.ua/video/touch/preview/?text=%D0%A1%D0%BC%D0%BE%D1%82%D1%80%D0%B8%D1%82%D0%B5%20%D0%BF%D0%BE%D1%80%D0%BD%D0%BE%20%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B6%D0%BE%D0%BF%D0%B0%D1%8F%20%D0%BF%D1%8B%D1%88%D0%BA%D0%B0%20%D1%81%20%D0%BE%D0%B3%D1%80%D0%BE%D0%BC%D0%BD%D1%8B%D0%BC%D0%B8%20%D0%B4%D0%BE%D0%B9%D0%BA%D0%B0%D0%BC%D0%B8%20%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B8%D0%BB%D0%B0%20%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5%20%D1%81%D1%82%D1%80%D0%B0%D1%81%D1%82%D0%B8.&filmId=5643814182587913559&url=http%3A%2F%2Fporn0sex.vip%2Fvideos%2Fkrasivoe-porno-s-polnoy-devushkoy%2F'


headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'}
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

br.session.headers = headers
br.session.headers.update(headers)

def get_porn_div(query,num=20,lang='pt-BR'):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko), Chrome/61.0.3163.100 Safari/537.36'}
	
	#br.addheaders = headers

	#query = '%20'.join(query.split(' '))
	list_div_content = []
	list_div_info = []
#url_test='https://pornoklad.me/videos/pyshnaya-mamka-s-seksualnymi-formami/'
	
#	print(f'page n:{i}')
	url_base='https://www.playvids.com'
	url = f'{url_base}/videos?q={query}'

	url_html = br.get(url)
	url_html.raise_for_status()
	url_html = url_html.text
#	print(url_html)
	html_parser = bs(url_html,features="html.parser")
	print(html_parser)

	list_div_content = html_parser.find_all('div',{'class':"card-body"})
	list_div_img = html_parser.find_all('div',{'class':'card-img'})
	list_div_duration = html_parser.find_all('span',{'class':'duration'})



	list_div = html_parser.find_all('div')
	print(len(list_div))
	
	list_video=[]
	for i in range(len(list_div)):
		if list_div[i].attrs.get('class'):
			if 'itemVideo' in list_div[i].attrs.get('class'):
				#print(list_div[i])
				print(f'duration: {list_div[i].find("span",{"class":"duration"}).text}')
				print(f'img: {list_div[i].find("img")["src"]}')
				print(f'href: {url_base}{list_div[i].find("a")["href"]}')	
				print(f'title: {list_div[i].find("img")["alt"]}')
				video = {'title':list_div[i].find("img")["alt"],
					'duration':list_div[i].find('span',{'class':'duration'}).text,
					'imgUrl':list_div[i].find('img')['src'],
					'url':list_div[i].find('a')['href']
					}
#print(list_div[i])
				list_video.append(video)
	print(len(list_video))
	return list_video
#	print('img',len(list_div_img))
#	print(list_div_content)
	#list_div_info += html_parser.find_all('div',{'class':'mbunder'})
	#list_div += html_parser.find_all('div',{'class':"serp-item2__info-meta-item"})
#	print(len(list_div_duration))

'''
	list_href_videos = []
	for i in range(len(list_div_content)-1):
		print()
		print(f'href: {url_base}{list_div_content[i].find("a")["href"]}')
		print(f'urlImg: {list_div_img[i].find("img")["src"]}')
		print(f'duration:{list_div_duration[i].text}')
'''
	#list_div_all = html_parser.find_all('div',class_=True)
	#print(len(list_div_all))
	#print(list_div_all)

	#print(f'list results:{len(list_div_content)}')
	#print('\n')
#list_div = [i['class'] for i in list_div if 's' in i['class']]

	#print(list_div)
#	print(len(list_div))
	#res=[]
	#for i in range(len(list_div_content)):
#		res.append(str(list_div_content[i]))
		
	#	url_video=list_div_content[i].find('a')['href']
	#	code_embed = url_video.split('/')[1].split('-')[1]
#		print(code_embed)
	#	title_video=list_div_content[i].find('img')['alt']

	#	img_url_data_src=list_div_content[i].find('img').get('data-src')
	#	img_url_data_st=list_div_content[i].find('img').get('data-st')
	#	img_url_src=list_div_content[i].find('img').get('src')

	#	duration_video=list_div_info[i].find('span',title='Duration').text
	#	rating_video=list_div_info[i].find('span',title='Rating').text
	#	views_video=list_div_info[i].find('span',title='Views').text

	#	print('mbcontent:',list_div_content[i])
#		print('mbunder:',list_div_info[i],'\n')
	#	video = {'title':title_video,
	#		'url_video':f'{url_base}{url_video}',
	#		'img_url_src':f'{img_url_src}',
	#		'img_url_data_src':img_url_data_src,
	#		'img_url_data_st':img_url_data_st,
	#		'duration':duration_video,
	#		'views_video':views_video,
	#		'rating_video':rating_video,
	#		'code_embed':code_embed
	#		}
	#	print('\n',video)
	#	res.append(video)		
		
		
#	return res[:24]


res = ((get_porn_div('eva notty')))

for v in res:
	print('')
	print(v)


def get_source_video(url_video_eporner):
	pass
