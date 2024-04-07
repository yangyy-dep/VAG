#!/bin/bash
model_dir=$(dirname $(readlink -f "$0"))
#��һ�л�ȡ��ǰ�ű����ڵ�Ŀ¼�������丳ֵ������ model_dir��dirname �������ڻ�ȡ����·����Ŀ¼����readlink -f ���ڻ�ȡָ���ļ��ľ���·��
#���ص�ǰ�ű����ڵ�Ŀ¼�ľ���·��

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
#����ű�����Ŀ¼��������Ŀ¼�Ƿ����
pushd $model_dir
if [ ! -d $outdir ]; then
    mkdir -p $outdir
fi

gen_mlir 
gen_fp16bmodel
#����ԭʼ�Ĺ���Ŀ¼
popd