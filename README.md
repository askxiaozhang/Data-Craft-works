# Data-Craft-works
用于一些非常规的数据转换方法的实现。例如：多边形标注框转换为矩形框。json转换为txt文本等

## 目录结构

```shell
DataCraftworks/              # 主目录
|-- data_transform_factory/   # 数据转换工厂主代码
|   |-- src/                 # 源代码目录
|   |   |-- data_parser/     # 多边形 JSON 解析模块
|   |   |   |-- __init__.py  # 初始化文件
|   |   |   |-- json_parser.py  # 解析 JSON 数据的模块
|   |
|   |   |-- conversion_engine/
|   |   |   |-- __init__.py
|   |   |   |-- rectangle_converter.py  # 矩形转换器模块
|   |   |   |-- bounding_box_extractor.py  # 新增的模块，用于提取边界框
|   |
|   |   |-- output_module/    # 输出模块
|   |   |   |-- __init__.py  # 初始化文件
|   |   |   |-- txt_output.py  # TXT 文件输出器
|   |
|   |   |-- utils/  # 通用工具模块
|   |   |   |-- __init__.py
|   |   |   |-- label_mapping.py  # 标签映射的工具函数
|   |   |   |-- bounding_box_operations.py  # 新增的模块，用于边界框操作
|   |
|   |-- tests/                # 测试模块
|   |   |-- test_data_parser.py    # 多边形解析器测试
|   |   |-- test_rectangle_converter.py  # 矩形转换器测试
|   |   |-- test_txt_output.py  # TXT 文件输出器测试
|   |
|   |-- __init__.py           # 初始化文件
|   |-- main.py               # 主程序入口
|
|-- docs/                    # 文档目录
|   |-- user_guide.md        # 用户指南
|   |-- developer_guide.md   # 开发者指南
|
|-- examples/                # 示例目录
|   |-- sample_data/         # 示例数据目录
|   |   |-- input_data/      # 输入数据目录
|   |   |   |-- example_polygon.json  # 多边形 JSON 示例数据
|   |   |
|   |   |-- output_data/     # 期望输出数据目录
|   |   |   |-- example_rectangle.txt  # 期望的矩形框 TXT 示例数据
|
|-- requirements.txt         # 依赖库文件
|-- LICENSE                  # 许可证文件
|-- README.md                # 主文档
```

# 使用方法

运行 Data-Craft-works/data_transform_factory/目录下的main.py函数

其中`json_folder_path = 'examples/sample_data/input_data/json_data'`把待转换的json文件夹路径中的数据换成自己的

同理设置生成的txt结果路径`txt_outer_path = '../examples/sample_data/output_data/txt_out_data'`

`decode_json(json_folder_path, txt_outer_path, json_name, convert=False)` **这里设置是否要缩放坐标，如果为False则不用缩放**





