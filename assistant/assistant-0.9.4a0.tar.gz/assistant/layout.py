from prompt_toolkit.widgets import MenuContainer
from prompt_toolkit.layout.layout import Layout

def get_layout(body, menu_items_list, float_item_list, bindings, buffer_window):
	return Layout(container=MenuContainer(body=body, menu_items=menu_items_list, floats=float_item_list, key_bindings=bindings), focused_element=buffer_window)
