def get_recommendations(temperature, fan_hours, cooler_hours):
    recommendations = []
    if cooler_hours > 7:
        recommendations.append(
            "High cooler usage detected. Reducing usage by 2 hours/day can save energy."
        )
    if fan_hours > 14:
        recommendations.append(
            "Fan usage is high. Consider lower speed or switching off when away."
        )
    if temperature > 38:
        recommendations.append(
            "High temperature detected. Keep ventilation open during evenings."
        )
    if not recommendations:
        recommendations.append("Energy usage is optimal.")
    
    return recommendations

recommendations = get_recommendations(40, 16, 8)

for rec in recommendations:
    print(rec)