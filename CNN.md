|名称  |  来源   | 说明  |状态   | 备注  |
|  ----  | ----  |----  | ----  |----  |
| 《Gradient-Based Learning Applied to Document Recognition》| Proceedings of the IEEE 1998|Lenet5：<br/>1 最终预测使用BRF而不是Softmax；<br/>2 端到端的数字序列识别GTN部分没看懂，好像网上的中文介绍也没怎么见到；|NULL |NULL |
| 《ImageNet Classification with Deep Convolutional Neural Networks》 | NIPS 2012 |Alexnet：<br/>0 SOTA-ILSVRC-2012；<br/>1 采用Relu作为激活函数；<br/>2 使用两个GPU；<br/>3 采用LRN；<br/>4 Overlapping<br/> Pooling；<br/>5 采用Dropout；  |NULL |NULL |
| 《Network In Network》| ICLR 2014|NIN网络：<br/>1 引入Mlpconv layer，即1x1卷积；<br/>2 最后一层使用了Global Average Pooling；|NULL |Global average pooling参考：mountain blue：Global average pooling--<Network In Network>
| 《VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION》| ICLR2015|牛津大学VGGNet：<br/>0 SOTA-ImageNet2014；<br/>1 只使用3x3的小核(两个堆叠的3x3小核等效7x7的大核)；<br/>2 深度达16~19层；<br/>3 证明LRN无效（AlexNet中使用过）；<br/>使用Caffe进行训练（支持多卡GPU）；|NULL |NULL |
| 《Going deeper with convolutions》 | CVPR2015 |InceptionNet/GoogleLeNet：<br/>1 SOTA-ILSVRC14；<br/>2 引入Inception模块（不同尺寸的卷积）DepthConcat；<br/>3 卷积核主要是7x7,3x3,5x5，参数降低通过1x1卷积实现；<br/>4 22个参数层；<br/>5 在网络中间添加预测任务，增强底层网络的判别能力，相当于正则操作；<br/>6 通过DistBelife（TensorFlow的前身）进行训练； |NULL |DepthConcat：https://qastack.cn/stats/184823/how-does-the-depthconcat-operation-in-going-deeper-with-convolutions-work |
| 《Deep Residual Learning for Image Recognition》 | CVPR2016 |何凯明、孙剑的残差网络：<br/>1 SOTA-ILSVRC-2015；<br/>2 152层，8倍VGG；<br/>3 没特别理解Residual和Shortcuts的论文分析理解不是很充分； |NULL |Hightway network：Uno Whoiam：Highway Networks：ResNet，我是你爸爸 |
| NULL  | NULL |NULL |NULL |NULL |
