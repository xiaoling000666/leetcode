# -*- coding:utf-8 -*-
import torch
import torch.utils.data as Data
torch.manual_seed(1)
BATCH_SIZE = 5

x = torch.linspace(1, 10, 10)
y = torch.linspace(10, 1, 10)



torch_dataset = Data.TensorDataset(x, y)
loader = Data.DataLoader(
    dataset = torch_dataset,  #把dataset放到loader中
    batch_size = BATCH_SIZE,
    shuffle = True,     #要不要随机数据
    num_workers=2,
)

if __name__=='__main__':
    for epoch in range(5):
        for step, (batch_x, batch_y) in enumerate(loader):  # 每一步 loader 释放一小批数据用来学习
            print('Epoch: ', epoch, '| Step: ', step, '| batch x: ',
                  batch_x.numpy(), '| batch y: ', batch_y.numpy())
# 假设这里就是你训练的地方...
# 打出来一些数据
