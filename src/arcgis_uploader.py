from arcgis.gis import GIS
from config import ARCGIS_URL, ARCGIS_USERNAME, ARCGIS_PASSWORD, FEATURE_LAYER_ITEM_ID
import pandas as pd
from datetime import datetime


FIELD_MAP = {
    "Дата": "date_1",
    "Область": "Область",
    "Місто": "city",
    "Значення 1": "value_1",
    "Значення 2": "value_2",
    "Значення 3": "value_3",
    "Значення 4": "value_4",
    "Значення 5": "value_5",
    "Значення 6": "value_6",
    "Значення 7": "value_7",
    "Значення 8": "value_8",
    "Значення 9": "value_9",
    "Значення 10": "value_10",
    "long": "long",
    "lat": "lat",
}

def upload_to_arcgis(df: pd.DataFrame):
    gis = GIS(ARCGIS_URL, ARCGIS_USERNAME, ARCGIS_PASSWORD)
    item = gis.content.get(FEATURE_LAYER_ITEM_ID)
    layer = item.layers[0]

    df = df.copy()
    df.loc[:, "long"] = df["long"].astype(str).str.replace(",", ".").astype(float)
    df.loc[:, "lat"] = df["lat"].astype(str).str.replace(",", ".").astype(float)

    features = []
    for _, row in df.iterrows():
        attributes = {FIELD_MAP[k]: row[k] for k in FIELD_MAP if k in row}
        feature = {
            "geometry": {
                "x": row["long"],
                "y": row["lat"],
                "spatialReference": {"wkid": 4326}
            },
            "attributes": attributes
        }
        features.append(feature)

    if features:
        layer.edit_features(adds=features)
        print(f"Завантажено {len(features)} записів до ArcGIS.")
    else:
        print("Немає нових записів для завантаження.")
