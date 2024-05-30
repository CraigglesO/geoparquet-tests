# Experiments with geoparquet in Python

## Install

```shell
pip install geopandas pyarrow fsspec s3fs
```

I'm not even sure you need all these things, I used chatGPT to figure out how to use these tools.

Don't be fooled by the `geoparquet` library. It's not official and actually fails to load the data.

## The Data

### Ocean data to test on

<https://osmdata.openstreetmap.de/data/water-polygons.html>

<https://osmdata.openstreetmap.de/download/water-polygons-split-4326.zip>

### US Census data to test on

<https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_zcta510_500k.zip>

## Benchmarks

All benchmarks and work were done on an M3 Macbook Pro with 18 GB of Ram and 12 cores.

### Zip Code Boundaries

Total Size Shapefile: 87M
Total Size Parquet: 97M

```shell
 time python3 create.py
python3 create.py  4.82s user 2.78s system 157% cpu 4.836 total

 time python3 read.py
      ZCTA5CE10      AFFGEOID10 GEOID10    ALAND10  AWATER10                                           geometry
0         36083  8600000US36083   36083  659750662   5522919  MULTIPOLYGON (((-85.63225 32.28098, -85.62439 ...
1         35441  8600000US35441   35441  172850429   8749105  MULTIPOLYGON (((-87.83287 32.84437, -87.83184 ...
2         35051  8600000US35051   35051  280236456   5427285  POLYGON ((-86.74384 33.25002, -86.73802 33.251...
3         35121  8600000US35121   35121  372736030   5349303  POLYGON ((-86.58527 33.94743, -86.58033 33.948...
4         35058  8600000US35058   35058  178039922   3109259  MULTIPOLYGON (((-86.87884 34.21196, -86.87649 ...
...         ...             ...     ...        ...       ...                                                ...
33139     10983  8600000US10983   10983    5267037     16676  POLYGON ((-73.96564 41.02787, -73.96612 41.029...
33140     50460  8600000US50460   50460   93166133         0  POLYGON ((-92.80629 43.23026, -92.80354 43.232...
33141     40870  8600000US40870   40870   18226594    201441  POLYGON ((-83.19264 36.91650, -83.19086 36.916...
33142     40914  8600000US40914   40914   32269366    419039  POLYGON ((-83.62748 37.07419, -83.62455 37.073...
33143     52750  8600000US52750   52750   77963307    472441  POLYGON ((-90.44672 41.89151, -90.44177 41.891...

[33144 rows x 6 columns]
python3 read.py  0.73s user 2.70s system 657% cpu 0.522 total
```

### Water Polygons

Total Size Shapefile: 1.1G
Total Size Parquet: 1.0G

```shell
# water_polygons
 time python3 create.py
python3 create.py  51.69s user 4.41s system 103% cpu 54.346 total

 time python3 read.py
         x   y                                           geometry
0        1  41  POLYGON ((2.00067 40.99950, 0.99933 40.99950, ...
1      -11 -72  POLYGON ((-10.91746 -70.99950, -10.92245 -71.0...
2      -11 -72  POLYGON ((-10.75741 -70.99950, -10.73509 -71.0...
3      148 -11  POLYGON ((149.00051 -11.00050, 147.99949 -11.0...
4      -27 -58  POLYGON ((-25.99907 -56.99950, -25.99907 -58.0...
...    ...  ..                                                ...
53347  175  89  POLYGON ((176.05730 90.00000, 176.05730 88.999...
53348  176  89  POLYGON ((177.05730 90.00000, 177.05730 88.999...
53349  177  89  POLYGON ((178.05730 90.00000, 178.05730 88.999...
53350  178  89  POLYGON ((179.05730 90.00000, 179.05730 88.999...
53351  179  89  POLYGON ((180.00000 90.00000, 180.00000 88.999...

[53352 rows x 3 columns]
python3 read.py  2.36s user 2.53s system 141% cpu 3.458 total
```
