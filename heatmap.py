import altair as alt
import numpy as np
import pandas as pd
import seaborn as sns

# 데이터
flights = sns.load_dataset('flights')
source = pd.DataFrame({'Year': flights['year'], 'Month': flights['month'],'Passengers': flights['passengers']})


#그리기
chart = alt.Chart(source).mark_rect().encode(
    x='Year:O',
    y='Month:O',
    color='Passengers:Q'
)

#저장
chart.save('heatmap.html')