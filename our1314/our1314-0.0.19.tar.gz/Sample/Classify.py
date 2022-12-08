import os.path
import time
import torch.optim
import torchvision.datasets
from torch import nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(512 * 612 * 3, 300),
            nn.BatchNorm1d(300),
            nn.ReLU(),
            nn.Linear(300, 100),
            nn.BatchNorm1d(100),
            nn.ReLU(),
            nn.Linear(100, 10)
        )

    def forward(self, x):
        x = self.model(x)
        return x


# region 0、初始化配置参数
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model_path = './out'
is_train = False
writer = SummaryWriter("logs")
# endregion

# region 1、初始化数据
dataset_mnist_train = torchvision.datasets.ImageFolder("C:\\Users\\pc\\Desktop\\有无识别数据集2022.6.20", transform=torchvision.transforms.ToTensor())
dataset_mnist_test = torchvision.datasets.ImageFolder("C:\\Users\\pc\\Desktop\\有无识别数据集2022.6.20", transform=torchvision.transforms.ToTensor())

print(len(dataset_mnist_train))
print(len(dataset_mnist_test))

dataloader_train = DataLoader(dataset_mnist_train, 5, shuffle=True, num_workers=0)
dataloader_test = DataLoader(dataset_mnist_test, 5, shuffle=True, num_workers=0)
# endregion

if is_train:
    current_epoch = 0
    model = Net()
    model.to(device)
    loss_fn = nn.CrossEntropyLoss()
    opt = torch.optim.RMSprop(model.parameters(), lr=0.001)
    model.train()

    # region 选择加载已训练过的模型还是新建模型
    '''
    断点继续参考：
    https://www.zhihu.com/question/482169025/answer/2081124014
    '''
    lists = os.listdir(model_path)
    if not len(lists) == 0:
        lists.sort(key=lambda fn: os.path.getmtime(model_path + "\\" + fn))  # 按时间排序
        last_pt_path = os.path.join(model_path, lists[len(lists) - 1])
        checkpoint = torch.load(last_pt_path)
        current_epoch = checkpoint['epoch']
        model.load_state_dict(checkpoint['net'])
        opt.load_state_dict(checkpoint['optimizer'])
        model.train()
    # endregion

    # ******************************************************************************
    for epoch in range(current_epoch, 150):
        eval_loss = 0
        eval_acc = 0
        for images, labels in dataloader_train:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            loss = loss_fn(outputs, labels)
            opt.zero_grad()
            loss.backward()
            opt.step()
            # print(loss.item())
            eval_loss += loss.item()
            # num_correct = (outputs == labels).sum().item()
            pass
            # 目标label是0-9，预测label是张量，是否需要将目标label归一化
            # 神经网络只考虑单张图像的情况，多张图像由框架自动适应。

        writer.add_scalar('loss', eval_loss, epoch)

        print(f"epoch：{epoch}, 损失：{eval_loss}")
        state_dict = {'net': model.state_dict(),
                      'optimizer': opt.state_dict(),
                      'epoch': epoch}
        if epoch % 5 == 0:
            p = f'{model_path}/{time.strftime("%Y.%m.%d_%H.%M.%S")}-loss={str(round(eval_loss, 2))}.pth'
            torch.save(state_dict, p)
    # state = model.state_dict()
    # 保存整个模型（包括网络参数和网络结构）
    torch.save(model.state_dict(), model_path)

else:
    lists = os.listdir(model_path)
    lists.sort(key=lambda fn: os.path.getmtime(model_path + "\\" + fn))
    last_pt_path = os.path.join(model_path, lists[len(lists) - 1])
    checkpoint = torch.load(last_pt_path)

    model = Net()
    model.load_state_dict(checkpoint['net'])
    model.eval()
    out = torch.tensor([0])

    acc = 1.
    for images, labels in dataloader_test:
        out = model(images)
        _, index = out.max(1)

        print((index == labels).sum())
        num_correct = (index == labels).sum().item()
        # print(num_correct)
        acc = num_correct / images.shape[0]
        print(acc)
        pass

        # outputs = model(images)
        # loss = loss_fn(outputs, labels)
        # _, pred = outputs.max(1)

torch.onnx.export()