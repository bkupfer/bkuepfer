from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from tensorflow.keras.layers import Dropout, Flatten, Dense
from tensorflow.keras.models import Sequential

from tensorflow.keras.preprocessing import image
from tqdm import tqdm

import numpy as np

from .extract_bottleneck_features import extract_Xception
from .dog_names import DOG_NAMES
from PIL import Image
import io


def bytes_to_tensor(img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    img = img.convert('RGB')
    img = img.resize((224, 224), Image.NEAREST)
    x = image.img_to_array(img)
    return np.expand_dims(x, axis=0)


def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224, 3))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)


def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)


class DogClassifier:

    def __init__(self):
        VGG19_model = Sequential()
        VGG19_model.add(Conv2D(filters=36, kernel_size=2, input_shape=(7, 7, 2048)))
        VGG19_model.add(MaxPooling2D(pool_size=2, strides=1, padding="same"))
        VGG19_model.add(GlobalAveragePooling2D())
        VGG19_model.add(Dense(266, activation="relu"))
        VGG19_model.add(Dense(133, activation="softmax"))
        # VGG19_model.summary()

        VGG19_model.compile(
            loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
        )

        VGG19_model.load_weights('dog_classifier/saved_models/weights.best.my_Xception_checkpoint.hdf5')
        self.VGG19_model = VGG19_model

    def Xception_predict_breed(self, img_file):
        # extract bottleneck features
        bottleneck_feature = extract_Xception(bytes_to_tensor(img_file))
        # obtain predicted vector
        predicted_vector = self.VGG19_model.predict(bottleneck_feature)
        # return dog breed that is predicted by the model
        return DOG_NAMES[np.argmax(predicted_vector)]

