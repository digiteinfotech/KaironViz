# Kairon Visualization

### version 0.0.6

Different plots for data visualization in notebook and html export.

Look at `example.ipynb` notebook for basic demo uses.

## Installing

> pip install kaironviz

## Available charts

-   sanky_chart
-   sanky_chart2
-   drill_chart
-   word_cloud
-   tree_diagram

## Sanky Chart

### `sanky_chart`

This function generates a Sanky chart to visualize the relationships between columns in a DataFrame.

**Parameters:**

-   `dataframe`: pandas DataFrame containing the data to be visualized.
-   `headers`: List of column headers in the DataFrame.
-   `height`: Height of the chart (default is 450).
-   `legend`: Title of the chart legend (default is "chart example").
-   `legend_style`: CSS style for the legend (default is 'text-align: center; font: 28px Arial').
-   `text_scale`: Scaling factor for text size (default is 1).
-   `text_color`: Color of the text (default is '#333').
-   `text_font`: Font for the text (default is 'Arial').
-   `draw_labels`: Boolean indicating whether to draw labels (default is True).
-   `draw_column_labels`: Boolean indicating whether to draw column labels (default is True).
-   `trancation`: Truncation value for labels (default is 20).
-   `node_width`: Width of nodes in the chart (default is 20).
-   `vertical_spacing`: Vertical spacing between nodes (default is 20).
-   `show_toolbar`: Boolean indicating whether to display the toolbar (default is True).
-   `from_prefix`, `to_prefix`, `from_suffix`, `to_suffix`: Prefixes and suffixes for from/to labels (default is empty strings).
-   `label_distance`: Distance of labels from nodes (default is 10).
-   `use_gradient`: Boolean indicating whether to use gradient colors (default is True).
-   `client_height`: Client height of the chart (default is 0).
-   `compact`: Removes unnecessary data (default is True).

### `sanky_chart2`

This function generates a Sanky chart to visualize relationships between source and destination column entities, where the level is the column that the entities belong to in the Sanky chart.

**Parameters:**

-   `dataframe`: pandas DataFrame containing the data to be visualized.
-   `src_name`, `dest_name`: Names of the source and destination columns.
-   `src_level`, `dest_level`: Levels(integer indices) of the source and destination columns.
-   `height`: Height of the chart (default is 450).
-   `legend`: Title of the chart legend (default is "chart example").
-   `legend_style`: CSS style for the legend (default is 'text-align: center; font: 28px Arial').
-   `text_scale`: Scaling factor for text size (default is 1).
-   `text_color`: Color of the text (default is '#333').
-   `text_font`: Font for the text (default is 'Arial').
-   `draw_labels`: Boolean indicating whether to draw labels (default is True).
-   `draw_column_labels`: Boolean indicating whether to draw column labels (default is True).
-   `trancation`: Truncation value for labels (default is 20).
-   `node_width`: Width of nodes in the chart (default is 20).
-   `vertical_spacing`: Vertical spacing between nodes (default is 20).
-   `show_toolbar`: Boolean indicating whether to display the toolbar (default is True).
-   `from_prefix`, `to_prefix`, `from_suffix`, `to_suffix`: Prefixes and suffixes for from/to labels (default is empty strings).
-   `label_distance`: Distance of labels from nodes (default is 10).
-   `color_mode`: Color mode for the chart (default is 0).
-   `use_gradient`: Boolean indicating whether to use gradient colors (default is True).
-   `client_height`: Client height of the chart (default is 0).
-   `restructure_levels`: Boolean indicating if you need to rearrange columns for larger number of levels (default is False)

## Drill Chart

### `drill_chart`

This function creates an n-level drill-down chart.

**Parameters:**

-   `data`: Data for the drill chart.
-   `start_label`: Label for the starting point of the drill chart.
-   `y_label`: Label for the y-axis (default is 'values').
-   `legend`: Title of the chart legend (default is 'Drill Chart').
-   `legend_color`: Color of the legend text (default is 'black').
-   `legend_font`: Font style for the legend (default is 'Bold 20px Arial').
-   `legend_pos`: Position of the legend (default is 'bottom').
-   `legend_align`: Alignment of the legend (default is 'center').
-   `nav_color`: Color of the navigation bar (default is '#046688').
-   `nav_font`: Font style for the navigation bar (default is '16px Arial').
-   `nav_justify`: Justification for the navigation bar (default is 'right').
-   `nav_padding`: Padding for the navigation bar (default is '10px').
-   `label_scale`: Scaling factor for labels (default is 1.2).
-   `label_color`: Color of labels (default is 'black').
-   `resolution`: Resolution of the chart (default is 1.2).
-   `background_color`: Background color of the chart (default is 'transparent').
-   `height`: Height of the chart (default is 480).
-   `max_column_width`: Maximum width for columns in the chart (default is 100).

## Word Cloud

### `word_cloud`

The `word_cloud` function is used to create a word cloud chart.

### Parameters:

-   `data`: This can be a string, a list, or a DataFrame. If it's a string or a list, the function will count the frequency of each word and create a DataFrame. If it's a DataFrame, it will be copied as is.
-   `height` (default = 480): The height of the word cloud chart.
-   `width` (default = 640): The width of the word cloud chart.
-   `max_item` (default = 400): The maximum number of words to display in the word cloud.
-   `max_font_size` (default = 60): The maximum font size of the words in the word cloud.
-   `min_font_size` (default = 12): The minimum font size of the words in the word cloud.
-   `color_mode` (default = True): If set to True, the word cloud will be colored. If False, it will be in grayscale.
-   `font` (default = 'Helvatica'): The font of the words in the word cloud.

## Diagram

### tree_diagram

The `tree_diagram` function is used to create a tree diagram chart.

### Parameters:

-   `data_dict`: A dictionary representing the tree structure.
-   `height` (default = 450): The height of the tree diagram chart.
-   `text_color` (default = '#333'): The color of the text in the tree diagram.
-   `line_color` (default = '#333'): The color of the lines in the tree diagram.
-   `box_background` (default = 'transparent'): The background color of the boxes in the tree diagram.
-   `border_radius` (default = 0.6): The border radius of the boxes in the tree diagram.
-   `border_color` (default = '#333'): The color of the borders of the boxes in the tree diagram.
-   `font_size` (default = 14): The font size of the text in the tree diagram.
-   `font_family` (default = 'Arial'): The font of the text in the tree diagram.
-   `orientation` (default = 'vertical'): The orientation of the tree diagram. It can be 'vertical' or 'horizontal'.
