import json


def read_file(name):
    name_file = 'json_file/file_tach/comment/' + name + '.json'
    f = open(name_file)
    list_id = json.load(f)
    return list_id


def export_file(name, data):
    name = 'json_file/file_tach/comment/' + name + '.json'
    with open(name, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    print("Export complete")


if __name__ == '__main__':
    total = []
    file1 = read_file("file_1_comment")
    file2 = read_file("file_2_comment")
    file3 = read_file("file_3_comment")
    file4 = read_file("file_4_comment")

    total = file1 + file2 + file3 + file4
    print(len(total))
    export_file("total_comment(13-4-2022)", total)

# 4.667.466 comment
