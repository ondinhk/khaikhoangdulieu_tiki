# Cấu trúc API tìm được:
# https://tiki.vn/api/v2/reviews?include=comments&limit=300&product_id=111304924&page=1
# API trả về một danh sách thông tin các bình luận của sản phẩm

# Phân tích:
# product_id=111304924&page=1
# Chỉ cần thay đổi product_id=? và page=?

# Sử dụng 4 file chứa ID sản phẩm vừa tách ở bước 4
# Cho 4 luồng để lấy dữ liệu từ các link API


import json
import time

import requests as rq
import threading

BASE_URL = "https://tiki.vn/api/v2/reviews?include=comments&limit=300&product_id="
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')
}


def read_file(name):
    name_file = 'json_file/file_tach/' + name + '.json'
    f = open(name_file)
    list_id = json.load(f)
    return list_id


def export_file(name, data):
    name = 'json_file/file_tach/comment/' + name + '.json'
    with open(name, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    print("Export complete")


# Trả về một danh sách các comment của một ID sản phẩm
def get_data_id(id):
    global BASE_URL
    global HEADERS
    LIST = []
    # Get link
    try:
        link_product = BASE_URL + str(id);
        # Response
        response = rq.get(link_product, headers=HEADERS)
    except:
        return
    # Convert json
    res_json = response.json()
    # Get max page
    max_page = res_json['paging']['last_page']
    # Get list product form id category
    listIDProduct = getCommentIDProduct(link_product, max_page)
    LIST += listIDProduct
    return LIST


# Do một sản phẩm có nhiều page
# Func trả về toàn bộ data của sản phẩm
def getCommentIDProduct(link, max_page):
    allPage = []
    # &page=0
    time.sleep(1)
    link = link + '&page='
    for page in range(1, max_page + 1):
        try:
            temp = getDataFromPage(link, page)
        except:
            print("Error")
            continue
        if (len(temp) != 0):
            allPage += temp
        elif len(temp) == 0:
            return allPage
    return allPage


# Trả về dữ liệu của một page
def getDataFromPage(link, page):
    # https://tiki.vn/api/v2/reviews?include=comments&limit=300&product_id=111304924&page=1
    # Temp
    array = []
    # Create link
    link = link + str(page)
    try:
        response = rq.get(link, headers=HEADERS)
        # Convert json
        res_json = response.json()
    except:
        return
    data = res_json['data']
    if len(data) == 0:
        return array
    # Get item product from json file
    for idx, item in enumerate(data):
        content = item['content']
        name = item['created_by']['name']
        rate = item['rating']
        array_item = {'name': name, 'content': content, 'rate': rate}
        array.append(array_item)
    return array;


# Trả về file json
def run_crawl(data_input, name):
    TOTAL = []
    for idx, id in enumerate(data_input):
        print(name, idx, " / 12923")
        try:
            TOTAL += get_data_id(id)
        except:
            print("Error", id)
            continue
        # break
    print(len(TOTAL))
    export_file(name, TOTAL)


# Class cấu hình đa luồng
class myTheard(threading.Thread):
    def __init__(self, id, name, data):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.data = data

    # Định nghĩa hàm run, mỗi khi thread start sẽ gọi hàm này
    def run(self):
        global run_crawl
        run_crawl(self.data, self.name)


if __name__ == '__main__':
    # Get file
    file_1 = read_file("file_1")
    file_2 = read_file("file_2")
    file_3 = read_file("file_3")
    file_4 = read_file("file_4")

    # Create thread
    thread_1 = myTheard(1, "file_1_comment", file_1)
    thread_2 = myTheard(2, "file_2_comment", file_2)
    thread_3 = myTheard(3, "file_3_comment", file_3)
    thread_4 = myTheard(4, "file_4_comment", file_4)

    # Run thread_4
    try:
        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()
    except:
        print("Ko the start")

# số lượng Id sản phẩm 51.695
# file 1 -> 1.070.486
# file 2 -> 666.943
# file 3 -> 1.127.627
# file 4 -> 1.802.410
