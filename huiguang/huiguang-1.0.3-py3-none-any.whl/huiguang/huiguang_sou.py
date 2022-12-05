sou_list = ['贾富昌','杨晓刚','李非凡','金万昱','朱彬涛']

def get_sou():
    print('搜索到>>>>>')
    for name in sou_list:
        print('搜到到的结果如下',{name})

    print('搜索完毕>>>>>>>')
    return sou_list

if __name__ == '__main__':
    get_sou()