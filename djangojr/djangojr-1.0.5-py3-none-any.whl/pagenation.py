
def pagenation(obj, page, page_size, start=0):
    data = dict()
    page = page if page >= start else start
    size = ((len(obj)/page_size)-1)+start
    data["currentPage"] = page
    data["firstPage"] = start
    data["lastPage"] = int(str(float(size)).split(".")[0])
    data["nextPage"] = True if data["lastPage"] > page else False
    current_page = (page*page_size)-start
    next_page = current_page+page_size
    obj = obj[current_page:next_page]
    return obj, data
