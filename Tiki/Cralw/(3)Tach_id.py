# Do file 2 (list_info_product) chứa nhiều thông tin
# Loại bỏ các sản phẩm không có comment
# Tách riêng ID sản phẩm từ file 2


import json


def export_file(name, data):
    name = 'json_file/' + name + '.json'
    with open(name, 'w') as f:
        json.dump(data, f)
    print("Export complete")


# đọc file info
f = open('json_file/list_info_Product.json')
list_category = json.load(f)

# mảng tạm
list_id = []

# Lặp qua các phần tử của file info
for idx, item in enumerate(list_category):
    # Lấy các id của các phần tử có count != 0
    if item["review_count"] != 0:
        list_id.append(item["id"])

# Xuất file
export_file("list_id_product", list_id)
print(len(list_id))

# 75290 => 51695 sản phẩm có comment
