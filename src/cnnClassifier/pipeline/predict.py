import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename) -> None:
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join('artifacts', 'training', 'model.keras'))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(244, 244))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0]==1:
            prediction = 'Healthy'
            return [{'Prediction': prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{'Prediction': prediction}]