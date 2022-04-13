# Mỗi url của danh mục, phía cuối có các mã số
# Các mã số đó đại diện cho id danh mục
# => Mục tiêu tách các id đó ra
# vd: https://tiki.vn/do-choi-me-be/c2549

import json


def read_file():
    array_id = []
    f = open('file_chua_xu_ly/big_cate.json')
    list_category = json.load(f)
    for item in list_category:
        try:
            idx = item[::-1].index('/')
        except:
            continue
        final = item[::-1][0:idx]
        final = final[::-1].replace('c', '');
        if (final == "tikingon"):
            continue
        array_id.append(final)
    return array_id


def export_id_cate(data):
    with open('file_chua_xu_ly/id_category.json', 'w') as f:
        json.dump(data, f)
    print("export complete")


if __name__ == '__main__':
    id_category = read_file()
    print(len(id_category))
    # export_id_cate(id_category)

# Lấy được 24 mã loại hàng chính
# Bỏ sung thủ công 17 mã loại hàng thực phẩm từ trang tiki ngon
# 41 loại hàng
