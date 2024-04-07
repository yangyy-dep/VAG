# Vision aided gan

## 目录
* [1. 简介](#1-简介)
* [2. 特性](#2-特性)
* [3. 准备模型](#3-准备模型)
  * [3.1 自己下载并且编译模型](#31-自己下载并且编译模型)
  * [3.2 使用准备好的模型文件](#32-使用准备好的模型文件)
* [4. 例程测试](#4-例程测试)
* [5. 运行性能测试](#5-运行性能测试)

## 1. 简介
Vision aided gan:[Vision aided gan](https://github.com/nupurkmr9/vision-aided-gan)，引入了预训练的模型辅助GAN训练取得了新的SOTA，特别是在有限的数据中，显着提高了生成的图像的质量。

目前提供了基于stylegan2模型生成图像。

## 2. 特性

- 支持BM1684X(SoC)
- 支持FP32(BM1684X)、BF16(BM1684X)
- 基于sophon-sail的python推理，生成图片

## 3. 准备模型

Vision aided gan可在BM1684X上运行。本demo提供了基于stylegan2模型生成图像。

### 3.1 自己下载并且编译模型
在script路径下，运行convert_onnx.py即可将vision aided gan基于stylegan2模型onnx的格式保存在目录results下:

```bash
cd script
python3 convert_onnx.py --source=pkl/network-snapshot-005000.pkl --dest=results/
```

模型编译前需要安装TPU-MLIR，具体可参考[TPU-MLIR环境搭建](../../docs/Environment_Install_Guide.md#1-tpu-mlir环境搭建)。安装好后需在TPU-MLIR环境中进入例程目录。使用TPU-MLIR将onnx模型编译为BModel，具体方法可参考《TPU-MLIR快速入门手册》的“3. 编译ONNX模型”(请从[算能官网](https://developer.sophgo.com/site/index/material/31/all.html)相应版本的SDK中获取)。

最后参考TPU-MLIR工具的使用方式激活对应的环境，并在script路径下执行bmodel导出脚本文件（vision_aided_gan_f16_bmodel.sh），会将当前路径下的onnx文件转换为bmodel。


### 3.2 使用准备好的模型文件

models文件结构如下：

```
models
├── BM1684X
│	├── generator_1684x_bf16.bmodel         # 使用TPU-MLIR编译，用于BM1684X的bf16 bmodel
│   └── generator_1684x_f32.bmodel        # 使用TPU-MLIR编译，用于BM1684X的f32 bmodel      
├── onnx
│   └── stylegan2.onnx             # 导出的onnx模型
└── pkl
    └── network-snapshot-005000.pkl                              # 字典文件
```

## 4. 例程测试
- [Python例程](python/README.md)

## 5. 运行性能测试

图像生成性能如下:

|   测试平台    |     测试程序        |        测试模型         | inference_time | postprocess_time |
| -----------   | ------------------  | ---------------------   | -------------  | ---------------- |
| BM1684X SoC   | gen_img_opencv.py   | generator_1684x_bf16.bmodel |    60.54     |     4.98       |
| BM1684X SoC   | gen_img_opencv.py   | generator_1684x_f32.bmodel |    38.58     |     4.97       |
