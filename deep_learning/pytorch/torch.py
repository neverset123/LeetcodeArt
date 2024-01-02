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


## 3. torch
import torch

## 加载图片
from torchvision import datasets, transforms
train_transform = transforms.Compose([transforms.RandomRotation(30),
                                       transforms.RandomResizedCrop(224),
                                       transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(),
                                       transforms.Normalize([0.5, 0.5, 0.5], 
                                                            [0.5, 0.5, 0.5])]) # data augmentation

test_transform = transforms.Compose([transforms.Resize(255),
                                 transforms.CenterCrop(224),
                                 transforms.ToTensor(),
                                 transforms.Normalize([0.5, 0.5, 0.5], 
                                                            [0.5, 0.5, 0.5])])
dataset = datasets.ImageFolder('path/to/data', transform=train_transform)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

## 创建tensor
tensor = torch.from_numpy(array) # array和tensor共享内存
array = tensor.numpy()
array = torch.randn(n_input, n_hidden)
tensor = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
tensor.type(torch.FloatTensor) #更改数据类型
tensor.topk(1, dim=1)
tensor.item() # convert tensor to python number

## 改变维度
tensor.shape
tensor.reshape() # 或tensor.view()
tensor.resize_() # underscore 表示in-place method


# 算术运算
torch.mm(tensor1, tensor2) #matrix multiple
torch.sum(tensor, dim=1) # 或tensor.sum(dim=1)
torch.exp(-x)
torch.mean()

## torch函数
import torch.nn.functional as F
F.sigmoid()
F.softmax()

## 搭建模型
x = torch.zeros(1, requires_grad=True)
x.requires_grad = False
with torch.no_grad():
    pass

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
from collections import OrderedDict
model = nn.Sequential(OrderedDict([
                      ('fc1',nn.Linear(784, 128)),
                      ('relu1', nn.ReLU()),
                      ('drop1', nn.Dropout(0.2)),
                      ('fc2', nn.Linear(128, 64)),
                      ('relu2', nn.ReLU()),
                      ('drop2', nn.Dropout(0.2)),
                      ('output', nn.Linear(64, 10)),
                      ('softmax', nn.LogSoftmax(dim=1))
                    ]))
## 训练模型
# model.fc1.bias.data.fill_(0)
# model.fc1.weight.data.normal_(std=0.01)
ce = nn.NLLLoss()
from torch import optim
optimizer = optim.SGD(model.parameters(), lr=0.01)
optimizer.zero_grad() # reset optimizer gradient, so that it is not accumulated

model.train() # set model to training mode
logpb = model(x)
loss = ce(logpb, labels) #注意第一个参数是logits，而不是prob
loss.backward() # back propagation
optimizer.step() # update the weight

## 模型验证
with torch.no_grad():
    model.eval() #set model to evaluation mode to avoid dropout
    logps = model(img)
ps = torch.exp(logps)

top_p, top_class = ps.topk(1, dim=1)
equals = top_class == labels.view(*top_class.shape)
accuracy = torch.mean(equals.type(torch.FloatTensor))
print(f'Accuracy: {accuracy.item()*100}%')

## 保存模型
checkpoint = {'input_size': 784,
              'output_size': 10,
              'hidden_layers': [each.out_features for each in model.hidden_layers],
              'state_dict': model.state_dict()}
torch.save(checkpoint, 'checkpoint.pth')
def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = fc_model.Network(checkpoint['input_size'],
                             checkpoint['output_size'],
                             checkpoint['hidden_layers'])
    model.load_state_dict(checkpoint['state_dict'])
    
    return model

## transfer learning
from torchvision import datasets, transforms, models
model = models.densenet121(pretrained=True)
for param in model.parameters():
    param.requires_grad = False

from collections import OrderedDict
classifier = nn.Sequential(OrderedDict([
                          ('fc1', nn.Linear(1024, 500)),
                          ('relu', nn.ReLU()),
                          ('fc2', nn.Linear(500, 2)),
                          ('output', nn.LogSoftmax(dim=1))
                          ]))
    
model.classifier = classifier

## GPU and CPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
input = input.to(device)
model = model.to(device)


