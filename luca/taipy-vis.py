from taipy.gui import Gui
import pandas as pd 
from taipy.gui import Html




# *** PAGE 1 ***

g1_data_p1 = pd.read_csv('../cleaned_data/countries_ev_data(IEA).csv')
g1_data_p1.drop('Unnamed: 0', inplace=True, axis=1) 

g1_country_lov_p1 = sorted(g1_data_p1['region'].unique().tolist())
g1_country_p1 = g1_country_lov_p1[0]

g1_data_var_lov_p1 = ['Sales', 'Shares']
g1_data_var_p1 = g1_data_var_lov_p1[0]

g1_df_p1 = g1_data_p1[g1_data_p1['region'] == g1_country_p1]

g1_y1_p1 = 'ev_' + g1_data_var_p1.lower()
g1_y2_p1 = 'fossil_' + g1_data_var_p1.lower()

g1_fuel_lov_p1 = ['All','EV' ,'ICE']
g1_fuel_p1 = g1_fuel_lov_p1[0]


# *** PAGE 1: Graph 2 data ***
g2_data_p1 = pd.read_csv('../cleaned_data/australia_ev_comparison(IEA).csv')
g2_data_p1.drop('Unnamed: 0', inplace=True, axis=1) 
g2_comp_lov_p1 = ['Average', 'Top Country']
g2_data_var_lov_p1 = ['Sales', 'Shares']

g2_df_p1 = g2_data_p1

g2_comp_p1 = g2_comp_lov_p1[0]
g2_data_var_p1 = g2_data_var_lov_p1[0]

def change_g2_comp_p1(value, data_var):
    if value == 'Average':
        return value +' '+ data_var
    else:
        if data_var == 'sales':
            return 'China sales'
        else:
            return 'Norway shares'

g2_y1_p1 = 'Australia '+ g2_data_var_p1.lower()
g2_y2_p1 = change_g2_comp_p1(g2_comp_p1, g2_data_var_p1.lower()) 



page1 = """

## ICE Sales vs. EV Sales (Taipy)

<|layout|columns= 1 5|

<| 
Country:\n
<|{g1_country_p1}|selector|lov={g1_country_lov_p1}|dropdown|> 
|>
<| 
Data:\n
<|{g1_data_var_p1}|selector|lov={g1_data_var_lov_p1}|dropdown|>
|>
<| 
Fuel Type:\n
<|{g1_fuel_p1}|selector|lov={g1_fuel_lov_p1}|dropdown|>
|>
|>

<|{g1_df_p1}|chart|mode=lines+markers|x=year|y[1]={g1_y1_p1}|y[2]={g1_y2_p1}|line[1]=dash|color[2]=red|rebuild|> 

#### Table Data:
<|{g1_df_p1}|table|>

<br/>

Sample text\n
Australia adoption rate is lower than the average.........\n
Sample text\n
Sample text\n
Sample text.

## Australia Data:
<|layout|columns= 1 5|
<| 
comparison:\n
<|{g2_comp_p1}|selector|lov={g2_comp_lov_p1}|dropdown|> 
|>
<| 
Data:\n
<|{g2_data_var_p1}|selector|lov={g2_data_var_lov_p1}|dropdown|>
|>
|>
<|{g2_df_p1}|chart|mode=lines+markers|x=year|y[1]={g2_y1_p1}|y[2]={g2_y2_p1}|line[1]=dash|color[2]=red|rebuild|> 


<br/>

Sample text\n
Australia adoption rate is lower than the average but is catching up...........etc.......\n
Sample text\n
Sample text\n
Sample text.
"""

# *** PAGE 2 ***

data_p2 = pd.read_csv('../cleaned_data/types_sales(IEA).csv')
data_p2.drop('Unnamed: 0', inplace=True, axis=1) 

type_lov_p2 = data_p2['powertrain'].unique().tolist()
type_lov_p2.append('all')
type_lov_p2 = sorted(type_lov_p2)
type_p2 = type_lov_p2[0]


df_p2 = data_p2[data_p2['powertrain'] == type_p2]


page2 = """

## ICE Type Sales (Taipy)


<|{type_p2}|selector|lov={type_lov_p2}|dropdown|> 

<|{df_p2}|chart|mode=lines+markers|x=year|y[1]=aus_sales|y[2]=avg_sales|line[1]=dash|color[2]=red|rebuild|> 

table data:
<|{df_p2}|table|>
"""



# *** ON CHANGE ***

def on_change(state, var_name, var_value):
    # page 1
    if var_name == 'g1_country_p1':
        state.g1_df_p1 = g1_data_p1[g1_data_p1['region'] == var_value]

    elif var_name == 'g1_data_var_p1':
        ev = 'ev_' + var_value.lower()
        fossil = 'fossil_' + var_value.lower()
        state.g1_y1_p1 = ev
        state.g1_y2_p1 = fossil
        state.g1_df_p1 = g1_data_p1[g1_data_p1['region'] == state.g1_country_p1]
    
    elif var_name == 'g2_comp_p1':
        aus = 'Australia '+ state.g2_data_var_p1.lower()
        comp = change_g2_comp_p1(var_value, state.g2_data_var_p1.lower())
        state.g2_y1_p1 = aus
        state.g2_y2_p1 = comp
        state.g2_df_p1 = g2_data_p1

    elif var_name == 'g2_data_var_p1':
        aus = 'Australia '+ var_value.lower()
        comp = change_g2_comp_p1(state.g2_comp_p1, var_value.lower())
        state.g2_y1_p1 = aus
        state.g2_y2_p1 = comp
        state.g2_df_p1 = g2_data_p1    


    # page 2
    elif var_name == 'type_p2':
        if var_value == 'all':
            state.df_p2 = data_p2
        else:
            state.df_p2 = data_p2[data_p2['powertrain'] == var_value]
    
    #else:
        #print(var_name,var_value)


#Gui(page1).run()


html_page = Html("""
<h1>Hello World</h1>


""")

pages = {
    "/": '<|navbar|lov={[("/EV_vs_ICE", "EV vs. ICE"), ("/EV_type_sales", "EV Type Sales"), ("/html", "HTML page") ]}|>',
     "EV_vs_ICE": page1,
     "EV_type_sales": page2,
     "html": html_page
   }
Gui(pages=pages).run()