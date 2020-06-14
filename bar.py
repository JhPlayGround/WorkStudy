import altair as alt
import pandas as pd
from vega_datasets import data

source = data.wheat()

chart = alt.Chart(source).mark_bar().encode(
    x='year:O',
    y="wheat:Q",
    color=alt.condition(
        alt.datum.wheat >= 50,
        alt.value('orange'),    
        alt.value('steelblue')  
    )
).properties(width=1200, height=600)

text = chart.mark_text(
    align='right',
    baseline='bottom', 
    dx=6
).encode(
    text='wheat:Q'
)

rule = alt.Chart(source).mark_rule(color='red').encode(
    y='mean(wheat):Q'
)

chart = chart + text + rule

chart.save('bar.html')


