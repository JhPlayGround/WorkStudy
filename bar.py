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
#Y축 내용 변경
y_axis = alt.Axis(
    title='평균 최고 기온',
    offset=0,
    ticks=False,
    minExtent=10,
    domain=False
)

x_axis = alt.Axis(
    title='월',
    offset=0,
    ticks=False,
    minExtent=10,
    domain=False
)

base = alt.Chart(source).encode(x = alt.X('months:O', axis=x_axis))
bar = base.mark_bar(
    # 막대 그래프 끝 부분 둥글게
    cornerRadiusTopLeft = 10,
    cornerRadiusTopRight = 10,
    cornerRadiusBottomLeft = 10,
    cornerRadiusBottomRight = 10
).encode(
    y = alt.Y('temp_max:Q', axis=y_axis),
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



"""
Diverging Stacked Bar Chart
"""
source = alt.pd.DataFrame([
      {
        "question": "Question 1",
        "type": "Strongly disagree",
        "value": 24,
        "percentage": 0.7,
        "percentage_start": -19.1,
        "percentage_end": -18.4
      },
      {
        "question": "Question 1",
        "type": "Disagree",
        "value": 294,
        "percentage": 9.1,
        "percentage_start": -18.4,
        "percentage_end": -9.2
      },
      {
        "question": "Question 1",
        "type": "Neither agree nor disagree",
        "value": 594,
        "percentage": 18.5,
        "percentage_start": -9.2,
        "percentage_end": 9.2
      },
      {
        "question": "Question 1",
        "type": "Agree",
        "value": 1927,
        "percentage": 59.9,
        "percentage_start": 9.2,
        "percentage_end": 69.2
      },
      {
        "question": "Question 1",
        "type": "Strongly agree",
        "value": 376,
        "percentage": 11.7,
        "percentage_start": 69.2,
        "percentage_end": 80.9
      },

      {
        "question": "Question 2",
        "type": "Strongly disagree",
        "value": 2,
        "percentage": 18.2,
        "percentage_start": -36.4,
        "percentage_end": -18.2
      },
      {
        "question": "Question 2",
        "type": "Disagree",
        "value": 2,
        "percentage": 18.2,
        "percentage_start": -18.2,
        "percentage_end": 0
      },
      {
        "question": "Question 2",
        "type": "Neither agree nor disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 2",
        "type": "Agree",
        "value": 7,
        "percentage": 63.6,
        "percentage_start": 0,
        "percentage_end": 63.6
      },
      {
        "question": "Question 2",
        "type": "Strongly agree",
        "value": 11,
        "percentage": 0,
        "percentage_start": 63.6,
        "percentage_end": 63.6
      },

      {
        "question": "Question 3",
        "type": "Strongly disagree",
        "value": 2,
        "percentage": 20,
        "percentage_start": -30,
        "percentage_end": -10
      },
      {
        "question": "Question 3",
        "type": "Disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": -10,
        "percentage_end": -10
      },
      {
        "question": "Question 3",
        "type": "Neither agree nor disagree",
        "value": 2,
        "percentage": 20,
        "percentage_start": -10,
        "percentage_end": 10
      },
      {
        "question": "Question 3",
        "type": "Agree",
        "value": 4,
        "percentage": 40,
        "percentage_start": 10,
        "percentage_end": 50
      },
      {
        "question": "Question 3",
        "type": "Strongly agree",
        "value": 2,
        "percentage": 20,
        "percentage_start": 50,
        "percentage_end": 70
      },

      {
        "question": "Question 4",
        "type": "Strongly disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": -15.6,
        "percentage_end": -15.6
      },
      {
        "question": "Question 4",
        "type": "Disagree",
        "value": 2,
        "percentage": 12.5,
        "percentage_start": -15.6,
        "percentage_end": -3.1
      },
      {
        "question": "Question 4",
        "type": "Neither agree nor disagree",
        "value": 1,
        "percentage": 6.3,
        "percentage_start": -3.1,
        "percentage_end": 3.1
      },
      {
        "question": "Question 4",
        "type": "Agree",
        "value": 7,
        "percentage": 43.8,
        "percentage_start": 3.1,
        "percentage_end": 46.9
      },
      {
        "question": "Question 4",
        "type": "Strongly agree",
        "value": 6,
        "percentage": 37.5,
        "percentage_start": 46.9,
        "percentage_end": 84.4
      },

      {
        "question": "Question 5",
        "type": "Strongly disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": -10.4,
        "percentage_end": -10.4
      },
      {
        "question": "Question 5",
        "type": "Disagree",
        "value": 1,
        "percentage": 4.2,
        "percentage_start": -10.4,
        "percentage_end": -6.3
      },
      {
        "question": "Question 5",
        "type": "Neither agree nor disagree",
        "value": 3,
        "percentage": 12.5,
        "percentage_start": -6.3,
        "percentage_end": 6.3
      },
      {
        "question": "Question 5",
        "type": "Agree",
        "value": 16,
        "percentage": 66.7,
        "percentage_start": 6.3,
        "percentage_end": 72.9
      },
      {
        "question": "Question 5",
        "type": "Strongly agree",
        "value": 4,
        "percentage": 16.7,
        "percentage_start": 72.9,
        "percentage_end": 89.6
      },

      {
        "question": "Question 6",
        "type": "Strongly disagree",
        "value": 1,
        "percentage": 6.3,
        "percentage_start": -18.8,
        "percentage_end": -12.5
      },
      {
        "question": "Question 6",
        "type": "Disagree",
        "value": 1,
        "percentage": 6.3,
        "percentage_start": -12.5,
        "percentage_end": -6.3
      },
      {
        "question": "Question 6",
        "type": "Neither agree nor disagree",
        "value": 2,
        "percentage": 12.5,
        "percentage_start": -6.3,
        "percentage_end": 6.3
      },
      {
        "question": "Question 6",
        "type": "Agree",
        "value": 9,
        "percentage": 56.3,
        "percentage_start": 6.3,
        "percentage_end": 62.5
      },
      {
        "question": "Question 6",
        "type": "Strongly agree",
        "value": 3,
        "percentage": 18.8,
        "percentage_start": 62.5,
        "percentage_end": 81.3
      },

      {
        "question": "Question 7",
        "type": "Strongly disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": -10,
        "percentage_end": -10
      },
      {
        "question": "Question 7",
        "type": "Disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": -10,
        "percentage_end": -10
      },
      {
        "question": "Question 7",
        "type": "Neither agree nor disagree",
        "value": 1,
        "percentage": 20,
        "percentage_start": -10,
        "percentage_end": 10
      },
      {
        "question": "Question 7",
        "type": "Agree",
        "value": 4,
        "percentage": 80,
        "percentage_start": 10,
        "percentage_end": 90
      },
      {
        "question": "Question 7",
        "type": "Strongly agree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 90,
        "percentage_end": 90
      },

      {
        "question": "Question 8",
        "type": "Strongly disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 8",
        "type": "Disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 8",
        "type": "Neither agree nor disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 8",
        "type": "Agree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 8",
        "type": "Strongly agree",
        "value": 2,
        "percentage": 100,
        "percentage_start": 0,
        "percentage_end": 100
      }
])

color_scale = alt.Scale(
    domain=[
        "Strongly disagree",
        "Disagree",
        "Neither agree nor disagree",
        "Agree",
        "Strongly agree"
    ],
    range=["#c30d24", "#f3a583", "#cccccc", "#94c6da", "#1770ab"]
)

y_axis = alt.Axis(
    title='Question',
    offset=5,
    ticks=False,
    minExtent=60,
    domain=False
)

base = alt.Chart(source).encode(
    x='percentage_start:Q',
    x2='percentage_end:Q')

bar = base.mark_bar().encode(
    y=alt.Y('question:N', axis=y_axis),
    color=alt.Color(
        'type:N',
        legend=alt.Legend( title='Response'),
        scale=color_scale,
    )
)

chart = bar

chart.save('Simple Diverging Stacked Bar Chart.html')

"""
그룹 막대 그래프 - 가로
"""
source = data.barley()

base = alt.Chart().encode(x='year:O')

bar = base.mark_bar().encode(
    y=alt.Y('mean(yield):Q', title='Mean Yield'),
    color='year:N',
)

error_bars = base.mark_errorbar(extent='ci').encode(
    y='yield:Q'
)

text = bar.mark_text(
    align='center',
    baseline='bottom', 
    dx=6
).encode(
    text='mean(yield):Q'
)

chart = alt.layer(bar, error_bars,text, data=source).facet(column='site:N')
chart.save('Simple Grouped Bar Chart.html')

"""
그룹 막대 그래프 - 세로 
"""
source = data.barley()

base = alt.Chart().encode(
    x = alt.X('sum(yield):Q', title = 'Sum Yield')
)

bar = base.mark_bar().encode(
    y=alt.Y('year:O', title='Year'),
    color='year:O'
)

text = bar.mark_text(
    align='left',
    baseline='middle', 
    dx=6
).encode(
    text='sum(yield):Q'
)


chart = alt.layer(bar, text, data=source).facet(row='site:N')
chart.save('Simple Grouped Bar2 Chart.html')

"""
겹쳐져있는 막대 그래프 
"""
source = data.iowa_electricity()


base = alt.Chart().encode(
  x = alt.X('year:O', title = 'Year')
)

bar = base.mark_bar(opacity=0.7).encode(
  y= alt.Y('net_generation:Q', stack=None, title ='Net_Generation'),
  color = "source"
)

chart = alt.layer(bar, data=source)
chart.save('Simple Layered Bar Chart.html')

"""
스택 막대 그래프 - 글자 쓰기(글자 색상 변경, 텍스트 소수점 제거 가능)
"""
source = data.barley()

base = alt.Chart().encode(x = alt.X('sum(yield)', title='Yield')) #정규화

bar = base.mark_bar(opacity=0.7).encode(
  y=alt.Y('variety', title='Variety'),
  color=alt.Color('site')
)

text = base.mark_text(dx=-15, dy=3, color='white').encode(
    x=alt.X('sum(yield):Q', stack='zero'),
    y=alt.Y('variety:N'),
    detail='site:N',
    text=alt.Text('sum(yield):Q', format='.1f')
)


chart = alt.layer(bar, text, data=source)
chart.save('Simple Stacked Bar Chart.html')


"""
스택 막대 그래프 정규화해서 그리기
"""
source = data.barley()

base = alt.Chart().encode(x = alt.X('sum(yield)', title='Yield', stack='normalize')) #정규화

bar = base.mark_bar(opacity=0.7).encode(
  y=alt.Y('variety', title='Variety'),
  color = 'site'
)


chart = alt.layer(bar, data=source)
chart.save('Simple Stacked Bar2 Chart.html')



"""
스택 막대 그래프 정렬해서 그리기
"""
source = data.barley()

base = alt.Chart().encode(x = alt.X('sum(yield)', title='Yield')) #정규화

bar = base.mark_bar(opacity=0.7).encode(
  y=alt.Y('variety', title='Variety', sort='-x'), #- 붙이면 내림차순, -없으면 오름차순
  color = 'site'
)

chart = alt.layer(bar, data=source)
chart.save('Simple Stacked Bar3 Chart.html')



"""
스택 막대 그래프 정렬해서 그리기2
"""
source = data.barley()

base = alt.Chart().encode(x = alt.X('sum(yield)', title='Yield')) #정규화

bar = base.mark_bar(opacity=0.7).encode(
  y=alt.Y('variety', title='Variety', sort='-x'), #- (그래프 전체)붙이면 내림차순, -없으면 오름차순
  color = 'site',
  order = alt.Order(
    'site',
    sort = 'descending' #어떤 지표를 먼저 쌓을지 순서 #ascending
  )
)

chart = alt.layer(bar, data=source)
chart.save('Simple Stacked Bar4 Chart.html')



"""
스택 막대 그래프 여러개 나눠서 그리기
"""
source = data.barley()

base = alt.Chart().encode(x = alt.X('sum(yield)', title='Yield')) #정규화

bar = base.mark_bar(opacity=0.7).encode(
  y=alt.Y('variety', title='Variety', sort='-x'), #- (그래프 전체)붙이면 내림차순, -없으면 오름차순
  color = 'site',
  order = alt.Order(
    'site',
    sort = 'descending' #어떤 지표를 먼저 쌓을지 순서 #ascending
  )
)

chart = alt.layer(bar, data=source).facet(column='year:N')
chart.save('Simple Stacked Bar5 Chart.html')

