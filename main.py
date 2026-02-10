from src.google_loader import load_google_sheet
from src.data_transformer import transform_data
from src.arcgis_uploader import upload_to_arcgis

def main():
    df_raw = load_google_sheet()
    df_raw.to_csv("data/raw_data.csv", index=False)
    print(f"Сирі дані: {len(df_raw)} рядків")

    df_prepared = transform_data(df_raw)
    df_prepared.to_csv("data/prepared_data.csv", index=False)
    print(f"Підготовлені дані: {len(df_prepared)} рядків")

    upload_to_arcgis(df_prepared)

if __name__ == "__main__":
    main()
