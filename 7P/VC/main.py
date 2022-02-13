import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import plotly as plt
import plotly.express as px
import numpy as np

brazil = gpd.read_file("Focos_2021-01-01_2021-11-28.geojson")
brazil['datahora'] = brazil['datahora'].apply(lambda x: x[:7])
brazil.loc[brazil['riscofogo'] == -999, 'riscofogo'] = np.nan
brazil.loc[brazil['riscofogo'] == 0, 'riscofogo'] = np.nan
brazil = brazil.dropna()
brazil = brazil.reset_index(drop=True)
brazil = brazil.sort_values('datahora')

fig = px.scatter_mapbox(brazil, 
    lat='latitude', 
    lon='longitude', 
    animation_frame='datahora', 
    color='precipitacao', 
    range_color=[0,20], 
    size='riscofogo', 
    color_continuous_scale=px.colors.sequential.Inferno[::-1],
    hover_data={
        "datahora": False, 
        "riscofogo": True, 
        "precipitacao": True, 
        "municipio": True, 
        "estado": True, 
        "frp": True, 
        "latitude": True, 
        "longitude": True
    },
    hover_name="bioma"
)
fig.update_layout(mapbox_style="open-street-map")
fig.show()
