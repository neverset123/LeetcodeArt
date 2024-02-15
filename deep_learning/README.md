## CNN
具有位移不变性，权值共享
### Dimension
$$
W_out= (W-F+2*P)/S +1
H_out= (H-F+2*P)/S +1
D_out = K
volume = w_out*H_out*D_out
W: width, H: height, F: filter size, S: stride, P: padding, K: filter number
$$
$$
共享权重参数个数 = (F_width*F_height*F_Depth+1)*(out_width*out_height*out_depth)
不共享权重参数个数 = (F_width*F_height*F_Depth+1)*out_depth
$$
### Pooling
因为Pooling可以用步长大于1的卷积替代，所以Pooling并不必要。
### type
1) 1x1 conv
2) inception
对输入数据同时进行average pooing, 3x3 conv, 1x1 conv和5x5 conv.

## Transformer




