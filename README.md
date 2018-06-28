# Wind_predict_seq2seq
基于seq2seq模型的风功率预测<br>

# 版本要求
python3.6<br>
tensorflow>=1.4<br><br>
# 网络说明
1.利用简单神经网络将缺失数据补全<br>
2.基于seq2seq模型训练数据<br>
seq2seq模型示意图<br>
![](https://github.com/LeslieZhoa/Wind_predict_seq2seq/blob/master/img/1.png)

# 文件说明
## 数据 data/
2015年5,6月数据具体完整版.xlsx:原始风功率数据<br>
fitt.h5:剔除缺损数据，分好x,y<br>
twomonthes.h5:重载补全数据神经网络补全数据<br>
tdata1.h5:分好序列的数据文件<br>
## 程序
data.ipynb：数据处理代码相关说明(其中重载路径需重新定义)<br>
fitted.ipynb:补全数据网络的训练<br>
untitled0.py：重载补全数据网络代码脚本<br>
wind.ipynb:风功率预测训练代码<br><br>
# 结果显示
准确率采取1-均方根误差，其中验证集最好准确率为94%，可视化预测值与真实值曲线如下：<br>
![](https://github.com/LeslieZhoa/Wind_predict_seq2seq/blob/master/img/show.png)
# 参考文献
[Sutskever I, Vinyals O, Le Q V. Sequence to Sequence Learning with Neural Networks[J]. 2014, 4:3104-3112.](http://xueshu.baidu.com/s?wd=paperuri%3A%28e9aa7b19ac49e6698424e934d418e05b%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Farxiv.org%2Fabs%2F1409.3215&ie=utf-8&sc_us=5597873999363172369)
