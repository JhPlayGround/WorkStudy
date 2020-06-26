import altair as alt
from vega_datasets import data
import numpy as np
import pandas as pd


"""
영역 그래프  계단형
"""
#데이터 
source = data.stocks()

#공통 특성
base = alt.Chart().encode(x=alt.X('date', title='Date')).transform_filter(alt.datum.symbol == 'GOOG')

#영역 
area = base.mark_area(color="lightblue", interpolate='step-after', line=True).encode(y= alt.Y('price', title = 'Price'))

#합성
chart = alt.layer(area, data=source).properties(width = 600 , height=400, )
chart.save('Simple Area Chart.html')


"""
영역 그래프 + 색상 그라데이션
"""
area = base.mark_area(line={'color':'darkgreen'},
    color=alt.Gradient(gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0), alt.GradientStop(color='darkgreen', offset=1)],
        x1=1, x2=1, y1=1, y2=0)).encode(y= alt.Y('price', title = 'Price'))

#합성
chart = alt.layer(area, data=source).properties(width = 600 , height=400, )
chart.save('Simple Area Chart2.html')



"""
영역 그래프 + 특성별 분할
"""
source = data.iris()

base = alt.Chart().transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']).transform_density(
    density='value',
    bandwidth=0.3,
    groupby=['Measurement_type'],
    extent= [0, 8]
)

area = base.mark_area().encode(
    alt.X('value:Q'),
    alt.Y('density:Q')
).properties(width=600, height=100)

chart = alt.layer(area, data = source).facet(row='Measurement_type:N')

chart.save('Simple Area Chart3.html')


"""
영역 그래프 + 영역 겹치기
"""
source = data.iowa_electricity()

base = alt.Chart()

area = base.mark_area(opacity=0.3).encode(
    x=alt.X("year:T"),
    y=alt.Y("net_generation:Q"),
    color="source:N"
)

chart = alt.layer(area, data = source)
chart.save('Simple Area Chart4.html')


"""
영역 그래프 + 정규화
"""
base = alt.Chart()

area = base.mark_area(opacity=0.7).encode(
    x=alt.X("year:T"),
    y=alt.Y("net_generation:Q", stack='normalize'),
    color="source:N"
)

chart = alt.layer(area, data = source)
chart.save('Simple Area Chart5.html')



"""
영역 그래프 + 기준 값 동일하게 맞춤
"""
source = data.iris()

base = alt.Chart().transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']).transform_density(
    density='value',
    bandwidth=0.3,
    groupby=['Measurement_type'],
    extent= [0, 8],
    counts = True,
    steps = 200
)

area = base.mark_area().encode(
    alt.X('value:Q'),
    alt.Y('density:Q', stack='zero'),
    alt.Color('Measurement_type:N')
).properties(width=600, height=100)

chart = alt.layer(area, data = source)


chart.save('Simple Area Chart6.html')


"""
영역 그래프 (스트림 그래프)
"""
source = data.unemployment_across_industries.url

base = alt.Chart()

#interactive() 적용시 상하좌우 이동 가능 → 데이터가 없어도 상하좌우 이동 가능
area = base.mark_area().encode(
    alt.X('yearmonth(date):Q', axis=alt.Axis(format='%Y', domain=True, tickSize=0)), 
    alt.Y('sum(count):Q', stack='center', axis=None),
    alt.Color('series:N',scale=alt.Scale(scheme='category20b'))
).interactive()

chart = alt.layer(area, data = source)
chart.save('Simple Area Chart7.html')


"""
영역 그래프 - 분할 해서 그리기
"""
source = data.iowa_electricity()

base = alt.Chart()

area = base.mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N"
).properties(
    height=100
)

chart = alt.layer(area, data = source).facet(row="source:N")
chart.save('Simple Area Chart8.html')


"""
영역 그래프 - 분할 정렬 해서 그리기
"""
source = data.stocks()

base = alt.Chart()

area = base.mark_area().encode(
    x=alt.X('date:T', title='Date'),
    y=alt.Y('price:Q', title='Price'),
    color='symbol:N'
).properties(height=50, width=400)

chart = alt.layer(area, data= source).facet(row=alt.Row('symbol:N', sort=['MSFT', 'AAPL', 'IBM', 'AMZN','GOOG']))
chart.save('Simple Area Chart9.html')