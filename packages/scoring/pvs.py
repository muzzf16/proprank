def calculate_pvs(technical, local, gbp, geo, content, competitor):
    return round(
        technical * 0.20 +
        local * 0.20 +
        gbp * 0.20 +
        geo * 0.15 +
        content * 0.15 +
        competitor * 0.10,
        2
    )
