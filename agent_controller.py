from controller.data_loader import load_farm_data, load_market_data
from controller.farmer_advisor import farmer_advisor
from controller.market_researcher import market_researcher
from controller.memory_manager import save_to_memory

def run_advisory(farm_id):
    farm_data = load_farm_data(farm_id)

    if farm_data is None:
        return f"❌ Farm ID '{farm_id}' not found in the dataset."

    market_data = load_market_data()
    if market_data is None or market_data.empty:
        return "❌ Market data not available."

    # Run advisor agents
    farmer_recommendation = farmer_advisor(farm_data)
    market_recommendation = market_researcher(market_data)

    crop_last_season = farm_data.get('Crop_Grown_Last_Season', 'a suitable crop')
    
    advisory_summary = (
        f"{farmer_recommendation}\n\n"
        f"{market_recommendation}\n\n"
        f"✅ Final Recommendation: Based on your farm condition and market trends, "
        f"consider cultivating a suitable crop. Last season you grew: {crop_last_season}."
    )

    save_to_memory(farm_id, farm_data, advisory_summary)

    return advisory_summary
