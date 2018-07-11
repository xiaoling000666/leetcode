# -*-coding:utf-8-*-
import torch
from torch.autograd import Variable
tensor = torch.FloatTensor([[1, 2], [3, 4]])
variable = Variable(tensor, requires_grad=True)   #把tensor放到varbiable
#通过variable搭建计算图纸，误差反向传播通过variable反向传播，requires_grad表示是不是要进行反向传播的计算

t_out = torch.mean(tensor*tensor)  # x^2
v_out = torch.mean(variable*variable)
#tensor 不能进行反向传播

v_out.backward()
#v_out*sum(var*var)
#d(v_out)/d(var)=1/4*2*variable = variable/2
print(variable.grad)

print(variable.data)

print(variable.data.numpy())
#不能直接打印variable.numpy(),需打印variable.data.numpy()







