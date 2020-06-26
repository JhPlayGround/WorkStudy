import altair as alt
from vega_datasets import data
import numpy as np
import pandas as pd



"""
라인 그래프 + 신뢰 구간 + 포인트
"""
#데이터
source = data.cars()

#공통 특성
base = alt.Chart(source).encode(x=alt.X('Year', title='Year'))

#라인, 포인트
line = base.mark_line(point=True).encode(
    y=alt.Y('mean(Miles_per_Gallon)', title='Miles/Gallon'),
)

#신뢰 구간
band = base.mark_errorband(extent='ci').encode(
    y=alt.Y('Miles_per_Gallon', title='Miles/Gallon'),
)

#합성
chart = alt.layer(line, band).properties(width=550)
chart.save('Simple Line Chart.html')

"""
라인 그래프 + 집계선 추가
"""
#데이터
source = data.stocks()

#공통 특성
base = alt.Chart(data=source).encode(color = 'symbol')

#라인
line = base.mark_line().encode(
    x=alt.X('date', title='Date'),
    y=alt.Y('price', title = 'Price'),
)

#집계선
rule = base.mark_rule().encode(
    y='average(price)',
    size=alt.value(2)
)

#합성
chart = alt.layer(line, rule).properties(width=550)
chart.save('Simple Line Chart2.html')

"""
라인 그래프 + y축 비율 
"""
#데이터
source = data.jobs.url

#공통 특성
base = alt.Chart(source)

#라인
line = base.mark_line().encode(
    alt.X('year:O'),
    alt.Y('perc:Q', axis=alt.Axis(format='%')),
    color='sex:N'
).transform_filter(
    alt.datum.job == 'Welder'
)

#합성
chart = alt.layer(line).properties(width=550)
chart.save('Simple Line Chart3.html')


"""
라인 그래프 + 가변 두께
"""
#데이터
source = data.stocks()

#공통 특성
base = alt.Chart(data=source).encode(color = 'symbol')

#라인
line = base.mark_trail().encode(
    x=alt.X('date', title='Date'),
    y=alt.Y('price', title = 'Price'),
    size = 'price'
)


#합성
chart = alt.layer(line).properties(width=550)
chart.save('Simple Line Chart4.html')



"""
라인 그래프 + 값별로 다른 선
"""
#데이터
source = data.stocks()

#공통 특성
base = alt.Chart(data=source).encode(color = 'symbol', strokeDash='symbol')

#라인
line = base.mark_line().encode(
    x=alt.X('date', title='Date'),
    y=alt.Y('price', title = 'Price')
)


#합성
chart = alt.layer(line).properties(width=550)
chart.save('Simple Line Chart5.html')

"""
라인 그래프 계단형
"""
source = data.stocks()

#공통 특성
base = alt.Chart(data=source).encode(color = 'symbol', strokeDash='symbol')

#라인
line = base.mark_line(interpolate='step-after').encode(
    x=alt.X('date', title='Date'),
    y=alt.Y('price', title = 'Price')
)
chart = alt.layer(line).properties(width=550)
chart.save('Simple Line Chart6.html')