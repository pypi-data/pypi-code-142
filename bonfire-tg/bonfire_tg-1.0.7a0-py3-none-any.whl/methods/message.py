class message(object):
  def __init__(self, value):
    self.value = value

  @property
  def id(self):
      try:
       return self.value['message']['message_id']
      except:
        return None
  @property
  def chat_remove_members(self):
      """chat event"""
      try:
       return self.value['message']['left_chat_participant']
      except:
        return None

  @property
  def edit_(self):
      """edit message handler"""
      try:
       return self.value['edited_message']
      except:
        return None


  @property
  def chat_new_members(self):#
      """chat event"""
      try:
       return self.value['message']['new_chat_members']
      except:
        return None
  @property
  def update_id(self):
      try:
       return self.value['update_id']
      except:
        return None

  @property
  def callback_data(self):
      try:
       return self.value['callback_query']['data']
      except:
        return None

  @property
  def callback_from_username(self):
      try:
       return self.value['callback_query']['from']['username']
      except:
        return None

  @property
  def callback_id(self):
      try:
       return self.value['callback_query']['id']
      except:
        return None

  @property
  def callback_chat(self):
      try:
       return self.value['callback_query']['message']['chat']['id']
      except:
        return None

  @property
  def author_id(self):
      try:
       return self.value['message']['from']['id']
      except:
        return None
  @property
  def author_username(self):
      try:
       return self.value['message']['from']['username']
      except:
        return None
  @property
  def author_first_name(self):
      try:
       return self.value['message']['from']['first_name']
      except:
        return None
  @property
  def text(self):
      try:
       return self.value['message']['text']
      except :
        return None

  @property
  def author_is_bot(self):
      try:
       return self.value['message']['from']['is_bot']
      except:
        return None

  @property
  def chat_id(self):
      try:
       return self.value['message']['chat']['id']
      except:
       return None

  @property
  def language(self):
      try:
       return self.value['message']['from']['language_code']
      except:
       return None

  @property
  def reply_message(self):
      try:
       return self.value['message']['reply_to_message']
      except:
        return None

  @property
  def reply_message_id(self):
      try:
       return self.value['message']['reply_to_message']['message_id']
      except:
        return None

  @property
  def reply_message_author_username(self):
      try:
       return self.value['message']['reply_to_message']['from']['username']
      except:
        return None

  @property
  def reply_message_author_is_bot(self):
      try:
       return self.value['message']['reply_to_message']['from']['is_bot']
      except:
        return None

  @property
  def reply_message_first_name(self):
      try:
       return self.value['message']['reply_to_message']['from']['first_name']
      except:
        return None


  @property
  def reply_message_text(self):
      try:
       return self.value['message']['reply_to_message']['text']
      except:
        return None

  @property
  def date(self):
      try:
       return self.value['message']['date']
      except:
        return None


