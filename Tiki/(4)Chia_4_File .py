# Do số lượng sản phẩm lớn -> 51695 sản phẩm
# Chia file ra làm 4 để sử dụng tính năng đa luồng
# Mỗi file sẽ có 12924 ID
import json


def export_file(name, data):
    name = 'json_file/file_tach/' + name + '.json'
    with open(name, 'w') as f:
        json.dump(data, f)
    print("Export complete")


f = open('json_file/list_id_product.json')

list_id = json.load(f)

hafl = round(len(list_id) / 4)

list_1 = []
list_2 = []
list_3 = []
list_4 = []

for idx, item in enumerate(list_id):
    if idx < hafl:
        list_1.append(item)
    elif idx < hafl * 2:
        list_2.append(item)
    elif idx < hafl * 3:
        list_3.append(item)
    else:
        list_4.append(item)

export_file("file_1", list_1)
export_file("file_2", list_2)
export_file("file_3", list_3)
export_file("file_4", list_4)
# len(list_1) => 12924
# len(list_2) => 12924
# len(list_3) => 12924
# len(list_4) => 12923
