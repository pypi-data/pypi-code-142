""" {bot_name} """

# {bot_name} instructions
@BOTS["{bot_name}"].add_instruct(msg_type="text", msg="/hello", compare="lm")
def hello_world():
    BOTS["{bot_name}"].send_message(BOTS["{bot_name}"].message["chat"]["id"],"Hello world")

# {bot_name} url
@app.route('/{bot_name}', methods=['GET', 'POST'])
def run_{bot_name}():
    if request.method == 'POST':
        # Get respond
        res = request.get_json()

        # Add respond
        BOTS["{bot_name}"].add_request(res)

        # Run bot
        BOTS["{bot_name}"].run()

        return Response('ok', status=200)
    else:
        return "<h1>Welcome {bot_name}</h1>"