import geopandas as gpd

name = 'cb_2018_us_zcta510_500k'
# name = 'water_polygons'

# Load your geospatial data
gdf = gpd.read_file(f'./data/{name}.shp')  # Use f-string to replace the filename dynamically

# Convert to GeoParquet
gdf.to_parquet(f'./data/{name}.geoparquet', engine='pyarrow')
