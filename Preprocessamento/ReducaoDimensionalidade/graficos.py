import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def grafico_violino(X, y, inicio, fim):
    
    dados_plot = pd.concat([y, X.iloc[:,inicio:fim]],axis = 1)
    dados_plot = pd.melt(dados_plot, id_vars="diagnostico",
                         var_name="exames",
                         value_name='valores')
    
    ax = plt.figure(figsize=(10, 10))
    ax = sns.violinplot(x = "exames", y = "valores", hue = "diagnostico",
                   data = dados_plot, split= True)
    ax = plt.xticks(rotation = 90)
    
    return ax


