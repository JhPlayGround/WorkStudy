import altair as alt
from vega_datasets import data
import numpy as np
import pandas as pd
import seaborn as sns

#데이터 변경
source = data.seattle_weather()
source = pd.DataFrame(source)

for i in range(source.shape[0]):
    source.loc[i, 'date'] = str(source.loc[i, 'date'])[:10]
    source.loc[i, 'month'] = str(source.loc[i, 'date'])[5:7]

source = source.groupby(source['month']).mean()
source['months'] = ['01','02','03','04','05','06','07','08','09','10','11', '12']
source['temp_avg'] = (source['temp_max'] + source['temp_min'])/2
source['precipitation'] = round(source['precipitation'],2)
source['temp_max'] = round(source['temp_max'],2)
source['temp_min'] = round(source['temp_min'],2)
source['wind'] = round(source['wind'],2)
source['temp_avg'] = round(source['temp_avg'],2)

"""
일반 막대 그래프
"""
base = alt.Chart(source).encode(x='months:O')
bar = base.mark_bar(
    # 막대 그래프 끝 부분 둥글게
    cornerRadiusTopLeft = 10,
    cornerRadiusTopRight = 10,
    cornerRadiusBottomLeft = 10,
    cornerRadiusBottomRight = 10
).encode(
    y='temp_max:Q',
    # 특정값 이상이면 색상 변화
    color=alt.condition(
        alt.datum.temp_max > 16.39,
        alt.value('pink'),    
        alt.value('green')  
    )
)

#텍스트
text = bar.mark_text(
    align='center',
    baseline='bottom', 
    dx=6
).encode(
    text='temp_max:Q'
)

#기준선
rule = alt.Chart(source).mark_rule(color='blue').encode(
    y='mean(temp_max):Q'
)

#새로운 축
line =  base.mark_line(color='orange').encode(
    y='temp_min:Q'
)

#tik 추가
tick = base.mark_tick(
    color='red',
    thickness=2,
    size=60 * 0.9,  # controls width of tick.
).encode(
    y='temp_avg:Q',
)

#실제 그래프
chart = (bar + text + rule + line + tick).properties(width = alt.Step(60) , height=400, )
chart.save('Simple Bar Chart.html')

"""
퍼센트 막대 그래프
"""
source = pd.DataFrame({'Activity': ['Sleeping', 'Eating', 'TV', 'Work', 'Exercise'],
                           'Time': [8, 2, 4, 8, 2]})

base = alt.Chart(source).transform_joinaggregate(
    TotalTime='sum(Time)',
).transform_calculate(
    PercentOfTotal="datum.Time / datum.TotalTime"
).encode(
    x = alt.X('PercentOfTotal:Q', axis=alt.Axis(format='.0%'))
)

bar = base.mark_bar().encode(
    y='Activity:N'
)



chart = (bar).properties(width = 600 , height=400 )

chart.save('Simple Percnet Bar Chart.html')