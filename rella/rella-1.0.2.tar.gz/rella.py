import requests

class Rella:
  def __init__(self, api_key, enabled=True, ingest_url="https://ingestion.rella.so/i/events"):
    self.api_key = api_key
    self.enabled = enabled
    self.ingest_url = ingest_url

  def track(self, event_type, title, msg=None, icon=None, color=None, tags=None):
    if not self.enabled:
      return
      
    body = {
      "type": event_type,
      "title": title,
    }
    
    if msg:
      body["msg"] = msg
    if icon:
      body["icon"] = icon
    if color:
      body["color"] = color
    if tags:
      body["tags"] = tags
    
    try:
      requests.post(self.ingest_url, json=body, headers={
        "content-type": "application/json",
        "authorization": self.api_key,
      })
    except Exception as e:
      print(f"Failed to post event to Rella: {e}")
