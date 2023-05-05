#%%
import os
import geopandas

geojson_in = os.path.join("..", "layers", "mental_health.geojson")
data = geopandas.read_file(geojson_in)
outdir = os.path.dirname(geojson_in)

col = "AUDIENCE"
val = "Children and Youth"
# %%

out = data[getattr(data, col)==val]
out.to_file(os.path.join(outdir, "child_youth_mental_health.geojson"), driver="GeoJSON")
