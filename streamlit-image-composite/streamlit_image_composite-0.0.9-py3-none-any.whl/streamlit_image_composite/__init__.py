import base64
import os
from io import BytesIO
from typing import Tuple

import streamlit.components.v1 as components
from PIL import Image
from PIL.Image import Image as PILImage

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "image_composite",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("image_composite", path=build_dir)


def pil_to_base64(pil_image):
    buffer = BytesIO()
    pil_image.save(buffer, format="PNG")
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode('ascii')


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def image_composite(fg: PILImage, bg: PILImage, fg_size: Tuple[int, int], bg_size: Tuple[int, int], key=None):
    """
    Create a new instance of "image_composite"
    Args:
        fg: A pil image of foreground
        bg: A pil image of background
        fg_size: (width, height) of fg image
        bg_size: (width, height) of fg image
        key: We use the special "key" argument to assign a fixed identity to this component instance

    Returns:
        A dict of {x, y, rotate, scaleX, scaleY} of the transformations done to the foreground image
    """

    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    fg = pil_to_base64(fg)
    bg = pil_to_base64(bg)
    fg_width, fg_height = fg_size
    bg_width, bg_height = bg_size
    component_value = _component_func(fg=fg, bg=bg, fg_height=fg_height, fg_width=fg_width, bg_height=bg_height,
                                      bg_width=bg_width, key=key, default={})

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/__init__.py`
if not _RELEASE:
    import streamlit as st

    # We use the special "key" argument to assign a fixed identity to this
    # component instance. By default, when a component's arguments change,
    # it is considered a new instance and will be re-mounted on the frontend
    # and lose its current state. In this case, we want to vary the component's
    # "name" argument without having it get recreated.
    fg_height = fg_width = 400
    fg_size = (fg_width, fg_height)
    bg_height = bg_width = 512
    bg_size = (bg_width, bg_height)
    fg = st.file_uploader("Foreground image:", type=["png", "jpg", "jpeg"])
    bg = st.file_uploader("Background image:", type=["png", "jpg", "jpeg"])

    if fg:
        fg = Image.open(fg)
    else:
        fg = Image.open(os.path.join(os.path.dirname(__file__), 'frontend/public/assets/elon_musk.png')).resize(
            fg_size, Image.BICUBIC)
    if bg:
        bg = Image.open(bg)
    else:
        bg = Image.open(os.path.join(os.path.dirname(__file__), 'frontend/public/assets/padang_padang.jpeg')).resize(
            bg_size, Image.BICUBIC)

    image_stats = image_composite(fg=fg, bg=bg, fg_size=fg_size, bg_size=bg_size, key="foo")
    st.write('State', image_stats)
