def get_recommendations(temperature, fan_hours, cooler_hours):
    recommendations = []

    if cooler_hours > 7:
        recommendations.append(
            "Reduce cooler usage by 2 hours/day to save energy."
        )

    if fan_hours > 14:
        recommendations.append(
            "Consider reducing fan speed during cooler hours."
        )

    if temperature > 38:
        recommendations.append(
            "Improve ventilation by opening windows in evening."
        )

    if not recommendations:
        recommendations.append("Energy usage is already optimized.")

    return recommendations