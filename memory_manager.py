def save_to_memory(farm_id, farm_data, advisory_summary):
    try:
        with open("advisory_log.txt", "a") as file:
            file.write(f"\n\nFarm ID: {farm_id}\n")
            file.write(str(farm_data))
            file.write("\nAdvisory Summary:\n")
            file.write(advisory_summary)
            file.write("\n" + "="*50)
    except Exception as e:
        print(f"❌ Error saving to memory: {e}")
