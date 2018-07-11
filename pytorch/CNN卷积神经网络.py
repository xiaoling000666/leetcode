import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision
import matplotlib.pyplot as plt

#Hyper Parameters 超参数
EPOCH = 1            #计算次数
BATCH_SIZE = 50
LR = 0.001
DOWNLOAD_MNIST = True       #用做下载数据

train_data = torchvision.datasets.MNIST(
    root = './mnist',
    train = True,
    transform = torchvision.transforms.ToTensor(),     #改成tensor，压缩到(0,1)
    download = DOWNLOAD_MNIST
)

train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
test_data = torchvision.datasets.MNIST(root='./mnist',train = False)
test_x = torch.unsqueeze(test_data.test_data,dim=1).type(torch.FloatTensor)[:2000]/255  # shape from (2000, 28, 28) to (2000, 1, 28, 28), value in range(0,1
test_y = test_data.test_labels[:2000]

class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(       #(1,28,28)
                in_channels = 1,               #图片只有一个层
                out_channels = 16,             #fliter的个数
                kernel_size = 5,               #fliter的宽和高都是5个像素点
                stride = 1,                    #每隔多少步跳一步
                padding = 2,                   #if stride = 1,padding = (kernel_size-1)/2
            ),                                 # ->(16,28,28)
            nn.ReLU(),                         # ->(16,28,28)
            nn.MaxPool2d(kernel_size=2),       #选择2*2区域中最大的值   # ->(16,14,14)
        )
        self.conv2 = nn.Sequential(            # ->(16,14,14)
            nn.Conv2d(16,32,5,1,2),            # ->(32,14,14)
            nn.ReLU(),                         # ->(32,14,14)
            nn.MaxPool2d(2)                    # ->(32,7,7)
        )
        self.out = nn.Linear(32 * 7 * 7, 10)
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)        #(batch,32,7,7)
        x = x.view(x.size(0), -1)    # (batch,32 * 7 * 7)
        output = self.out(x)
        return output
cnn =CNN()
# print (cnn)
optimizer = torch.optim.Adam(cnn.parameters(),lr=LR)
loss_func = nn.CrossEntropyLoss()     #目标不是one-hot
if __name__=='__main__':
    for epoch in range(EPOCH):
        for step,(x,y) in enumerate(train_loader):
            b_x = Variable(x)
            b_y = Variable(y)
            output = cnn(b_x)
            loss = loss_func(output, b_y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            print(loss.data[0])