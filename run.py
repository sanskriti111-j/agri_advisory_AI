from controller.agent_controller import run_advisory

def main():
    farm_id = input("Enter Farm ID (e.g. F001): ").strip()

    if not farm_id:
        print("❌ Farm ID cannot be empty.")
        return

    try:
        result = run_advisory(farm_id)

        if result is None:
            print("\n⚠️ No advisory could be generated. Please check the Farm ID.")
        else:
            print("\n✅ Advisory Summary:\n")
            print(result)
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")

if __name__ == "__main__":
    main()
