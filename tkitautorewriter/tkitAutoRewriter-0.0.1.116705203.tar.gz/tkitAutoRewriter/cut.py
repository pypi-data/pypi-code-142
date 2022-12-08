from .text_tilling import auto_text_tilling,text_tilling
from bs4 import BeautifulSoup
from tkitreadability import tkitReadability
from .img import get_markdown_images,get_markdown_images_format
from sentence_splitter import SentenceSplitter, split_text_into_sentences
"""段落分割，并且对图片进行提取

"""

def auto_cut_markdown(text,is_html=False,tilling=True,return_sents=False):
    """ｉＩ｀！＄
    段落分割，并且对图片进行提取
    1.分段
    2.提取图片
    3.分句
    The auto_cut_markdown function takes a markdown text and returns the images and texts in it.

    Parameters:
        text (str): The markdown string to be processed.

        is_html (bool, optional): Whether the input is html or not. Defaults to False.

        tilling (bool, optional): Whether split into paragraphs or not . Defaults to True.

        return_sents(bool,optional) :Whether return sentences or not .Defaults to False

    Returns:  A generator of dicts containing image information and texts in each paragraph of the input markdown string.

    :param text: Used to Store the text you want to process.
    :param is_html=False: Used to Determine whether the input is html or markdown.
    :param tilling=True: Used to Split the text into paragraphs.
    :param return_sents=False: Used to Return the sentences of each paragraph.
    :return: A list of dictionaries, each dictionary contains the following information:.

    :doc-author: Trelent
    """


    Readability = tkitReadability()
    if tilling:
        out=text_tilling(text)
    else:
        out=[text]
    for it in out:
        # print("================================")
        # print(it)
        item={"images":[],"text":''}
        if is_html:
            html=it
        else:
            html=Readability.markdown2Html(it)
        soup = BeautifulSoup(html,features="lxml")
        for ii,img in enumerate(soup.find_all('img')):

            img_info={
                "src":img.get("src"),
                "title":img.get("title"),
                "alt":img.get("alt"),
                # "width":img['width'],
                # "height":img['height']
                }
            item['images'].append(img_info)

        text=soup.get_text()
        item['text']=text
        if return_sents:
            item['sents']=split_text_into_sentences(text,'en')

        yield item


def auto_cut_paragraph(text,is_html=False):
    """提取图片和段落
    """
    # print("hh")

    # out=text_tilling(text)
    if is_html:
        Readability = tkitReadability()
        text=Readability.html2markdown(text)
        # text=Readability.markdown2Html(text)
    # print("================================================")
    # print(text)

    #转换回车
    text=text.replace("\n","[SEP]")

    items,images_list=get_markdown_images_format(text)
    # print(items,images_list)
    sents=[]
    sents_clear=[]
    images={}
    start=0
    for it,image in zip(items,images_list):

        if image is None:
            it=text.replace("[SEP]","\n",)
            if it!='':
                sents.append(it)
                sents_clear.append(it)
            pass
        else:
            # print(sents)
            paragraph=" ".join(sents)
            end=len(split_text_into_sentences(paragraph,'en'))
            # end=len(sents)
            # print(start,end)
            # start=end
            # image['index']=[]
            # img={"images":image,'index':end}
            # images.append(img)
            images[end]=image
            # sents_clear[end-1]=''

    # print(images)

    return {
        "images":images,
        "sents":split_text_into_sentences(" ".join(sents),'en'),
        "sents_clear":sents_clear
            }

def back2text(content):
    """
    将图片插入到原文，效果不好
    """
    # sents=content['sents']
    # newsents=
    newsents=[]
    # for img in content['images']:
    #     newsents=newsents+sents[:img['index']]
    for i,sent in enumerate(content['sents']):
        # print(i)
        if i in content['images'].keys():
            # print("tttttt")
            for iimg in content['images'][i]:
                img_text=f"\n\n![{iimg[0]}]({iimg[1]})\n\n"
                newsents.append(img_text)
        sent=sent.replace("[SEP]","\n")
        newsents.append(sent )

    # print(newsents)
    return newsents


        # print("================================")
        # print(it)
        # print(image)
            # continue
    # for it in out:
    #     # print("================================")
    #     # print(it)
    #     item={"images":[],"text":''}
    #     if is_html:
    #         html=it
    #     else:
    #         html=Readability.markdown2Html(it)
    #     soup = BeautifulSoup(html,features="lxml")
    #     for ii,img in enumerate(soup.find_all('img')):

    #         img_info={
    #             "src":img.get("src"),
    #             "title":img.get("title"),
    #             "alt":img.get("alt"),
    #             # "width":img['width'],
    #             # "height":img['height']
    #             }
    #         item['images'].append(img_info)

    #     text=soup.get_text()
    #     item['text']=text
    #     yield item

if __name__ == '__main__':

    text="""Why?  Basically the reason is the natural instincts of the two are completely incompatible.   Consider the following situation:  An excited child who was minding his/her own business or was playing with their sweet four legged friend, runs out the front door or into the backyard.  Suddenly, the border collie dogs herding nature kicks in and he wants to re-collect the escaped “sheep”.  He runs full tilt and blocks the child’s path, looking very threatening.  The child’s natural reaction is to become frightened, scream and run.  Unfortunately, this response only furthers the collie’s desire to put the “livestock” back in line and he will become even more ferocious, nipping at the kid’s heels or grabbing on to them to drag them back into the home.  Though the animal will find nothing wrong with his actions, the poor little boy or girl and any onlooker will be traumatized by the ordeal."""

    print("auto_cut_paragraph")
    print(auto_cut_paragraph(text,is_html=False))
