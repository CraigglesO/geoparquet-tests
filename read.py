import geopandas as gpd
# import geoparquet as gpq

# name = 'cb_2018_us_zcta510_500k'
name = 'water_polygons'

# Read GeoParquet data
gdf = gpd.read_parquet(f'./data/{name}.geoparquet')

# print(gdf)
