import pandas as pd

def load_farm_data(farm_id):
    path = r"C:\Users\utkar\OneDrive\sanskriti_22123038 tut3\agriculture_ai\data\farmer_advisor_dataset.csv"
    try:
        df = pd.read_csv(path)
        df['Farm_ID'] = df['Farm_ID'].astype(str).str.strip()
        farm_id = str(farm_id).strip()

        filtered_df = df[df["Farm_ID"] == farm_id]

        if filtered_df.empty:
            print(f"❌ Farm_ID '{farm_id}' not found in dataset.")
            return None

        return filtered_df.iloc[0]
    except Exception as e:
        print(f"❌ Error loading farm data: {e}")
        return None

def load_market_data():
    path = r"C:\Users\utkar\OneDrive\sanskriti_22123038 tut3\agriculture_ai\data\market_researcher_dataset.csv"
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"❌ Error loading market data: {e}")
        return None
