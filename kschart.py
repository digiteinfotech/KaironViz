import json
import pandas as pd
from jsmin import jsmin
import uuid

from IPython.display import HTML, display


def sanky_chart(dataframe, headers, height=450, legend ="chart example", legend_style = 'text-align: center; font: 28px Arial', text_scale = 1, text_color = '#333', text_font='Arial', draw_labels = True, draw_column_labels = True, trancation = 20,  node_width = 20, vertical_spacing = 20, show_toolbar = True,  from_prefix = '', to_prefix = '', from_suffix = '', to_suffix = ''):
    jsonStr = dataframe.to_json(orient='records')
    headers = json.dumps(headers)
    text = open('kschart/kschart_template.html', 'r').read()
    drillChart_js = open('kschart/kschart.js', 'r').read()
    drillChart_js = jsmin(drillChart_js)
    unique_id_str = str(uuid.uuid4())
    text = text.replace('@data_label', unique_id_str)
    text = text.replace('@kschart_js_inject', drillChart_js)
    chart_container_height = height + 80
    if show_toolbar:
        chart_container_height = chart_container_height + 150
    text = text.replace('@chart_container_height', str(chart_container_height))
    text = text.replace('@chart_height', str(height))
    text = text.replace('@chart_legend_style', legend_style)
    text = text.replace('@chart_legend_name', legend)
    text = text.replace('@chart_text_scale', str(text_scale))
    text = text.replace('@chart_text_color', text_color)
    text = text.replace('@chart_text_font', text_font)
    text = text.replace('@chart_draw_labels', str(draw_labels).lower())
    text = text.replace('@chart_draw_column_labels', str(draw_column_labels).lower())
    text = text.replace('@chart_trancation', str(trancation))
    text = text.replace('@chart_node_width', str(node_width))
    text = text.replace('@chart_vertical_spacing', str(vertical_spacing))
    text = text.replace('@chart_show_toolbar', str(show_toolbar).lower())
    text = text.replace('@chart_from_prefix', from_prefix)
    text = text.replace('@chart_to_prefix', to_prefix)
    text = text.replace('@chart_from_suffix', from_suffix)
    text = text.replace('@chart_to_suffix', to_suffix)

    text = text.replace('@chart_data', jsonStr)
    text = text.replace('@chart_headers', headers)

    #complete this
    display(HTML('<div>'+text+'</div>'))
    return text



def sanky_chart2(dataframe, src_name, dest_name, src_level, dest_level, height=450, legend ="chart example", legend_style = 'text-align: center; font: 28px Arial', text_scale = 1, text_color = '#333', text_font='Arial', draw_labels = True, draw_column_labels = True, trancation = 20,  node_width = 20, vertical_spacing = 20, show_toolbar = True, from_prefix = '', to_prefix = '', from_suffix = '', to_suffix = ''):

    jsonStr = dataframe.to_json(orient='records')
    text = open('kschart/kschart_template2.html', 'r').read()
    drillChart_js = open('kschart/kschart.js', 'r').read()
    drillChart_js = jsmin(drillChart_js)
    unique_id_str = str(uuid.uuid4())
    text = text.replace('@data_label', unique_id_str)
    text = text.replace('@kschart_js_inject', drillChart_js)
    chart_container_height = height + 80
    if show_toolbar:
        chart_container_height = chart_container_height + 150
    text = text.replace('@chart_container_height', str(chart_container_height))
    text = text.replace('@chart_height', str(height))
    text = text.replace('@chart_legend_style', legend_style)
    text = text.replace('@chart_legend_name', legend)
    text = text.replace('@chart_text_scale', str(text_scale))
    text = text.replace('@chart_text_color', text_color)
    text = text.replace('@chart_text_font', text_font)
    text = text.replace('@chart_draw_labels', str(draw_labels).lower())
    text = text.replace('@chart_draw_column_labels', str(draw_column_labels).lower())
    text = text.replace('@chart_trancation', str(trancation))
    text = text.replace('@chart_node_width', str(node_width))
    text = text.replace('@chart_vertical_spacing', str(vertical_spacing))
    text = text.replace('@chart_show_toolbar', str(show_toolbar).lower())
    text = text.replace('@chart_from_prefix', from_prefix)
    text = text.replace('@chart_to_prefix', to_prefix)
    text = text.replace('@chart_from_suffix', from_suffix)
    text = text.replace('@chart_to_suffix', to_suffix)



    text = text.replace('@chart_src_name', src_name)
    text = text.replace('@chart_dest_name', dest_name)
    text = text.replace('@chart_src_level', src_level)
    text = text.replace('@chart_dest_level', dest_level)
    text = text.replace('@chart_data', jsonStr)

    #complete this
    display(HTML('<div>'+text+'</div>'))
    return text




