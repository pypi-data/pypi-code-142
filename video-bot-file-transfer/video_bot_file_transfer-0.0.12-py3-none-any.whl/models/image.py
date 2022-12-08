class MyImage:
    def __init__(self, 
     media_id = None,
     keyword_id = None,
     sentence_id = None,
     section_id = None,
                url = None,
                original_url = None,
                path = None,
                path_converted = None, 
                thumb = None,
                time = 0,
                status =  None,
                provider = None,
                provider_link = None,
                user = None,
                user_attribution = None,
                attribution = None) -> None:
        
        self.url = url
        self.original_url = original_url
        self.path = path       
        self.path_converted =  path_converted
        self.thumb = thumb
        self.time = time
        self.provider = provider
        self.provider_link = provider_link
        self.user = user
        self.user_attribution = user_attribution
        self.status = status
        self.media_id = media_id
      
        self.keyword_id = keyword_id
        self.sentence_id = sentence_id
        self.section_id = section_id

        self.attribution = attribution
        