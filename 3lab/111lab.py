from math import radians, sin, cos, sqrt, atan2


def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371.0


    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)


    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad


    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance



vgups = (43.117778, 131.893056)  # ВГУЭС (переведенные координаты)
tgmu = (43.1155364, 131.8855348)  # ТГМУ
dvfu = (43.0237000, 131.8889000)  # ДВФУ


distance_vgups_tgmu = calculate_distance(vgups[0], vgups[1], tgmu[0], tgmu[1])
distance_vgups_dvfu = calculate_distance(vgups[0], vgups[1], dvfu[0], dvfu[1])



print("=" * 60)
print("РАССТОЯНИЯ МЕЖДУ УНИВЕРСИТЕТАМИ ВЛАДИВОСТОКА")
print("=" * 60)

print("ОСНОВНЫЕ МАРШРУТЫ:")
print(f"ВГУЭС → ТГМУ")
print(f"  Расстояние: {distance_vgups_tgmu:.3f} км ({distance_vgups_tgmu * 1000:.0f} м)")
print("-" * 40)

print(f"ВГУЭС → ДВФУ")
print(f"  Расстояние: {distance_vgups_dvfu:.3f} км ({distance_vgups_dvfu * 1000:.0f} м)")
print("-" * 40)