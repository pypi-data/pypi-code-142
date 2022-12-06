from urllib import parse as urlparse
import os
import requests



def replacement_func(url):

    splitted_arr = urlparse.urlsplit(url)
    #eleminate % from url.path
    without_percentage = splitted_arr.path.replace("%", "")
    #eleminate /catalog.xml from url.path
    without_catalog = without_percentage.replace("/catalog.xml", "")
    #eleminate /thredds/ from url.path
    without_thredds = without_catalog.replace("/thredds/", "")
    #create a name without /
    convert_underscore = without_thredds.replace("/", "_")
    #eleminate .xml form url.path
    converted_xml_o = convert_underscore.replace(".xml", "")

    return converted_xml_o

def html2xml(url):
    u = urlparse.urlsplit(url)
    path, extesion = os.path.splitext(u.path)
    if extesion == ".html":
        u = urlparse.urlsplit(url.replace(".html", ".xml"))
    return u.geturl()  
        
def get_xml(url):

    try:
        xml_url = requests.get(url, None, verify=False)
        xml = xml_url.text.encode('utf-8')
    except BaseException:
        pass
    return xml

def references_urls(url, additional):
    splitted_arr = urlparse.urlsplit(url)
    common_url = str(splitted_arr.scheme)+"://"+str(splitted_arr.netloc)
    wihtout_catalog_xml = urlparse.urljoin(common_url, os.path.split(splitted_arr.path)[0])
    if not additional:
        final_url =  url
    elif additional[0] == "h":
        # finding http or https
        final_url = additional
    elif additional[0] == "/":
        # Absolute paths
        final_url = urlparse.urljoin(common_url, additional)
    else:
        # Relative paths.
        final_url = wihtout_catalog_xml + "/" + additional
    
    return final_url