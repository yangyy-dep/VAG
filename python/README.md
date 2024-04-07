# Python例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [SoC平台](#11-soc平台)
* [2. 推理测试](#2-推理测试)
    * [2.1 参数说明](#21-参数说明)
    * [2.2 测试](#21-测试)

python目录下提供了Python例程，具体情况如下：

| 序号   | Python例程      | 说明                   |
| ---- | ----------------  | -----------------------|
| 1    | gen_img_opencv.py | SAIL推理、OpenCV后处理 |


## 1. 环境准备
###  SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。您还需要交叉编译安装sophon-sail，具体可参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)。

## 2. 推理测试
python例程不需要编译，可以直接运行。

## 2.1 参数说明
gen_img_opencv.py参数说明如下：

```bash
usage:gen_img_opencv.py [--model_path BMODEL] [--dev_id DEV_ID]
--model_path: 用于推理的bmodel路径，默认使用stage 0的网络进行推理；
--dev_id: 用于推理的tpu设备id。
```

### 2.2 测试
测试如下：
```bash
# 测试
python3 gen_img_opencv.py  --model_path models/generator_1684x_bf16.bmodel --dev_id 0
```
测试结束后，会将预测结果保存在`results/result.png`下，同时会打印推理时间等信息。