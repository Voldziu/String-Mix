import pandas as pd
import numpy as np

def mix(s1, s2):
    ls1=[]
    ls2=[]
    l1=[]
    l2=[]
    for i in s1:

        if i.islower():
            ls1.append(i)

    for i in s2:
        if i.islower():
            ls2.append(i)

    ls1= list(set(ls1))
    for i in ls1:
        l1.append(s1.count(i))
    ls2=list(set(ls2))
    for i in ls2:
        l2.append(s2.count(i))

    al1 = np.column_stack((ls1,l1))
    al2 = np.column_stack((ls2,l2))

    df1=pd.DataFrame(data=al1)
    df2=pd.DataFrame(data=al2)
    # print(df1.sort_values(by=1,ascending=False))
    # print(df2.sort_values(by=1,ascending=False))
    lol = pd.merge(df1,df2,how='outer',on=0)
    lol = lol.fillna(0)
    lol.columns =['literka','s1','s2']


    def chuj(x):
        literka = x['literka']
        s1 = x['s1']
        s2= x['s2']
        if int(s1) >int(s2):
            if int(s1)==1:
                return 'p'
            else:
                return '1:'+literka*int(s1)
        elif int(s2)>int(s1):
            if int(s2)==1:
                return 'p'
            else:
                return '2:'+literka*int(s2)
        else:
            if int(s1)==1:
                return "p"
            else:
                return '=:'+literka*int(s1)
    lol['p'] = lol.apply(chuj,axis=1)
    lol =lol[lol['p']!='p']
    lol['s1'] = lol['s1'].apply(int)
    lol['s2'] = lol['s2'].apply(int)
    lol['da']=lol[['s1','s2']].apply(np.max,axis=1)
    lol = lol.sort_values(by=['da','p'],ascending=[0,1])
    j = lol['p'].values
    napis =''
    for i in j:
        napis +=i+"/"
    return napis[:-1]








