from mytui import MyTUI

MyTUI.config(
    text_center=True,
)

'''
MyTUI.config() ->  config some variables
MyTUI.text()   ->  display a text box
MyTUI.menu()   ->  display a select menu
MyTUI.yesno()  ->  display a yes no choice
MyTUI.input()  ->  display an input field
'''

output = MyTUI.textbox(title="Exemple Text", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat")

if output == "back":
    print("Escaped")
    exit()
    
output = MyTUI.yesno(title="Exemple Yes / No", text="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

if output:
    
    options = [
        "1. First",
        "2. Second",
        "3. Third"
    ]
    
    choice = MyTUI.menu(title="Exemple Menu", text="Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt", options=options)
    
    if choice == options[0]:
        if MyTUI.yesno(title="Exemple Yes / No", text="Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem"):
            MyTUI.textbox(title="Exemple Text", text="The end.")
            exit()
        else:
            MyTUI.textbox(title="Exemple Text", text="Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
    
    elif choice == options[1]:

        name = MyTUI.input(title="Exemple Input", text="Enter your name", max_length=40, default_text="", input_size=30, only_alpha=True)
        MyTUI.textbox(title="Exemple Text", text=f"The end.\nYour name is {name}. \n \nYou can now leave using 'q'")

else:
    
    MyTUI.textbox(title="Refused!", text="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo")
    exit()