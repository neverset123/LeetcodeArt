import numpy as np

## 1. gradient descent(eg. sgimoid)
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

h = np.dot(x, w)
nn_output = sigmoid(h)
error = y - nn_output
error_term = error * sigmoid_prime(h)
del_w = learnrate  *error_term*  x

## 2. multilayer perceptrons (2 layers)
N_input = 4
N_hidden = 3
N_output = 2
np.random.seed(42)
X = np.random.randn(4).reshape(1,-1)
target = np.array([1.0, 1.0]).reshape(1,-1)
learnrate = 0.5
n_records = X.shape[0]
weights_input_hidden = np.random.normal(0, scale=0.1, size=(N_input, N_hidden))
weights_hidden_output = np.random.normal(0, scale=0.1, size=(N_hidden, N_output))

del_w_input_hidden = np.zeros(weights_input_hidden.shape)
del_w_hidden_output = np.zeros(weights_hidden_output.shape)
for x, y in zip(X, target):
    hidden_layer_in = np.dot(X, weights_input_hidden)
    hidden_layer_out = sigmoid(hidden_layer_in)
    output_layer_in = np.dot(hidden_layer_out, weights_hidden_output)
    output= sigmoid(output_layer_in)

    error = y - output
    output_error_term = error  *output*  (1 - output)
    hidden_error_term = np.dot(output_error_term, weights_hidden_output.T) * \
                        hidden_layer_out * (1 - hidden_layer_out)
    del_w_hidden_output += learnrate  *output_error_term*  hidden_layer_out.T
    del_w_input_hidden += learnrate  *hidden_error_term* x[:, None]

weights_input_hidden += del_w_input_hidden / n_records
weights_hidden_output += del_w_hidden_output / n_records

## 3. Tensor Operations
### 创建tensor
import torch
torch.manual_seed(7) #设置生成数据的seed
tensor = torch.randn(2,3) # 2*3的tensor
tensor = torch.zeros(1, requires_grad=True) # requires_grad=True表示需要计算梯度
tensor = torch.Tensor(2,3) # 2*3的tensor
tensor = torch.tensor([[1,2,3],[4,5,6]]) # 2*3的tensor向量
tensor = torch.tensor(1) #标量)
tensor = torch.from_numpy(array) # array和tensor共享内存
array = tensor.numpy() #convert tensor to numpy array
tensor.type(torch.FloatTensor) #更改数据类型
tensor.topk(1, dim=1)
tensor.item() # convert tensor to python number

### 改变维度
tensor.shape
tensor.reshape() # 或tensor.view()
tensor.resize_() # underscore 表示in-place method, 也适用于其他函数

### 算术运算
torch.mm(tensor1, tensor2) #matrix multiple
torch.matmul(tensor1, tensor2) #matrix multiple with broadcasting, so always be cautious
torch.sum(tensor, dim=1) # 或tensor.sum(dim=1)
torch.exp(-x)
torch.mean()

### torch函数
import torch.nn.functional as F
F.sigmoid()
F.softmax()
tensor.grad #查看tensor的梯度

## 搭建模型
from torch import nn
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)
    
    def forward(self, x):
        x = F.dropout(F.relu(self.fc1(x)), p=0.2)
        x = F.dropout(F.relu(self.fc2(x)), p=0.2)
        return F.log_softmax(self.fc3(x), dim=1)
model = Model()
#或者如果所有层是线性的，可以用nn.Sequential
from collections import OrderedDict
model = nn.Sequential(OrderedDict(
                      [('fc1',nn.Linear(784, 128)),
                      ('relu1', nn.ReLU()),
                      ('drop1', nn.Dropout(0.2)),
                      ('fc2', nn.Linear(128, 64)),
                      ('relu2', nn.ReLU()),
                      ('drop2', nn.Dropout(0.2)),
                      ('output', nn.Linear(64, 10)),
                      ('softmax', nn.LogSoftmax(dim=1))])
                    )

## transfer learning
from torchvision import models
model = models.densenet121(pretrained=True)
for param in model.parameters():
    param.requires_grad = False # freeze parameters
classifier = nn.Sequential(OrderedDict([
                          ('fc1', nn.Linear(1024, 500)),
                          ('relu', nn.ReLU()),
                          ('fc2', nn.Linear(500, 2)),
                          ('output', nn.LogSoftmax(dim=1))])
                          )
model.classifier = classifier
