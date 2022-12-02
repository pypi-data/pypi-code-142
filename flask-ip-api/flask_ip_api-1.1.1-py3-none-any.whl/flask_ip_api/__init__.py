def IPInfo(app):
  from werkzeug.middleware.proxy_fix import ProxyFix
  from flask import request
  import requests
  app.wsgi_app = ProxyFix(app.wsgi_app)
  @app.before_request
  def fix_ip():
    if request.headers.get('X-Forwarded-For'):
      request.ip = request.headers['X-Forwarded-For']
    elif request.environ.get('HTTP_X_FORWARDED_FOR'):
      request.ip = request.environ['HTTP_X_FORWARDED_FOR']
    else:
      request.ip = request.environ['REMOTE_ADDR']
    data = requests.get("https://ipapi.com/ip_api.php?ip="+request.ip).json()
    del data["connection"]
    data2 = requests.get("https://ipinfo.io/widget/demo/"+request.ip, headers={"referer": "https://ipinfo.io/"}).json()["data"]
    data["asn"] = data2["asn"]
    data["company"] = data2["company"]
    data["abuse"] = data2["abuse"]
    data["domains"] = data2["domains"]
    data["security"]["is_vpn"] = data2["privacy"]["vpn"]
    data["security"]["is_relay"] = data2["privacy"]["relay"]
    data["security"]["hosting"] = data2["privacy"]["hosting"]
    data["security"]["service"] = data2["privacy"]["service"]
    data3 = requests.get("https://ipinfo.io/widget/demo/"+data["asn"]["asn"], headers={"referer": "https://ipinfo.io/"}).json()
    data["asn"]["country"] = data3["country"]
    data["asn"]["allocated"] = data3["allocated"]
    data["asn"]["registry"] = data3["registry"]
    data["asn"]["domain"] = data3["domain"]
    data["asn"]["num_ips"] = data3["num_ips"]
    data["asn"]["ips_v4"] = data3["prefixes"]
    data["asn"]["ips_v6"] = data3["prefixes6"]
    request.ip = data