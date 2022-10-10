# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:28:20 2022

@author: Ada
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

trade = pd.read_csv('data.csv') #

trade['date']=pd.to_datetime(trade['date'])
trade.sort_values(['ticker','date'],ascending= False)

trade['return']=trade.groupby('ticker')['last'].shift(0)/trade.groupby('ticker')['last'].shift(1)-1
trade['volchange']=trade.groupby('ticker')['volume'].shift(-1)/trade.groupby('ticker')['volume'].shift(0)-1

traindata=trade.loc[trade['date'].dt.year<2020]
testdata=trade.loc[trade['date'].dt.year>=2020]
f=traindata.groupby('date',as_index=True)['volchange','return'].corr()

def testfactor(df,factor1):
    df['rank']=df.groupby('date')[factor1].rank()
    df['rank']=df['rank']//20
    df=df.groupby('rank')['return','rank'].mean()
    plt.scatter(df['rank'],df['return'])

testfactor(traindata,'volchange')
testfactor(traindata,'volume')
testfactor(traindata,'last')

def backtesting(df,factor):
    df['rank']=df.groupby('date')[factor].rank()
    df['rank']=df['rank']//20
    df['return']= df['return']+1
    df=df.groupby(['date','rank'],as_index=False)['return','rank'].mean()
    df['return_c']=df.groupby('rank',as_index=True)['return'].cumprod()
    plt.scatter(df.loc[df['rank']==0,['date']],df.loc[df['rank']==0,['return_c']])
    
backtesting(testdata,'volchange')
