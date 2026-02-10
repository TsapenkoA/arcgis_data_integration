import pandas as pd

VALUE_COLUMNS = [f"Значення {i}" for i in range(1, 11)]

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    result_rows = []

    for _, row in df.iterrows():
        max_value = int(max(row[col] for col in VALUE_COLUMNS))

        for i in range(max_value):
            new_row = {
                "Дата": row["Дата"],
                "Область": row["Область"],
                "Місто": row["Місто"],
                "long": row["long"],
                "lat": row["lat"],
            }

            for col in VALUE_COLUMNS:
                new_row[col] = 1 if row[col] > i else 0

            result_rows.append(new_row)

    return pd.DataFrame(result_rows)

