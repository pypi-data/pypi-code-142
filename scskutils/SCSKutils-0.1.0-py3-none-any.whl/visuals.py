import plotly.express as px

def heatmap(df,save=False,filepath='',filename='',width=1600,height=1600,display=True):

    fig = px.imshow(df, text_auto=True)
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,)
    
    if display:
        fig.show()

    if save:
        fig.write_html(f'{filepath}/{filename}.html')