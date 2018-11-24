import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('~/train.csv')

#column names
df.columns

# Dimentions
df.shape


# Column Describers
 columndescribers=pd.DataFrame({
                                'columns' : df.columns, 
                                'coltypes': df.dtypes,
                                'coldistinctcounts':df.apply(pd.Series.nunique)
                            })



# Column Lists
numericcols=['LotFrontage','LotArea','YearBuilt','YearRemodAdd','MasVnrArea','BsmtFinSF1','BsmtFinSF2','BsmtUnfSF','TotalBsmtSF','1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','Fireplaces','GarageYrBlt','GarageCars','GarageArea','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal','MoSold','SalePrice']
categoricalcols= list((set(df.columns)-(set(numericcols)))-set(['Id']))



# dataframes with same types
dfnumeric=df.filter(items=numericcols)
dfcategorical=df.filter(items=categoricalcols)

#Description of numeric columns
descriptions=dfnumeric.describe()



#Correlations of numeric columns
%matplotlib inline
corr = dfnumeric.corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)


#Correlations of all columns

corr1 = df.corr()
sns.heatmap(corr1, xticklabels=corr1.columns.values, yticklabels=corr1.columns.values)



#Missing Value percentages

Missingpercentages = pd.DataFrame({(len(df.index)-df.count())/len(df.index)})



# Duplicated rows
Duplicated=df[df.duplicated()]



# Histograms


def draw_histograms(df, variables, n_rows, n_cols):
    fig=plt.figure()
    for i, var_name in enumerate(variables):
        ax=fig.add_subplot(n_rows,n_cols,i+1)
        df[var_name].hist(bins=10,ax=ax)
        ax.set_title(var_name+" Distribution")
    fig.tight_layout()  # Improves appearance a bit.
    plt.show()

draw_histograms(df, df.columns[list(range(1, 9))], 3, 3)
draw_histograms(df, df.columns[list(range(10,18))], 3, 3)
draw_histograms(df, df.columns[list(range(19,27))], 3, 3)
draw_histograms(df, df.columns[list(range(28,36))], 3, 3)
draw_histograms(df, df.columns[list(range(37, 45))], 3, 3)
draw_histograms(df, df.columns[list(range(46, 54))], 3, 3)
draw_histograms(df, df.columns[list(range(55, 63))], 3, 3)
draw_histograms(df, df.columns[list(range(64, 72))], 3, 3)
draw_histograms(df, df.columns[list(range(73, 81))], 3, 3)
















