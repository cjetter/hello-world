# Script to generate figures and widgets for plotting of temperature, humidity, pH, etc.

#import libraries
from bokeh.plotting import figure
from bokeh.models import NumeralTickFormatter, Range1d, DatetimeTickFormatter
from bokeh.models import ResetTool, PanTool, WheelZoomTool, BoxAnnotation
from math import radians

# function to create time-series plot for temperature, humidity, etc.
def make_plot(src,datatype):
    '''
    The make_plot function serves to plot data across (temp, humidity, pH, etc.)

    src = The source of data points to plot passed in as a ColumnDataSource bokeh.models object
    datatype = The designation of the type of data being plotted is used to define the figure title, title of the y-axis, and set formatting and range boundaries for the y axis. Designate by passing in one of the following ["Temp","Hum","pH"] as a string
    '''
    # set datatype specific values 
    # define figure title by data type
    ftdict = {'Temp':'Temperatura/Tiempo','Hum':'Humedad/Tiempo','pH':'pH/Tiempo'}
    # define y axis title and legend title by data type
    ytdict = {'Temp':'temperatura (C)','Hum':'humedad (%)','pH':'pH'}
    # define boundary range of y axis by data type
    bddict = {'Temp':(-5,25,(-5,50)),'Hum':(0,1,(-.2,1.2)),'pH':(3,10,(2.5,11))}
    # define y axis formatting style
    fmtdict = {'Temp':'0,0.00','Hum':'0.00%','pH':'0,0.0'}
    # set ranges for acceptable values of temp, hum, pH, etc.
    bxdict = {'Temp':(20,40),'Hum':(0,1,(-.2,1.2)),'pH':(4.5,6.5)}
    # define color type of plot line by data type
    cldict = {'Temp':'firebrick','Hum':'navy','pH':'DarkGoldenrod'}

    # create and stylize plot figure
    f = figure(x_axis_type='datetime',tools=[ResetTool(),PanTool(),WheelZoomTool(dimensions='width')])
    #f.title.text'=ftdict[datatype]
    f.title.text='Test'
    f.title.text_font_size='12pt'
    f.title.text_font_style='bold'
    f.xaxis.axis_label='tiempo'
    f.yaxis.axis_label=ytdict[datatype]
    f.width = 1100
    f.height = 375
    f.min_border_bottom=60
    f.y_range=Range1d(start=bddict[datatype][0],end=bddict[datatype][1],bounds=bddict[datatype][2])

    # create and stylize axes of plot
    f.xaxis.formatter=DatetimeTickFormatter(
        milliseconds=["%m/%d/%Y %H:%M:%S:%3N"],
        seconds=["%m/%d/%Y %H:%M:%S"],
        minsec=["%m/%d/%Y %H:%M:%S"],
        minutes=["%m/%d/%Y %H:%M:%S"],
        hourmin=["%m/%d/%Y %H:%M:%S"],
        hours=["%m/%d/%Y %H:%M"],
        days=["%m/%d/%Y"],
        months=["%b-%Y"],
        years=["%Y"],)
    f.xaxis.major_label_orientation = radians(45)
    f.yaxis.formatter = NumeralTickFormatter(format=fmtdict[datatype])

    #create box annotation to highlight acceptable ranges for temp, hum, pH, etc.
    minval = bxdict[datatype][0]
    maxval = bxdict[datatype][1]
    low_box = BoxAnnotation(top=minval, fill_alpha=0.1, fill_color='light red')
    mid_box = BoxAnnotation(bottom=minval, top=maxval, fill_alpha=0.1, fill_color='green')
    high_box = BoxAnnotation(bottom=maxval, fill_alpha=0.1, fill_color='light red')
    f.add_layout(low_box)
    f.add_layout(mid_box)
    f.add_layout(high_box)

    #plot line of data
    f.line(source=src,x='x',y='y',line_color=cldict[datatype],line_width=2,legend=ytdict[datatype])

    return f