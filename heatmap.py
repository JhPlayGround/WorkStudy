#차트 라이브러리
import altair as alt
from altair_saver import save

#기본 라이브러리
import numpy as np
import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#데이터셋 라이브러리
from vega_datasets import data

import seaborn as sns
flights = sns.load_dataset('flights')
source = pd.DataFrame({'Year': flights.year, 'Month':flights.month, 'Passengers':flights.passengers})

#기본 히트맵
base = alt.Chart(source, title="연도 경과에 따른 월별 비행기 탑승 고객수").encode(
    x='Year:O', y='Month:O'
    
).properties(width=550, height =300)

#툴팁, 색상
heatmap = base.mark_rect().encode(
    color=alt.Color('Passengers:Q', scale=alt.Scale(scheme="viridis"), legend=alt.Legend(direction='horizontal')),
    tooltip=[alt.Tooltip('Year:O', title='연도 '), alt.Tooltip('Month:O', title='월'), alt.Tooltip('Passengers:Q', title='탑승객 수')]
)

#텍스트 부분
text = base.mark_text(baseline = 'middle').encode(
    text = 'Passengers',
    color=alt.condition(
        alt.datum.Passengers > 300,
        alt.value('black'),
        alt.value('white')
    )
)

# 툴팁, 색상 히트맵 + 텍스트
chart = (heatmap + text)

chart.save('Simple Heatmap.html')
