import torch
import torchvision.transforms as transforms  #torchvision.transform是pytorch中数据处理的模块
import torchvision.datasets as datasets      #torchvision.datasets是pytorch中存储数据的模块，对于常用数据集
                                             #直接提供在线下载的功能，若自己手中数据集已有，则另doemload=Flase

def load_data(args):
    if args.dataset_mode == "CIFAR10":
            transform_train = transforms.Compose([                     #transform.Compose函数是将各种对数据的处理组合起来的一个函数而已
                transforms.Resize(224),
                transforms.RandomCrop(224, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),                                  #在进行transform.Normalize的处理之前一定要有transform.Totensoer
                                                                        #因为之前的数据处理操作都是对图像而言的，而这一次归一化的是Tensor,所以一定要有这一步的变化
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),  #每个通道方差和标准差的操作，具体的数值不同的数据不一样，用到时再上网查找
            ])

            transform_test = transforms.Compose([
                transforms.Resize(224),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])
            #定义好数据的各种变换之后，就先该下载数据，下载好数据之后在做变换，之后再得到train_data了，
            #注意注意一定要注意！！！如果按这个下载会相当慢，如果自己已经下好了数据，就在root这里写好数据地址就行，
            #dowmload写为Flase就行，但是一定要记住，路径一定要写到数据集的上一级！！！！！！！一定要写到上一级！
            train_data = datasets.CIFAR10(root='C:\\Users\\asus\Desktop\MobileNetV3-Pytorch-master', train=True, download=False, transform=transform_train)
            test_data = datasets.CIFAR10(root='C:\\Users\\asus\Desktop\MobileNetV3-Pytorch-master', train=False, download=False, transform=transform_test)
            #下载好数据后，就该把数据加载到网络了，这时候就需要加载器加载，也会有batchsize什么的
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
