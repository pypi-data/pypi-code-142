import foolbox as fb
import torch
import torchvision
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import torchvision.datasets as td
import os


def dataset_init(dataset):
    data = td.MNIST('mnist', train=True, transform=torchvision.transforms.ToTensor(), download=True)
    if dataset == 'cifar10':
        data = td.CIFAR10('cifar10', train=True, transform=torchvision.transforms.ToTensor(), download=True)
    elif dataset == 'cifar100':
        data = td.CIFAR100('cifar100', train=True, transform=torchvision.transforms.ToTensor(), download=True)
    elif dataset == 'imagenet':
        data = td.ImageNet('imagenet', train=True, transform=torchvision.transforms.ToTensor(), download=True)
    # 产生一个数据的迭代器data_loader
    data_loader = DataLoader(data, batch_size=16)
    return data_loader


def plot(raw, labels, predic):
    plt.figure(figsize=(16, 8))
    id = 0
    for cnt in range(4):
        for j in range(4):
            plt.subplot(4, 4, id + 1)
            plt.imshow(raw[id, 0].reshape(28, 28), cmap="gray")
            plt.title(f"{labels[id]}->{predic[id]}", {"color": "red"})
            plt.axis("off")
            id += 1
    plt.show()


def attack(model_weights, Net, methodName, epsilon, steps=None, distance=None, dataset='mnist'):
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    model, device, fmodel, data_loader = init(model_weights, Net, dataset)
    attack_dataset(model, methodName, fmodel, device, data_loader, epsilon, steps, distance)


def init(model_weights, Net, dataset):
    # 如果保存的是模型参数，则应修改model.py为对应的网络结构，并使用以下方式读取模型：
    model = Net()
    model.load_state_dict(torch.load(model_weights))
    # model = torch.load(model)

    # 求值模式
    model.eval()

    data_loader = dataset_init(dataset)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    fmodel = fb.PyTorchModel(model, bounds=(0, 1))
    return model, device, fmodel, data_loader


def attack_dataset(model, methodName, fmodel, device, data_loader, epsilon, steps, distance):
    global attack
    # 方法1（需要初始化steps的算法）
    if methodName == 'VirtualAdversarialAttack':
        attack = fb.attacks.VirtualAdversarialAttack(steps=steps)
    # 方法2~7，需要初始化distance
    elif methodName == 'BinarySearchContrastReductionAttack':
        attack = fb.attacks.BinarySearchContrastReductionAttack(distance=distance)
    elif methodName == 'DatasetAttack':
        attack = fb.attacks.DatasetAttack(distance=distance)
    elif methodName == 'GaussianBlurAttack':
        attack = fb.attacks.GaussianBlurAttack(distance=distance)
    elif methodName == 'InversionAttack':
        attack = fb.attacks.InversionAttack(distance=distance)
    elif methodName == 'LinearSearchBlendedUniformNoiseAttack':
        attack = fb.attacks.LinearSearchBlendedUniformNoiseAttack(distance=distance)
    elif methodName == 'LinearSearchContrastReductionAttack':
        attack = fb.attacks.LinearSearchContrastReductionAttack(distance=distance)
    elif methodName == 'PointwiseAttack':
        attack = fb.attacks.PointwiseAttack()
    elif methodName == 'BoundaryAttack':
        attack = fb.attacks.BoundaryAttack()
    elif methodName == 'L2CarliniWagnerAttack':
        attack = fb.attacks.L2CarliniWagnerAttack()
    elif methodName == 'DDNAttack':
        attack = fb.attacks.DDNAttack()
    elif methodName == 'EADAttack':
        attack = fb.attacks.EADAttack()
    elif methodName == 'FGM':
        attack = fb.attacks.FGM()
    elif methodName == 'FGSM':
        attack = fb.attacks.FGSM()
    elif methodName == 'NewtonFoolAttack':
        attack = fb.attacks.NewtonFoolAttack()
    elif methodName == 'PGD':
        attack = fb.attacks.PGD()
    elif methodName == 'SaltAndPepperNoiseAttack':
        attack = fb.attacks.SaltAndPepperNoiseAttack()
    elif methodName == 'L1BrendelBethgeAttack':
        attack = fb.attacks.L1BrendelBethgeAttack()
    elif methodName == 'L1FMNAttack':
        attack = fb.attacks.L1FMNAttack()
    elif methodName == 'L2AdditiveGaussianNoiseAttack':
        attack = fb.attacks.L2AdditiveGaussianNoiseAttack()
    elif methodName == 'L2AdditiveUniformNoiseAttack':
        attack = fb.attacks.L2AdditiveUniformNoiseAttack()
    elif methodName == 'L2BasicIterativeAttack':
        attack = fb.attacks.L2BasicIterativeAttack()
    elif methodName == 'L2BrendelBethgeAttack':
        attack = fb.attacks.L2BrendelBethgeAttack()
    elif methodName == 'L2ClippingAwareAdditiveGaussianNoiseAttack':
        attack = fb.attacks.L2ClippingAwareAdditiveGaussianNoiseAttack()
    elif methodName == 'L2ClippingAwareAdditiveUniformNoiseAttack':
        attack = fb.attacks.L2ClippingAwareAdditiveUniformNoiseAttack()
    elif methodName == 'L2ClippingAwareRepeatedAdditiveGaussianNoiseAttack':
        attack = fb.attacks.L2ClippingAwareRepeatedAdditiveGaussianNoiseAttack()
    elif methodName == 'L2ClippingAwareRepeatedAdditiveUniformNoiseAttack':
        attack = fb.attacks.L2ClippingAwareRepeatedAdditiveUniformNoiseAttack()
    elif methodName == 'L2ContrastReductionAttack':
        attack = fb.attacks.L2ContrastReductionAttack()
    elif methodName == 'L2DeepFoolAttack':
        attack = fb.attacks.L2DeepFoolAttack()
    elif methodName == 'L2FastGradientAttack':
        attack = fb.attacks.L2FastGradientAttack()
    elif methodName == 'L2FMNAttack':
        attack = fb.attacks.L2FMNAttack()
    elif methodName == 'L2PGD':
        attack = fb.attacks.L2PGD()
    elif methodName == 'L2ProjectedGradientDescentAttack':
        attack = fb.attacks.L2ProjectedGradientDescentAttack()
    elif methodName == 'L2RepeatedAdditiveGaussianNoiseAttack':
        attack = fb.attacks.L2RepeatedAdditiveGaussianNoiseAttack()
    elif methodName == 'L2RepeatedAdditiveUniformNoiseAttack':
        attack = fb.attacks.L2RepeatedAdditiveUniformNoiseAttack()
    elif methodName == 'LinfAdditiveUniformNoiseAttack':
        attack = fb.attacks.LinfAdditiveUniformNoiseAttack()
    elif methodName == 'LinfBasicIterativeAttack':
        attack = fb.attacks.LinfBasicIterativeAttack()
    elif methodName == 'LinfDeepFoolAttack':
        attack = fb.attacks.LinfDeepFoolAttack()
    elif methodName == 'LinfFastGradientAttack':
        attack = fb.attacks.LinfFastGradientAttack()
    elif methodName == 'LInfFMNAttack':
        attack = fb.attacks.LInfFMNAttack()
    elif methodName == 'LinfinityBrendelBethgeAttack':
        attack = fb.attacks.LinfinityBrendelBethgeAttack()
    elif methodName == 'LinfPGD':
        attack = fb.attacks.LinfPGD()
    elif methodName == 'LinfProjectedGradientDescentAttack':
        attack = fb.attacks.LinfProjectedGradientDescentAttack()
    elif methodName == 'LinfRepeatedAdditiveUniformNoiseAttack':
        attack = fb.attacks.LinfRepeatedAdditiveUniformNoiseAttack()

    for images, labels in data_loader:
        raw, clipped, is_adv = attack(fmodel, images.to(device), labels.to(device), epsilons=epsilon)
        predic = torch.argmax(model(raw.to(device)), dim=1).detach().cpu()
        plot(raw, labels, predic)
