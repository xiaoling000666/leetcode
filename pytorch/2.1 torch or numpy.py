# -*-coding:utf-8-*-
import torch
import numpy as np
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
print(np_data)
print(torch_data)
#数据转换
# a = np.ones(5)
# b = torch.from_numpy(a)      #将numpy数据转化为torch数据
# tensor2array=torch_data.numpy()                 #将torch数据转化为numpy数据
# print(tensor2array)
# print(np_data, torch_data, torch_data.numpy)
# #abs
#data = [-1,-2,1,2]
#tensor = torch.FloatTensor(data)              #将数据转化为tensor浮点型
# print(np.abs(data))                          #[1,2,1,2]
# print(torch.abs(tensor))                      #[1,2,1,2]
# print(np.sin(data))
# print(torch.sin(tensor))
# print(np.mean(data))
# print(torch.mean(tensor))
#
# data = [[1,2],[3,4]]
# tensor = torch.FloatTensor(data)
# data= np.array(data)
# print(np.matmul(data,data))
# print(torch.mm(tensor,tensor))