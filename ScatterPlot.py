import altair as alt
from vega_datasets import data
import numpy as np
import pandas as pd

source = data.cars()

#산점도 - mark_circle 함수 사용 + bin 적용
base = alt.Chart()

plot = base.mark_circle().encode(
    x=alt.X('Horsepower:Q', bin = True),
    y=alt.Y('Miles_per_Gallon:Q', bin=True),
    size='Acceleration'
)

chart = alt.layer(plot, data = source)
chart.save('Simple ScatterPlot.html')



#산점도 - multi-features
base = alt.Chart()

plot = base.mark_circle(opacity = 0.7).encode(
    x=alt.X('Horsepower:Q', scale=alt.Scale(zero=False) , title='Horsepower'),
    y=alt.Y('Miles_per_Gallon:Q',scale=alt.Scale(zero=False, padding=1), title='Miles_per_Gallon'),
    color='Origin',
    size='Acceleration'
)

chart = alt.layer(plot, data = source)
chart.save('Simple ScatterPlot6.html')


#산점도 - 회귀선 추가
base = alt.Chart()
degree_list = [1,3,5]

plot = base.mark_circle(opacity = 0.7).encode(
    x=alt.X('Horsepower:Q', scale=alt.Scale(zero=False) , title='Horsepower'),
    y=alt.Y('Miles_per_Gallon:Q',scale=alt.Scale(zero=False, padding=1), title='Miles_per_Gallon')
)

polynomial_fit = [
    plot.transform_regression(
        "Horsepower", "Miles_per_Gallon", method="poly", order=order, as_=["Horsepower", str(order)]
    )
    .mark_line()
    .transform_fold([str(order)], as_=["degree", "Miles_per_Gallon"])
    .encode(alt.Color("degree:N"))
    for order in degree_list
]


chart = alt.layer(plot, *polynomial_fit, data = source)
chart.save('Simple ScatterPlot7.html')




#산점도 - mark.point 사용 - 마커 사이즈 변경
base = alt.Chart()

plot = base.mark_point().encode(
    x=alt.X('Horsepower:Q', scale=alt.Scale(zero=False) , title='Horsepower'),
    y=alt.Y('Miles_per_Gallon:Q',scale=alt.Scale(zero=False, padding=1), title='Miles_per_Gallon'),
    size='Acceleration'
)

chart = alt.layer(plot, data = source)
chart.save('Simple ScatterPlot2.html')


#산점도 - brush 사용
base = alt.Chart()
brush = alt.selection(type='interval')

plot  = base.mark_point().encode(
    x=alt.X('Horsepower:Q', scale=alt.Scale(zero=False) , title='Horsepower'),
    y=alt.Y('Miles_per_Gallon:Q',scale=alt.Scale(zero=False, padding=1), title='Miles_per_Gallon'),
    size= 'Acceleration',
    color=alt.condition(brush, 'Origin', alt.value('grey'))
).add_selection(brush)

chart = alt.layer(plot, data = source)
chart.save('Simple ScatterPlot3.html')

#산점도 - Data table 표기 사용
base = alt.Chart()
brush = alt.selection(type='interval')

plot  = base.mark_point().encode(
    x=alt.X('Horsepower:Q', scale=alt.Scale(zero=False) , title='Horsepower'),
    y=alt.Y('Miles_per_Gallon:Q',scale=alt.Scale(zero=False, padding=1), title='Miles_per_Gallon'),
    size= 'Acceleration',
    color=alt.condition(brush, 'Origin', alt.value('grey'))
).add_selection(brush)

ranked_text = alt.Chart(source).mark_text().encode(y=alt.Y('row_number:O',axis=None)
).transform_window(row_number='row_number()').transform_filter(brush
).transform_window(rank='rank(row_number)'
).transform_filter(alt.datum.rank<20
)

horsepower = ranked_text.encode(text='Horsepower:N').properties(title='Horsepower')
mpg = ranked_text.encode(text='Miles_per_Gallon:N').properties(title='MPG')
origin = ranked_text.encode(text='Origin:N').properties(title='Origin')
text = alt.hconcat(horsepower, mpg, origin) 

chart = alt.hconcat(alt.layer(plot, data = source), text).resolve_legend(color="independent")

chart.save('Simple ScatterPlot4.html')

#산점도 - Dot Dash 추가 
brush = alt.selection(type='interval')
base = alt.Chart(source).add_selection(brush)

plot  = base.mark_point().encode(
    x=alt.X('Horsepower:Q', scale=alt.Scale(zero=False) , title=' '),
    y=alt.Y('Miles_per_Gallon:Q',scale=alt.Scale(zero=False, padding=1), title=''),
    size= 'Acceleration',
    color=alt.condition(brush, 'Origin', alt.value('grey'))
).add_selection(brush)

tick_axis = alt.Axis(labels=False, domain=False, ticks=False)

x_ticks = base.mark_tick().encode(
    alt.X('Miles_per_Gallon', axis=tick_axis),
    alt.Y('Origin', title='', axis=tick_axis),
    color=alt.condition(brush, 'Origin', alt.value('lightgrey'))
)

y_ticks = base.mark_tick().encode(
    alt.X('Origin', title='', axis=tick_axis),
    alt.Y('Horsepower', axis=tick_axis),
    color=alt.condition(brush, 'Origin', alt.value('lightgrey'))
)

chart = y_ticks | (plot & x_ticks)
chart.save('Simple ScatterPlot5.html')
