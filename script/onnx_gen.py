import dnnlib
import numpy as np
import torch
import legacy
import functools
import click
import os
from PIL import Image
import cv2
import onnxruntime
import numpy as np

# 创建一个InferenceSession的实例，并将模型的地址传递给该实例
onnx_model = onnxruntime.InferenceSession('results/stylegan2.onnx')
# 输入
dummy_input = np.random.randn(1, 512).astype(np.double)
# 推理
output_name = onnx_model.get_outputs()[0].name
outputs = onnx_model.run([output_name], {onnx_model.get_inputs()[0].name: dummy_input})[0]
output = (outputs.squeeze().transpose((1, 2, 0)) * 127.5 + 128)
image = np.clip(output, 0, 255).astype(np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imwrite("./results/result.png",image)

