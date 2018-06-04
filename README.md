# Wind_predict_seq2seq
基于seq2seq模型的风功率预测<br>

# 版本要求
python3.6<br>
tensorflow>=1.4<br><br>
# 网络说明
1.利用简单神经网络将缺失数据补全<br>
2.基于seq2seq模型训练数据<br>
seq2seq模型示意图<br>
![]()

# 文件说明
data.ipynb:数据处理文件<br>
fitted.ipynb:补全数据神经网络—-训练<br>
untitled0.py:补全数据神经网络--重载<br>
v1.1.ipynb:seq2seq网络<br>
v1.1g.ipynb:seq2seq网络修改<br><br>
# 参考文献
[Sutskever I, Vinyals O, Le Q V. Sequence to Sequence Learning with Neural Networks[J]. 2014, 4:3104-3112.](http://xueshu.baidu.com/s?wd=paperuri%3A%28e9aa7b19ac49e6698424e934d418e05b%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Farxiv.org%2Fabs%2F1409.3215&ie=utf-8&sc_us=5597873999363172369)
