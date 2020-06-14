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



chart.save('bar.html')


