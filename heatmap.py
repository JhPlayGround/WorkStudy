import altair as alt
import numpy as np
import pandas as pd
import seaborn as sns

# 데이터
flights = sns.load_dataset('flights')
source = pd.DataFrame({'연도': flights['year'], '월': flights['month'],'탑승자 수': flights['passengers']})

#그리기
chart = alt.Chart(source, title="연도 경과에 따른 월별 비행기 탑승자 수").mark_rect().encode(
    alt.X('연도:O', scale=alt.Scale(paddingInner=0)),
    alt.Y('월:O', scale=alt.Scale(paddingInner=0)),
    color=alt.Color('탑승자 수:Q', scale=alt.Scale(scheme="greenblue"), legend=alt.Legend(direction='horizontal')),
    tooltip=[alt.Tooltip('연도:O', title='연도'), alt.Tooltip('월:O', title='월'), alt.Tooltip('탑승자 수:Q', title='탑승자 수')],
).properties(width=550, height=300)

#저장
chart.save('heatmap.html')