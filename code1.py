import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/choiminseok/Desktop/최민석/야구/야구공작소/속구 모양과 변화구/stats.csv')
html_table = df.to_html('/Users/choiminseok/Desktop/최민석/야구/야구공작소/속구 모양과 변화구/data.html')
df = df.fillna(0)
compare = df.columns[5:]
df['max_col'] = df[compare].idxmax(axis=1)

colors = {
    'n_sl_formatted': 'red',
    'n_ch_formatted': 'green',
    'n_cu_formatted': 'blue',
    'n_si_formatted': 'yellow',
    'n_fc_formatted': 'orange',
    'n_fs_formatted': 'purple',
    'n_st_formatted': 'cyan',
    'n_fo_formatted': 'magenta'
}
df['color'] = df['max_col'].map(colors)

plt.scatter(df['ff_avg_break_x'], df['ff_avg_break_z'], c = df['color'])
plt.show()
