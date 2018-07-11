import torch
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

n_data = torch.ones(100, 2)         # 数据的基本形态
x0 = torch.normal(2*n_data, 1)      # 类型0 x data (tensor), shape=(100, 2)生成的x0数据是两行一列，数据服从均值为2，方差为1的正态分布
y0 = torch.zeros(100)               # 类型0 y data (tensor), shape=(100, 1)生成的y0数据是100个值为0的数据
x1 = torch.normal(-2*n_data, 1)     # 类型1 x data (tensor), shape=(100, 1)生成的x1数据是两行一列，数据服从均值为-2，方差为1的正态分布
y1 = torch.ones(100)                # 类型1 y data (tensor), shape=(100, 1)生成的y1数据是100个值为1的数据
#注意 x, y 数据的数据形式是一定要像下面一样 (torch.cat 是在合并数据)
x = torch.cat((x0, x1), 0).type(torch.FloatTensor)  # FloatTensor = 32-bit floating
y = torch.cat((y0, y1)).type(torch.LongTensor)    # LongTensor = 64-bit integer
print(y)
#torch中默认的形式，x是32-bit浮点型，y是64-bit integer
x, y = Variable(x), Variable(y)
#把x和y放到Variable的篮子里
plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=y.data.numpy(), s=100, lw=0, cmap='RdYlGn')
plt.show()
class Net(torch.nn.Module):            #继承神经网络
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.out = torch.nn.Linear(n_hidden, n_output)
    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.out(x)
        return x

net = Net(2, 10, 2) #有几个类型就输出几个输出
optimizer = torch.optim.SGD(net.parameters(), lr=0.02)
loss_func = torch.nn.CrossEntropyLoss()     #交叉熵损失函数,softmax,输出的分类结果是概率,三分类问题[0.1,0.2,0.7]
for t in range(100):
    out = net(x)    #[-2. -12, -20] F.softmax(out)[0.1,0.2,0.7]
    loss = loss_func(out, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if loss <= 0.1:
        print(loss)
        break
    if t % 5 == 0:
        plt.cla()
        #过了一道 softmax 的激励函数后的最大概率才是预测值
        prediction = torch.max(F.softmax(out, dim=1), 1)[1]
        #torch.max(a, 1),返回每一行中最大值的那个元素，且返回其索引（返回最大元素在这一行的列索引）,torch.max()[1]， 只返回最大值的每个索引
        pred_y = prediction.data.numpy().squeeze()
        target_y = y.data.numpy()
        plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=100, lw=0, cmap='RdYlGn')
        accuracy = sum(pred_y == target_y) / 200.  # 预测中有多少和真实值一样
        plt.text(1.5, -4, 'Accuracy=%.2f' % accuracy, fontdict={'size': 20, 'color': 'red'})
        plt.pause(1)




