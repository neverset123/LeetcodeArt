## read  data
import matplotlib.pyplot as plt
import torch
from torch import nn
from torchvision import datasets, transforms
train_transform = transforms.Compose([transforms.RandomRotation(30),
                                       transforms.RandomResizedCrop(28), # most of the pretrianed model requires the input image to be 224*224
                                       transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(), #convert hwc to chw and scale to [0,1]
                                       transforms.Normalize([0.5, 0.5, 0.5], # means for each channel
                                                            [0.5, 0.5, 0.5])]) # std for each channel

test_transform = transforms.Compose([transforms.Resize(35), # no random augmentation for test data
                                 transforms.CenterCrop(28),
                                 transforms.ToTensor(),
                                 transforms.Normalize([0.5, 0.5, 0.5], 
                                                            [0.5, 0.5, 0.5])])
data_train = datasets.ImageFolder('path/to/data', transform=train_transform)
loader_train = torch.utils.data.DataLoader(data_train, batch_size=32, shuffle=True)
data_test = datasets.ImageFolder('path/to/data', transform=test_transform)
loader_test = torch.utils.data.DataLoader(data_test, batch_size=32, shuffle=False)
image, label = next(iter(loader_train))
plt.imshow(image[0]) # does color image also work?

## train model
from torch import optim
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# model.fc1.bias.data.fill_(0) # set bias to 0
# model.fc1.weight.data.normal_(std=0.01)   # set weights to small random numbers from normal distribution
loss_func = nn.NLLLoss() # negative log likelihood losss, nn.CrossEntropyLoss()等效于nn.LogSoftmax()叠加nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01) #optimizer = optim.Adam(model.parameters(), lr=0.01) # Adam(momentum) is better than SGD， which provides faster convergence and robust for complex optimization problem by adapting learning rate; while momentum in SGD is used to accelerate optimization but not adapt its learning rate based on gradients like adam does. 
model = model.to(device)
epochs = 5
train_loss_list = []
train_accuracy_list = []
for e in range(epochs):
    train_loss = 0
    train_accuracy = 0
    model.train() # set model to training mode after validation
    for images, labels in loader_train:
        images = images.view(images.shape[0], -1) # flatten images
        images = images.to(device)
        labels = labels.to(device)
        optimizer.zero_grad() # reset optimizer gradient, so that it is not accumulated
        logpb = model(images)
        pb = torch.exp(logpb)
        loss = loss_func(logpb, labels) #注意第一个参数是logits，而不是prob
        loss.backward() # back propagation
        optimizer.step() # update the weight
        train_loss += loss.item()
        top_p, top_class = pb.topk(1, dim=1)
        equals = top_class == labels.view(*top_class.shape)
        train_accuracy += torch.mean(equals.type(torch.FloatTensor)).item() #convert tensor python number
    train_loss_list.append(train_loss/len(loader_train))
    train_accuracy_list.append(train_accuracy/len(loader_train))
    print(f"Training loss: {train_loss/len(loader_train)}")
    print(f'Training accuracy: {train_accuracy/len(loader_train)*100}%')

## validation
test_loss = 0
test_accuracy = 0
with torch.no_grad():
    model.eval() #set model to evaluation mode to avoid dropout
    for iamges, labels in loader_test:
        images = images.view(images.shape[0], -1)
        images = images.to(device)
        labels = labels.to(device)
        logpb = model(iamges)
        pb = torch.exp(logpb)
        test_loss += loss_func(logpb, labels).item()
        top_p, top_class = pb.topk(1, dim=1)
        equals = top_class == labels.view(*top_class.shape)
        test_accuracy += torch.mean(equals.type(torch.FloatTensor)).item()
print(f"Test loss: {test_loss/len(loader_test)}")
print(f'Test accuracy: {test_accuracy/len(loader_test)*100}%')

## save model
checkpoint = {'input_size': 784,
              'output_size': 10,
              'hidden_layers': [layer.out_features for layer in model.hidden_layers],
              'state_dict': model.state_dict()}
torch.save(checkpoint, 'checkpoint.pth')
def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    #rebuild model with same architecture
    model = Model(checkpoint['input_size'],
                             checkpoint['output_size'],
                             checkpoint['hidden_layers'])
    model.load_state_dict(checkpoint['state_dict'])
    return model

