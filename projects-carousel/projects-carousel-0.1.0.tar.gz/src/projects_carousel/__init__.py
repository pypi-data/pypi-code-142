from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components
import webbrowser

st.set_page_config(page_title="Abraão Portfolio",
                    layout="centered",
                    initial_sidebar_state="auto")

# Tell streamlit that there is a component called projects_carousel,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"projects_carousel", path=str(frontend_dir)
)

# Create the python function that will be called
def projects_carousel(
    label: str,
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        label=label,
        key=key
    )

    return component_value

    

def main():
    values_to_carousel = [["images\profile2.jpg", "Andressa Serafim"], 
                            ["images\profile3.jpg", "Annara Soares"], 
                            ["images\profile4.jpg", "Felipe Brum"], 
                            ["images\profile5.jpg", "Remulo Costa"], 
                            ["images\profile6.jpg", "Tarciso Velho"], 
                            ["images\profile1.jpg", "Andrea Arruda"]]

    value = projects_carousel(values_to_carousel)
    st.write(value)

    if value == "Felipe Brum":
        webbrowser.open("https://www.linkedin.com/in/brumfl/", new = 0)
    elif value == "Annara Soares":
        webbrowser.open("https://www.linkedin.com/in/annara-soares-830a21145/", new = 0)
    elif value == "Andrea Arruda":
        webbrowser.open("https://www.linkedin.com/in/andréa-arruda-0705a923/", new = 0)
    elif value == "Tarciso Velho":
        webbrowser.open("https://sigaa.ufrn.br/sigaa/public/docente/portal.jsf?siape=2183828", new = 0) 
    elif value == "Andressa Serafim":
        webbrowser.open("https://www.evz.ufg.br/n/84231-olimpiada-de-empreendedorismo-social", new = 0)  
    elif value == "Remulo Costa":
        webbrowser.open("https://www.linkedin.com/in/rêmullo-costa-98871a55/", new = 0)  
    else:
        None



if __name__ == "__main__":
    main()
