# Lấy dữ liệu các sản phẩm của từng id danh mục được lấy từ file 1

# Cấu trúc api => trả về một danh sách các thông tin sản phẩm

# https://tiki.vn/api/personalish/v1/blocks/listings?limit=300&category=1789&page=1
# Phân tích: &category=1789&page=1

# Chỉ cần thay đổi id category và số page => danh sách sản phẩm của danh mục đó


import json
import requests as rq

BASE_URL = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=300&category="
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')
}
COUNT = 0
LIST = []


def read_file():
    f = open('file_chua_xu_ly/id_category.json')
    list_category = json.load(f)
    return list_category


def export_file(name, data):
    name = 'json_file/' + name + '.json'
    with open(name, 'w', encoding='utf8') as f:
        json.dump(data, f)
    print("Export complete")


def get_data_id(category_id):
    global BASE_URL
    global HEADERS
    global LIST
    # Get link
    link_category = BASE_URL + category_id;
    # Response
    response = rq.get(link_category, headers=HEADERS)
    # Convert json
    res_json = response.json()
    # Get max page => vì có nhiều page
    # Nên cần lặp n page để lấy dữ liệu
    max_page = res_json['paging']['last_page']
    # Get list product form id category
    listIDProduct = getIDProduct(link_category, max_page)
    LIST += listIDProduct


# Get id product => List id product
def getIDProduct(link, max_page):
    # tạo mảng tạm => đại diện cho data của all page trong sản phẩm
    allPage = []
    link = link + '&page='
    for page in range(1, max_page + 1):
        # lấy từng page
        temp = getDataFromPage(link, page)
        if (len(temp) != 0):
            allPage += temp
            print(COUNT)
        elif len(temp) == 0:
            return allPage
    return allPage


# Get data from page => data 1 page
def getDataFromPage(link, page):
    # https://tiki.vn/api/personalish/v1/blocks/listings?limit=300&category=1789&page=1
    # Temp
    global COUNT
    # Mảng tạm đại diện cho data của 1 page
    array = []
    # Create link page = ?
    link = link + str(page)
    print(link)
    response = rq.get(link, headers=HEADERS)
    # Convert json
    res_json = response.json()
    data = res_json['data']
    if len(data) == 0:
        return array
    # Get item product from json file
    for idx, item in enumerate(data):
        review_count = item['review_count']
        id = item['id']
        name = item['name']
        array_item = {'id': id, 'name': name, 'review_count': review_count}
        COUNT += 1
        # Thêm vào mảng tạm
        array.append(array_item)
    return array;


if __name__ == '__main__':
    category_list = read_file()
    # Lặp qua tất cả các id danh mục
    for id in category_list:
        # Lấy id của từng danh mục
        get_data_id(id)
    # get_data_id("1789")
    export_file("list_info_Product", LIST)
    print("Complete")
    print(COUNT)

# 75290
