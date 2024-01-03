# Data-Craft-works
用于一些非常规的数据转换方法的实现。例如：多边形标注框转换为矩形框。json转换为txt文本等

## 目录结构

```shell
DataCraftworks/              # 主目录
|-- data_transform_factory/   # 数据转换工厂主代码
|   |-- src/                 # 源代码目录
|   |   |-- data_parser/     # 多边形 JSON 解析模块
|   |   |   |-- __init__.py  # 初始化文件
|   |   |   |-- polygon_parser.py  # 多边形解析器
|   |
|   |   |-- conversion_engine/    # 转换引擎模块
|   |   |   |-- __init__.py      # 初始化文件
|   |   |   |-- rectangle_converter.py  # 矩形转换器
|   |
|   |   |-- output_module/    # 输出模块
|   |   |   |-- __init__.py  # 初始化文件
|   |   |   |-- txt_output.py  # TXT 文件输出器
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

