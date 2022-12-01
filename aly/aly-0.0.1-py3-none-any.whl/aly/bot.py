import requests,json,os


class TeleBot:
    
    def __init__(self,name,token):
        self.name = name
        self.token = token
        self.url = f'https://api.telegram.org/bot{self.token}/'
        self.res = None
        self.message = self.parse_res()
        self.instructions = []
    
    def add_request(self,request):
        self.res = request
        self.message = self.parse_res()

    def parse_res(self):
        if self.res != None:
            if self.res.get("message"):
                user = self.res.get('message').get('from')
                chat = self.res.get('message').get('chat')
                date = self.res.get('message').get('date')
                msg = ""
                msg_type = "text"

                if self.res.get('message').get('text'):
                    msg = self.res.get('message').get('text')
                    msg_type = "text"
                    if self.res.get('message').get('reply_markup'):
                        msg = {"text":self.res.get('message').get('text'),"reply_markup":self.res.get('message').get('reply_markup')}
                        if self.res.get('message').get('reply_markup').get('inline_keyboard'):
                            if self.res.get('message').get('reply_markup').get('inline_keyboard')[0][0].get("url"):
                                msg_type = "inline_url_buttons"
                            else:
                                msg_type = "inline_buttons"
                        else:
                            msg_type = "buttons"
                    
                elif self.res.get('message').get('video'):
                    msg = self.res.get('message').get('video')
                    msg_type = "video"

                elif self.res.get('message').get('voice'):
                    msg = self.res.get('message').get('voice')
                    msg_type = "voice"

                elif self.res.get('message').get('document'):
                    if self.res.get('message').get('animation'):
                        msg = self.res.get('message').get('animation')
                        msg_type = "animation"
                    else:
                        msg = self.res.get('message').get('document')
                        msg_type = "document"

                elif self.res.get('message').get('photo'):
                    msg = self.res.get('message').get('photo')
                    msg_type = "photo"
                
                elif self.res.get('message').get('video_note'):
                    msg = self.res.get('message').get('video_note')
                    msg_type = "video_note"
                
                elif self.res.get('message').get('location'):
                    msg = self.res.get('message').get('location')
                    msg_type = "location"
                
                elif self.res.get('message').get('poll'):
                    msg = self.res.get('message').get('poll')
                    msg_type = "poll"
                
                elif self.res.get('message').get('contact'):
                    msg = self.res.get('message').get('contact')
                    msg_type = "contact"
                
                elif self.res.get('message').get('sticker'):
                    msg = self.res.get('message').get('sticker')
                    msg_type = "sticker"
    
            elif self.res.get('callback_query'):
                user = self.res.get('callback_query').get('from')
                chat = self.res.get('callback_query').get("message").get('chat')
                date = self.res.get('callback_query').get("message").get('date')
                msg = self.res.get('callback_query').get('data')
                msg_type = "text"

            else:
                return None
            
            return {"user":user,"chat":chat,"date":date,"msg":msg,"msg_type":msg_type}
        else:
            return None

    def set_webhook(self,web_url):
        r = requests.get(self.url+f'setWebhook?url={web_url}')
        return r

    def get_user_profile_photos(self,user_id, **more):
        payload = {
            'user_id': user_id,
            **more
        }
        r = requests.post(self.url+"getUserProfilePhotos",json=payload)
        return r

    def forward_message(self,chat_id, from_chat_id, msg_id, disable_notification=False):
        payload = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': msg_id,
            'disable_notification':disable_notification
        }
        r = requests.post(self.url+"forwardMessage",json=payload)
        return r 

    def send_chat_action(self,chat_id, action):
        payload = {
            'chat_id': chat_id,
            'action': action,
        }
        r = requests.post(self.url+"sendChatAction",json=payload)
        return r

    def send_message(self,chat_id, text, **more):
        payload = {
            'chat_id': chat_id,
            'text': text,
            **more
        }
        r = requests.post(self.url+"sendMessage",json=payload)
        return r
    
    def send_audio(self,chat_id,audio_url, **more):
        payload = {
            'chat_id': chat_id,
            "audio": audio_url,
            **more
        }
        r = requests.post(self.url+"sendAudio", json=payload)
        return r
    
    def send_voice(self,chat_id,voice_url, **more):
        payload = {
            'chat_id': chat_id,
            "audio": voice_url,
            **more
        }
        r = requests.post(self.url+"sendVoice", json=payload)
        return r
    
    def send_photo(self,chat_id,photo_url,caption="", **more):
        payload = {
            'chat_id': chat_id,
            'photo': photo_url,
            'caption': caption,
            **more
        }
        r = requests.post(self.url+"sendPhoto", json=payload)
        return r
    
    def send_video(self,chat_id,video_url, **more):
        payload = {
            'chat_id': chat_id,
            'video': video_url,
            **more
        }
        r = requests.post(self.url+"sendVideo", json=payload)
        return r

    def send_doc(self,chat_id,doc_url, **more):
        payload = {
            'chat_id': chat_id,
            'document': doc_url,
            **more
        }
        r = requests.post(self.url+"sendDocument", json=payload)
        return r
    
    def send_sticker(self,chat_id,sticker_url, **more):
        payload = {
            'chat_id': chat_id,
            'sticker': sticker_url,
            **more
        }
        r = requests.post(self.url+"sendSticker", json=payload)
        return r

    def send_loc(self,chat_id,latitude,longitude, **more):
        payload = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            **more
        }
        r = requests.post(self.url+"sendLocation", json=payload)
        return r

    def send_poll(self,chat_id,question,options,correct_val,type="quiz",is_anonymous=False):
        payload = {
        'chat_id': chat_id,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": is_anonymous,
        "type": type,
        "correct_option_id": options.index(correct_val)
        }

        r = requests.post(self.url+"sendPoll", json=payload)
        return r

    def send_button(self,chat_id, text, button_text, callback_data=[], callback_urls=[]):
        if len(callback_data) == 0 and len(callback_urls) == 0:
            buttons = {'keyboard': [[{'text': txt} for txt in button_text]]}
        else:
            if len(callback_urls) == 0:
                if len(callback_data) == len(button_text):
                    buttons = {'inline_keyboard': [[{'text': button_text[i],"callback_data": callback_data[i]} for i in range(len(button_text))]]}
                else:
                    buttons = None
                    print("Number of CallBack data not equal number of buttons")

            elif len(callback_data) == 0:
                if len(callback_urls) == len(button_text):
                    buttons = {'inline_keyboard': [[{'text': button_text[i],"url": callback_urls[i]} for i in range(len(button_text))]]}
                else:
                    buttons = None
                    print("Number of CallBack urls not equal number of buttons")

        if buttons:
            payload = {
                'reply_markup': buttons
            }
            self.send_message(chat_id, text, **payload)
        else:
            self.send_message(chat_id, "Sorry Server Error")
    
    def download_file(self,file_id):
        url = f'{self.url}getFile?file_id={file_id}'
        a = requests.post(url)
        json_resp = json.loads(a.content)
        file_path = json_resp['result']['file_path']
        print(file_path)
    
        url_1 = f'https://api.telegram.org/file/bot{self.token}/{file_path}'
        b = requests.get(url_1)
        file_content = b.content
        
        self.create_folder(file_path.split("/")[0])
        with open(f"bots/{self.name}/{file_path}", "wb") as f:
            f.write(file_content)
    
    def save_data(self,file_name,**data):
        self.create_save_dir()
        try:
            with open(f"bots/{self.name}/{file_name}.json","r") as file:
                try:
                    json_data = json.loads(file.read())
                except json.JSONDecodeError:
                    json_data = []
        except FileNotFoundError:
            json_data = []

        json_data.append(data)           
        json_data = json.dumps(json_data)  

        with open(f"bots/{self.name}/{file_name}.json","w") as file:
            file.write(json_data)

    def save(self,username,chat_id,date,msg,msg_type,high_quality_photos=False):
        if msg_type != "poll" and msg_type != "buttons" and msg_type != "inline_buttons" and msg_type != "inline_url_buttons": 
            if msg_type == "photo":
                if high_quality_photos:
                    photo_index = -1
                else:
                    photo_index = 0
                file_id = msg[photo_index].get("file_id")
                self.download_file(file_id)
            elif msg_type == "location":
                data = {"username":username,"chat_id":chat_id,"date":date,"location":msg}
                self.save_data("locations",**data)
            elif msg_type == "text":
                data = {"username":username,"chat_id":chat_id,"date":date,"text":msg}
                self.save_data("chat",**data)
            elif msg_type == "contact":
                data = {"username":username,"chat_id":chat_id,"date":date} | msg
                self.save_data("contacts",**data)
            else:
                file_id = msg.get("file_id")
                self.download_file(file_id)
    
    def create_save_dir(self):
        try:
            os.mkdir(f'bots')
        except FileExistsError:
            pass
    
        try:
            os.mkdir(f'bots/{self.name}')
        except FileExistsError:
            pass

    def create_folder(self,folder):
        self.create_save_dir()
        try:
            os.mkdir(f'bots/{self.name}/{folder}')
        except FileExistsError:
            pass

    def run(self):
        def run_code(instruct):
            if instruct.get("code"):
                instruct.get("code")()

        if self.message != None:
            for instruct in self.instructions:
                if self.message.get("msg_type") == instruct.get("msg_type"):
                    if not instruct.get("msg"):
                        run_code(instruct)
                        
                    else:
                        if not instruct.get("compare") or instruct.get("compare") == "m":
                            if self.message.get("msg") == instruct.get("msg"):
                                run_code(instruct)
                                
                        elif instruct.get("compare") == "lm":
                            try:
                                if self.message.get("msg").lower() == instruct.get("msg").lower():
                                    run_code(instruct)
                                    
                            except:
                                pass
                        elif instruct.get("compare") == "in":
                            if instruct.get("msg") in self.message.get("msg"):
                                run_code(instruct)
                                
                elif instruct.get("msg_type") == None and instruct.get("msg") == None:
                    run_code(instruct)
                    # You can add break here

    def add_instruct(self,**decorator_kwargs):
        def decorator(func):
            print("run")
            instruct = {"code":func,**decorator_kwargs}
            self.instructions.append(instruct)
            def wrapper():    
                return func()
            return wrapper
        return decorator
        
