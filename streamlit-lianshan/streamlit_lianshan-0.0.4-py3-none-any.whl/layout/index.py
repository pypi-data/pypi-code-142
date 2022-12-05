import streamlit as st
from istreamlit.index_monitor_page import get_permission_status
import streamlit.components.v1 as components


def index():
    # 匹配token权限,允许继续展示数据
    # get_token = st.experimental_get_query_params()
    # get_permission_status(token=get_token)
    components.html("""
               <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
            """, 0, 0)
    st.markdown(
        '<style>'
        '.block-container{max-width: 95%;padding:1rem 4rem 2rem 1rem;} .css-18ni7ap{background:none;}'
        '.stTabs > div > div > button,.stTabs > div > div > button:hover{color:#AF8871 !important;} '
        '.stTabs > div > div > div{background-color:#AF8871 !important;}'
        '</style>',
        unsafe_allow_html=True)


def footer():
    # 修改底部内容
    footer_autograph()


def footer_autograph(content='Li Auto Data Science'):
    components.html(f"""
           <script>                 
                let content = '{content}'
                """ + """
                let footer = window.parent.document.querySelectorAll("footer")
                if(footer.length > 0){
                    footer[0].innerHTML = content + '<a href="https://lianshan.chehejia.com/iframedocument.html?index=10&sidebar_id=1" class ="css-1vbd788 egzxvld1" > Streamlit </a>'
                }
           </script> 
    """, 0, 0)


def metrics_link(link_list=None, tab_list=None):
    if link_list is None:
        link_list = {}
    if tab_list is None:
        tab_list = {}
    components.html('''
       <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
    ''', 0, 0)
    if len(link_list) > 0:
        # link_list = ['123', '12344']
        components.html(f'''
                    <script> 
                     let list = {link_list}
                     let tabList = {tab_list}
                    ''' + '''
                        let metricsList = window.parent.document.querySelectorAll(".css-1xarl3l.e16fv1kl1")
                        console.log('metricsList', metricsList)
                        setTimeout(() => {
                             let up = window.parent.document.querySelectorAll('*[data-testid=stSidebar] > div > div > div > div > div > div > iframe')                        
                            let sidebar = up[0].contentDocument
                            let nav_item = sidebar.querySelectorAll(".nav-link")
                            console.log('nav_item',nav_item)

                            for(let i =0; i < metricsList.length; i++){
                                metricsList[i].onclick = function(){   
                                        console.log('list',i,list[i]) 
                                        localStorage.setItem("enterIndex", i )
                                        nav_item[list[i]].click();           
                                    }
                                }

                            setTimeout(() => {
                                console.log('nav_item',nav_item[2].className)
                                let tabListDom =  window.parent.document.querySelectorAll('*[aria-orientation="horizontal"] > button ')
                                let enterIndex = localStorage.getItem("enterIndex")
                                console.log('enterIndex',enterIndex)
                                if(nav_item.length > 0){
                                    tabListDom[tabList[enterIndex]].click()
                                    localStorage.removeItem('enterIndex')
                                }                                
                            },2000)

                        },50)

                    </script>
            ''', 0, 0)
