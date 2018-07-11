import torch
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1) #在torch中数字有维度，unsqueeze将一维数据转化为二维数据
y = x.pow(2)+0.2*torch.rand(x.size())        #y=x^2+噪点的形式
x, y = Variable(x), Variable(y)

# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()

class Net(torch.nn.Module):       #继承torch的Module
    def __init__(self, n_features, n_hidden, n_output):
        super(Net, self).__init__()       #继承__init__功能,定义每层用什么样的形式
        self.hidden = torch.nn.Linear(n_features, n_hidden)
        # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)# 输出层线性输出
    def forward(self, x):      #Module中的forward功能
        #正向传播输入值，神经网络分析出输出值
        x = F.relu(self.hidden(x))     #激励函数
        x = self.predict(x)            #输出值
        return x

net = Net(1,10,1)  #1个输入层，10个隐藏层，1个输出层


optimizer = torch.optim.SGD(net.parameters(), lr=0.5)  #lr代表步长,SGD随机梯度下降法
loss_func = torch.nn.MSELoss()         #预测值和真实值的误差计算公式(均方差)

plt.ion()
plt.show()

for t in range(1000):
    prediction = net(x)             #给net数据训练数据x
    loss = loss_func(prediction, y)      #计算两者之间的误差
    optimizer.zero_grad()           #清空上一步的残余更新参数值
    loss.backward()                 #误差反向传播,计算参数更新值
    optimizer.step()                # 将参数更新值施加到 net 的 parameters 上
    if loss <=0.01:
        print(loss)
        break
    if t % 5 == 0:  #plot表示学习过程
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(),'r-',lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20,'color':  'red'})
        plt.pause(1)



