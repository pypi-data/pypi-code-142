def Findx(String, b = False) -> int:
    """
    It is find x.
    If String has x return True.
    Unless String x return None 
    """
    st = str(String)
    if b == False:
        if st.split('=')[1].count("x") == 0 and st.split('=')[0].count("x") == 0:
            return None
    elif b == True:
        if st.count("x") == 0:
            return None
    return True

def Findxyz(String, b = False) -> int:
    """
    It is find xyz.
    If String has xyz return True.
    Unless String xyz return None 
    """
    st = str(String)
    if b == False:
        if (st.split('=')[1].count("x") == 0 and st.split('=')[0].count("x") == 0) or (st.split('=')[1].count("y") == 0 and st.split('=')[0].count("y") == 0)\
            or (st.split('=')[1].count("z") == 0 and st.split('=')[0].count("z") == 0) or (st.count(",") != 2):
            return None
    elif b == True:
        if (st.count("x") == 0) and (st.count("y") == 0) and (st.count("z") == 0):
            return None
    return True

def Findxy(String, b = False) -> int:
    """
    It is find xy.
    If String has xy return True.
    Unless String xy return None 
    """
    st = str(String)
    if b == False:
        if (st.split('=')[1].count("x") == 0 and st.split('=')[0].count("x") == 0) or (st.split('=')[1].count("y") == 0 and st.split('=')[0].count("y") == 0) or (st.count(",") != 1):
            return None
    elif b == True:
        if (st.count("x") == 0) and (st.count("y") == 0):
            return None
    return True
