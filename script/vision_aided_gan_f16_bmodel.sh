#!/bin/bash
model_dir=$(dirname $(readlink -f "$0"))
#这一行获取当前脚本所在的目录，并将其赋值给变量 model_dir。dirname 函数用于获取给定路径的目录名，readlink -f 用于获取指定文件的绝对路径
#返回当前脚本所在的目录的绝对路径

outdir=../models/BM1684X

function gen_mlir()
{
    model_transform.py \
        --model_name generator \
        --model_def generator.onnx \
        --input_shapes [[1,512]] \
        --mlir generator_1684x.mlir
}

function gen_fp16bmodel()
{
    model_deploy.py \
        --mlir generator_1684x.mlir \
        --quantize BF16 \
        --chip  bm1684x \
        --model generator_1684x_bf16.bmodel

    mv generator_1684x_bf16.bmodel $outdir/
}
#进入脚本所在目录，检查输出目录是否存在
pushd $model_dir
if [ ! -d $outdir ]; then
    mkdir -p $outdir
fi

gen_mlir 
gen_fp16bmodel
#返回原始的工作目录
popd