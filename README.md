# data_testing
The analysis is simple. 
Divide the dataset into traindata and testdata.
Use traindata to do step 1) and step 2)
Use testdata to do step 3)--the backtest
1)get 'return' and the change of vol (vol_{t}/vol_{t-1}-1)
2)Group the stocks for each 20 (changeable) and check which sorted variable can drive cross section return
![image](https://user-images.githubusercontent.com/108187125/195058492-f8c72d1c-ca51-48ef-a370-3b7f599dd5ce.png)
3)choose the change of vol to sort the stocks and buy the first group of stocks, sell the position of yesterday. The plot of cumulative rate of return is show below. 
![image](https://user-images.githubusercontent.com/108187125/195076750-60e8ad7c-2ded-4037-89d3-e66c14d12184.png)
