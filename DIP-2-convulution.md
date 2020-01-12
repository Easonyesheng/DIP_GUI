# 数字图像处理总结2

卷积运算和图像滤波

------

## 卷积运算

对图像的操纵分为点操作，代数操作，几何操作和领域操作。  
卷积运算就是领域操作中的一个，而提到卷积，就不得不说他的姊妹correlation。  
话不多说，先看公式：  
convolution : $f*w=\sum_{(a,b)\in w}f(x-a,y-b)w(a,b)$  
correlation : $f \bigotimes w=\sum _{(a,b) \in w}f(x+a,y+b)w(a,b) $  
f是原图，k是kernel。a,b是kernel中的点坐标，默认kernel的中心坐标为（0，0）。  
可以看出两者的区别主要是原图的坐标变换是+ or -  
而且因为convolution是 - ，在代码中具体运算时，需要将kernel旋转$180^\circ$。  
一句话描述卷积的过程：对一个以某点为中心，kernel大小的原图区域，对应乘上旋转过的kernel的元素并求和，结果来作为kernel中心那个像素的新的灰度值，对图中所有点作该操作，就是一个卷积。  

------

## 图像滤波  

图像滤波就是用不同的kernel进行卷积操作。  
根据kernel的不同，又分为很多目的不同的操作，如边缘检测、图像平滑等。  
下面就举几个常见的例子：  

------

### Edge Detection

**典型算子：**
Roberts：
$$
\left |
 \begin{matrix}
  -1 & 0 \\
  0 & 1 \\
 \end{matrix}
\right |
$$
$$
\left |
 \begin{matrix}
  0 & -1 \\
  1 & 0 \\
 \end{matrix}
\right |
$$

Prewitt:
$$
\left |
 \begin{matrix}
  -1 & -1 & -1 \\
  0 & 0 & 0 \\
  1 & 1 & 1 \\
 \end{matrix}
\right |
$$
$$
\left |
 \begin{matrix}
  -1 & 0 & 1 \\
  -1 & 0 & 1 \\
  -1 & 0 & 1 \\
 \end{matrix}
\right |
$$
Sobel:
$$
\left |
 \begin{matrix}
  -1 & -2 & -1 \\
  0 & 0 & 0 \\
  1 & 2 & 1 \\
 \end{matrix}
\right |
$$
$$
\left |
 \begin{matrix}
  -1 & 0 & 1 \\
  -2 & 0 & 2 \\
  -1 & 0 & 1 \\
 \end{matrix}
\right |
$$
通过观察可以看出，这三个算子都强调不同像素间的差，其实就是离散形式的导数，所以这三个算子都是在求图片的梯度。  
而求梯度，就是突出变化，也就是能够得到图片的中像素值变化剧烈的地方，也就是边缘。  

------

### 图像平滑

**典型算子：**
平均滤波：
$$
\left [
 \begin{matrix}
  1/9 & 1/9 & 1/9 \\
  1/9 & 1/9 & 1/9 \\
  1/9 & 1/9 & 1/9 \\
 \end{matrix}
\right ]
$$
中值滤波：
这个算子不是寻常的计算算子，而是将3x3范围内的中值作为中心的灰度值。  
是一种统计学算子。  
Gaussian:  
$G(x,y)={1/{2\pi \sigma^2}} \times e^{-{x^2+y^2}/{2\sigma^2}}$
这个式子指的是高斯滤波器对应位置的值，其中一个关键元素是$\sigma$，是方差，在滤波时一般自己选定，他决定了高斯分布的峰高和宽（越大越矮、宽）  

------

## Code

实现时主要是依赖于opencv的

```python
cv2.filter2D(img,-1,filter)
```

这里的算法都可以在我的GitHub里的[项目](https://github.com/Easonyesheng/DIP_GUI)里找到  
该项目是一个包括阈值分割、卷积滤波、形态学和灰度形态学的数字图像处理算法集合  
且带有GUI，有很好的演示效果  
觉得可以别忘了star哦  
