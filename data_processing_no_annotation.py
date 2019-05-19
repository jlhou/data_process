import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets


def load_data(args):
    if args.dataset_mode == "CIFAR10":
            transform_train = transforms.Compose([
                transforms.Resize(224),
                transforms.RandomCrop(224, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),

                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])

            transform_test = transforms.Compose([
                transforms.Resize(224),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])

            train_data = datasets.CIFAR10(root='C:\\Users\\asus\Desktop\MobileNetV3-Pytorch-master', train=True, download=False, transform=transform_train)
            test_data = datasets.CIFAR10(root='C:\\Users\\asus\Desktop\MobileNetV3-Pytorch-master', train=False, download=False, transform=transform_test)

            train_loader = torch.utils.data.DataLoader(
                train_data,
                batch_size=args.batch_size,
                shuffle=True,
                num_workers=args.workers
            )

            test_loader = torch.utils.data.DataLoader(
                test_data,
                batch_size=args.batch_size,
                shuffle=False,
                num_workers=args.workers
            )


###！！！！此数据处理的方法只针对torchsion中有的数据，如果torchvison中没有，还有imagefolder,还有自己的数据集什么的要出路
###在遇到的时候再补充
