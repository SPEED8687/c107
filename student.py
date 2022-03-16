import pandas as pd
import plotly.graph_objects as go
df=pd.read_csv('c107csv.csv')
studentdf=df.loc[df['student_id']=='TRL_xyz']
graph=go.Figure(go.Bar(x=studentdf.groupby('level')['attempt'].mean(),y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
graph.show()