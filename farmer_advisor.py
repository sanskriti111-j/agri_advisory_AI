def farmer_advisor(farm_data):
    soil_type = farm_data.get("Soil_Type", "").lower()
    water_availability = farm_data.get("Water_Availability", "").lower()

    if soil_type == "loamy" and "high" in water_availability:
        recommendation = "Based on your loamy soil and good water availability, rice or sugarcane could be good choices."
    elif soil_type == "sandy":
        recommendation = "For sandy soil, consider millets or groundnut as water-efficient options."
    else:
        recommendation = "Please consult with a local agri-expert for detailed crop matching."

    return f"👨‍🌾 Farmer Advisory: {recommendation}"
