import os

from src.data_parser.json_parser import parse_json
from src.conversion_engine.rectangle_converter import normalize_coordinates
from src.conversion_engine.bounding_box_extractor import extract_bounding_box
from src.utils.label_mapping import name2id


def decode_json(json_folder_path, txt_outer_path, json_name, convert=True):
    if convert:
        print("坐标进行缩放至0-1")
    else:
        print("坐标不进行缩放")
    txt_name = os.path.join(txt_outer_path, json_name[json_name.rfind("/") + 1:-5] + '.txt')
    with open(txt_name, 'w') as f:
        json_path = os.path.join(json_folder_path, json_name)
        data = parse_json(json_path)
        img_w = data['imageWidth']
        img_h = data['imageHeight']

        for i in data['shapes']:
            label_name = i['label']
            bb = extract_bounding_box(i)

            if convert:
                bbox = normalize_coordinates((img_w, img_h), bb)
            else:
                bbox = bb

            try:
                f.write(str(name2id[label_name]) + " " + " ".join([str(a) for a in bbox]) + '\n')

            except Exception as e:
                raise e


if __name__ == "__main__":
    json_folder_path = '../examples/sample_data/input_data/json_data'  # 请将json文件放在该文件夹下
    txt_outer_path = '../examples/sample_data/output_data/txt_out_data'
    json_names = os.listdir(json_folder_path)
    print("共有：{}个文件待转化".format(len(json_names)))
    flagcount = 0
    for json_name in json_names:
        if not json_name.endswith(".json"):
            continue
        decode_json(json_folder_path, txt_outer_path, json_name, convert=False)  # 这里设置是否要缩放坐标，如果为False则不用缩放
        flagcount += 1
        print("还剩下{}个文件未转化".format(len(json_names) - flagcount))
    print('转化全部完毕')
