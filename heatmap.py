import altair as alt
import numpy as np
import pandas as pd
import seaborn as sns

# 데이터
flights = sns.load_dataset('flights')
source = pd.DataFrame({'Year': flights['year'], 'Month': flights['month'],'Passengers': flights['passengers']})

#그리기
chart = alt.Chart(source, title="연도 경과에 따른 월별 비행기 탑승자 수").mark_rect().encode(
    x='Year:O',
    y='Month:O',
    color=alt.Color('Passengers:Q', scale=alt.Scale(scheme="inferno")),
    tooltip=[alt.Tooltip('Year:O', title='연도'), alt.Tooltip('Month:O', title='월'), alt.Tooltip('Passengers:Q', title='탑승자 수')]
).properties(width=550, height=300)

#저장
chart.save('heatmap.html')