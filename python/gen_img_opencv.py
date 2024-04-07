# -*- coding: utf-8 -*-
import time
import os
import json
import numpy as np
import argparse
import sophon.sail as sail
import logging
import glob
import cv2
from sd_engine import EngineOV
logging.basicConfig(level=logging.INFO)




class Vision_gan():
    def __init__(
        self,
        model_path,
        dev_id = 0,
    ):
        super().__init__()
        self.gan = EngineOV(model_path, device_id=dev_id)
        self.inference_time = 0.0
        self.postprocess_time = 0.0
    def postprocess(self, outputs):
        
        output = (outputs.squeeze().transpose((1, 2, 0)) * 127.5 + 128)
        image = np.clip(output, 0, 255).astype(np.uint8)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
    def __call__(
            self,
            latents=None,

    ):
        latents = np.random.randn(1, 512).astype(np.double)
        start_time = time.time()
        img = self.gan({'latent': latents,
                               })[0]

        self.inference_time += time.time() - start_time
        start_time = time.time()
        output_img = self.postprocess(img)
        self.postprocess_time += time.time() - start_time
        # calculate speed

        logging.info("------------------ Inference Time Info ----------------------")
        logging.info("inference_time(ms): {:.2f}".format(self.inference_time * 1000))
        logging.info("postprocess_time(ms): {:.2f}".format(self.postprocess_time * 1000))
        return output_img

def run(engine):

    image = engine(

        )
    return image

def load_pipeline(args):
    pipeline = Vision_gan(
        model_path = args.model_path,
        dev_id = args.dev_id,
    )
    return pipeline
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # model_path
    parser.add_argument("--model_path", type=str, default="../models/BM1684X", help="bmodels path")
    # dev_id
    parser.add_argument("--dev_id", type=int, default=0, help="device id")
    try:
        args = parser.parse_args()
    except SystemExit as e:
        os._exit(e.code)
        
    engine = load_pipeline(args)
    image = run(engine)
    cv2.imwrite("./results/result.png",image)