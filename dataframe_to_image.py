import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table # EDIT: see deprecation warnings below

df = pd.DataFrame({'column1':[i for i in 'fuckyou'],'column2':[i for i in 'youfuck']})

ax = plt.subplot(111, frame_on=False) # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis

table(ax, df)  # where df is your data frame

plt.savefig('mytable.png')

df.to_html('table.html')
# subprocess.call('wkhtmltoimage -f png --width 0 table.html table.png', shell=True)