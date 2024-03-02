import tensorflow as tf

## 设置计算资源
import os
os.environ["CUDA_VISIBLE_DEVICES"]=""

## 训练模型 
#### 普通训练
from .tensorflow import model
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_val, y_val))
# model.fit(train_generator, epochs=5, steps_per_epoch = (num_samples // batch_size), validation_data=validation_generator, validation_steps=(num_val_samples // batch_size))
y_pred = model.predict(x_test)
model.save('model.h5')

#### 高级训练
import tensorflow.feature_column as fc

feature_columns = [fc.numeric_column("x", shape=[1])]
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)
linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)

