import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

## Tensor Operation
### create tensor
tensor_new = tensor.shuffle(0).batch(2) # shuffle the data and create batch
iter(tensor_new).next().numpy() # get the data from tensor iterator

data_generator = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2, 
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True, 
    fill_mode='nearest'
)
data_generator.flow_from_directory(
    directory,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)
data_generator.flow_from_dataframe(
    dataframe,
    directory,
    x_col='filename',
    y_col='class',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

### math operation
tf.add(tensor1, tensor2)
tf.subtract(tensor1, tensor2)
tf.matmul(tensor1, tensor2) # matrix multiple
tf.multiply(tensor1, tensor2) # element-wise multiple
tensor = tensor1 + tensor2

### 数据预处理
from skimage import exposure, io
img= exposure.equalize_adapthist(img, clip_limit=clip_limit) #直方图均衡化
img_scaled = img/img.max() #归一化

### 自定义层
class CustomLayer(tf.keras.layers.Layer):
    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(CustomLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        self.kernel = self.add_weight(name='kernel', shape=(input_shape[1], self.output_dim), initializer='uniform', trainable=True)
        super(CustomLayer, self).build(input_shape)

    def call(self, x):
        return tf.matmul(x, self.kernel)

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.output_dim)

### 搭建模型
#### 1. sequential API
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(100,)， kernel_initializer='he_normal'， bias_initializer='zeros'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

#### 2. functional API(可以搭建复杂的拓扑结构)
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.nn import relu, sigmoid, softmax

inputs = Input(shape=(100,))
x = Dense(32, activation='relu')(inputs)
outputs = Dense(1, activation='sigmoid')(x)
model = Model(inputs=inputs, outputs=outputs)
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

#### 3. model subclassing(可以搭建复杂的拓扑结构)
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
base_model.trainable = False
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer = tf.keras.layers.Dense(1)
model = tf.keras.Sequential([
  base_model,
  global_average_layer,
  prediction_layer
])


