Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
np.eye(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
np.arange (10,50)
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
       44, 45, 46, 47, 48, 49])
import numpy as np
x=np.zeros(10)
print(x)
SyntaxError: multiple statements found while compiling a single statement
x=np.zeros(10)
print(x)
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
y=np.random.random((3,3,3))

print(y)
[[[0.65207347 0.07334105 0.78545587]
  [0.47948054 0.96201036 0.18313461]
  [0.42060146 0.74661779 0.03370803]]

 [[0.84664565 0.69146459 0.6426834 ]
  [0.77547067 0.43461002 0.93503923]
  [0.31946205 0.57932325 0.03064779]]

 [[0.34962324 0.53629324 0.54598438]
  [0.5029876  0.32970178 0.63284899]
  [0.40707978 0.97910031 0.76494229]]]
z=np.zeros(10)
print(z)
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
z[5]=1
print(z)
[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(1,10)
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(1,10,2)
array([1, 3, 5, 7, 9])
>>> q=np.random,random((4,2))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    q=np.random,random((4,2))
NameError: name 'random' is not defined
>>> q=np.random.random((4,2))
>>> print(q)
[[0.27441836 0.03087887]
 [0.30304806 0.35588422]
 [0.94100642 0.86560303]
 [0.46133721 0.55845418]]
>>> q.ndim
2
>>> q.shape
(4, 2)
>>> np.linspace(start=100,stop=200,num=10)
array([100.        , 111.11111111, 122.22222222, 133.33333333,
       144.44444444, 155.55555556, 166.66666667, 177.77777778,
       188.88888889, 200.        ])
>>> a=[1,2,3,4,5,6,7,8,9]
>>> import numpy as np
>>> a1=np.array(a)
>>> print(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(np.array(a))
<class 'numpy.ndarray'>
>>> b=np.arange(1,28).reshape(4,4)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    b=np.arange(1,28).reshape(4,4)
ValueError: cannot reshape array of size 27 into shape (4,4)
