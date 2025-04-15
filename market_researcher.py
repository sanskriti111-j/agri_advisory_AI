def market_researcher(market_data):
    if market_data.empty:
        return "⚠️ Market data is empty."

    try:
        avg_demand_index = market_data["Demand_Index"].mean()
        avg_price = market_data["Market_Price_per_ton"].mean()
        avg_competitor_price = market_data["Competitor_Price_per_ton"].mean()

        recommendation = (
            f"📊 Market Insights:\n"
            f"- Average Demand Index: {avg_demand_index:.2f}\n"
            f"- Average Market Price per Ton: ₹{avg_price:.2f}\n"
            f"- Average Competitor Price per Ton: ₹{avg_competitor_price:.2f}\n"
        )

        if avg_demand_index > 100:
            recommendation += "🔼 Demand is relatively high. Consider increasing production."
        else:
            recommendation += "🔽 Demand is moderate. Monitor the market before scaling up."

        return recommendation

    except KeyError as e:
        return f"❌ Column not found in market data: {e}"
