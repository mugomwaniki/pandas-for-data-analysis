import pandas as pd
import numpy as np

#s = pd.Series([9,5,78,8,np.nan,9])
#print (s)
d= pd.date_range(20200317 ,periods=20)
#print (d)
df=pd.DataFrame(np.random.randn(20 ,4),index=d,columns=["A","B","C","D"])
#print(df)
df1=pd.DataFrame({'A':[1,2,3,4],
 'B':pd.Timestamp(20000719),
 'C':pd.Series(1,index=list(range(4)),dtype='float32'),
 'd':np.array([5]*4,dtype='int32'),
 'E':pd.Categorical(['true','false','true','false']),
 'F':'Mugo Mwaniki'})
#print(df1)
#print(df.head) =for first five values
#print(df.tail)= for last five values
#print(df.columns) =shows the columns
#print(df.index) =shows your indexes
#print(to_numpy) = creates a numphy array
#print(df.describe) = describes the dataframe in terms of count,mean,std,min,max.
#print (df.sort_index(axis=1,ascending= false)) =sorts index to your preference
#print('c')=prints data from a single column
#print(0:3) =gives data up to a certain point
#print(df.loc[d[0]])= extract data from a certain location
#print(df.loc[:,['A','D']])= extract data from a multi locations,,,,select multi acess using labels
#print(iloc[3:5,2:4]) = select values from a data frame

                  #HANDLING  MISSING DATA
#df2 = df.reindex(index= d[0,4], column=list(df.columns)+ ['E'])
#df2.loc[d[0]:d[1],'E'] = 1
#print(df2)

#print(df2.isnull) = checks null values
#print(df2.isnull().count) = counts null values
#(df2.dropna)   = the null values are dropped
#(df2.fillna(value=2)) = fills the missing values with 2 or either of choice

          #PANDAS OPERATIONS
# df.mean() shows mean   ===for one dataframe item   df.mean(1) 
#  The lambda function is given by (df.apply= (lambda x: x.max(-) - x.min())) 
                         
                 #                  ($$$string methods$$$)
s =pd.Series(["mugo mwaniki","python","Edureka","jupiter",np.nan,"liverpool"])
#print(s)
#df=pd.DataFrame(np.random.randn(10,4))
#print(df)

df2 = [df[:3],df[3:7],df[7:]]      #divides data in to pieces
print(df2)
pd.concat(df2) #concancates the missing pieces
             
             #LEFT & RIGHT JOINING

left = pd.DataFrame({'A':[1,2],'B':[3,4]})
right = pd.DataFrame({'C':[3,2],'B':[4,5]})

print(left)
print(right)

#pd.merge|(left,right,on='A') merges both 
#df.groupby(2).sum() #groups data using columns
#df.groupby(2,5).sum() #groups data using multiple columns

my_tuple = list(zip(*[[1,2,3,4,5,6,7,8],[11,12,15,16,17,18,18,10]]))

index =pd.MultiIndex.from_tuples(my_tuple,names=['first','last'])

#df=pd.DataFrame(np.random.randn(8,2),index=index,columns=['A', 'B'])

df2=df[:4]
print(df2)

df2.stack  #shows a stack of the data,,,to compress a level in adataframe % viceversa df.unstack
           

           #PIVOT TABLES IN PANDAS
df=pd.DataFrame({'A':['a','b','c','d'] * 3,
'B':['A','B','C'] * 4,
'C':['P','P','P','Q','Q','Q'],
'D':np.random.randn(12),
'E':np.random.randn(12)})


pd.pivot_table(df,values='D',index =['A','B'],columns=['C'])

          #TIME SERIES AND CATEGORICALS

dates = pd.date_range('20000719',periods = 100,freq='s')
ts= pd.Series(np.random.randint(0,500,len(dates),index=dates))
ts.resample('3min'),sum
dates = pd.date_range('20000719 00:00',periods = 7,freq='s')
ts= pd.Series(np.random.randn(len(dates),dates))
ts_utc =ts.tz_localize('UTC')

ts_utc.tz_convert('UK/Western')   #converts to another timezone

                 #PLOTTING USING PANDAS
import matplotlib.pyplot as plt
plt.close('all')
ts.pd.Series(np.random.randn(500),index=pd.date_range('19/07/2020',periods=500))
ts=ts.cumsum()
ts.plot()
          #PLOTTING WITH PANDAS
ts.to_csv("peter.csv")
pd.read_csv(r'C:\Users\Admin\Downloads\movies 2020.csv')
print(peter.csv)


















