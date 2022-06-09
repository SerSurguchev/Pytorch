# CycleGan implementation from scratch using PyTorch

Paper: [link](https://www.kaggle.com/datasets/balraj98/horse2zebra-dataset)


Horses and zebras dataset can be downloaded from Kaggle: [link](https://www.kaggle.com/datasets/balraj98/horse2zebra-dataset)


6 residual blocks is used for 128 × 128 training images, and 9 residual blocks for 256 ×256 or higher-resolution training images. 9 residual block was implemented in this project.


Let c7s1-k denote a 7×7 Convolution-InstanceNormReLU layer with k filters and stride 1. dk denotes a 3 × 3 Convolution-InstanceNorm-ReLU layer with k filters and stride 2. Reflection padding was used to reduce artifacts.

Rk denotes a residual block that contains two 3 × 3 convolutional layers with the same number of filters on both layer. uk denotes a 3 × 3 fractional-strided-ConvolutionInstanceNorm-ReLU layer with k filters and stride 1/2.


The network with 6 residual blocks consists of:

c7s1-64,d128,d256,R256,R256,R256,R256,R256,R256,u128,u64,c7s1-3

The network with 9 residual blocks consists of:

c7s1-64,d128,d256,R256,R256,R256,
R256,R256,R256,R256,R256,R256,u128
u64,c7s1-3
