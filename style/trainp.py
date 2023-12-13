import numpy as np # array manipulation
from huggingface_hub import from_pretrained_keras # download the model
import keras # deep learning
from PIL import Image # Image processing

 model = from_pretrained_keras("keras-io/lowlight-enhance-mirnet", compile=False)

 low_light_img = Image.open('../input/happy-whale-and-dolphin/train_images/00354cd9244e28.jpg').convert('RGB')

 low_light_img = low_light_img.resize((256,256),Image.NEAREST)

 low_light_img

 image = keras.preprocessing.image.img_to_array(low_light_img)

 image.shape
 image = image.astype('float32') / 255.0
 image.shape
 image = np.expand_dims(image, axis = 0)
 image.shape
 output = model.predict(image) # model inference to enhance the low light pics

 output_image = output[0] * 255.0
 output_image.shape
 output_image = output_image.clip(0,255)
 output_image.shape
 output_image = output_image.reshape((np.shape(output_image)[0],np.shape(output_image)[1],3))
 output_image

 output_image = np.uint32(output_image)

 Image.fromarray(output_image.astype('uint8'),'RGB')