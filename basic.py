## loading libraries
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder


## functions
def clean_data(df1, df2=None):
    """Performs standard data cleaning functions
    Returns updated dataframes
    """
    
    def remove_constant_columns(df1, df2=None):
        """Removes all columns with constant value.
        Returns updated dataframes.
        """

        # creating panel
        if len(df2) > 0:
            panel = pd.concat([df1, df2], ignore_index=True)
        else:
            panel = df1

        # removing constant columns
        for i in train.columns:
            if len(np.unique(train[i].values.astype('str'))) == 1:
                del panel[i]
                print('Column %s is a constant column and is removed from data' % (str(i)))

        df1, df2 = panel.loc[0:len(df1),], panel.loc[len(df1):len(panel),]

        return df1, df2


    def convert_columns_to_binary(df1, df2=None):
        """Converts all columns with two elements into a binary column.
        Returns updated dataframes.
        """

        # creating panel
        if len(df2) > 0:
            panel = pd.concat([df1, df2], ignore_index=True)
        else:
            panel = df1


        change = False

        # converting two-element columns to binary column
        for i in train.columns:
            if len(np.unique(train[i].values.astype('str'))) == 2:
                if not all(np.unique(train[i].values.astype('str')) == ['0','1']):
                    label = LabelEncoder()
                    label.fit(list(panel[i].values))
                    panel[i] = label.transform(list(panel[i].values))

                    change = True
                    print('Column %s converted to binary' % (str(i)))

        if not change:
            print('No binary columns in data')

        df1, df2 = panel.loc[0:len(df1),], panel.loc[len(df1):len(panel),]

        return df1, df2


    df1, df2 = remove_constant_columns(df1, df2)
    df1, df2 = convert_columns_to_binary(df1, df2)
    
    return df1, df2
