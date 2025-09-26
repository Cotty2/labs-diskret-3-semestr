import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Радиус Земли в километрах
    R = 6371
    
    # Разница координат
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Формула гаверсинусов
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    distance = R * c
    return distance

def degrees_to_radians(degrees):
    """Переводит градусы в радианы"""
    return degrees * math.pi / 180

# Координаты Туры (из таблицы)
tura_lat_deg = 64.28  # северная широта
tura_lon_deg = 100.22  # восточная долгота

# Координаты Нью-Йорка (из таблицы)
ny_lat_deg = 40.71   # северная широта  
ny_lon_deg = -74.01  # западная долгота (отрицательное значение)

# Координаты Сиднея (из таблицы)
sydney_lat_deg = -33.874  # южная широта (отрицательное значение)
sydney_lon_deg = 151.213  # восточная долгота

# Перевод координат в радианы
tura_lat_rad = degrees_to_radians(tura_lat_deg)
tura_lon_rad = degrees_to_radians(tura_lon_deg)
ny_lat_rad = degrees_to_radians(ny_lat_deg)
ny_lon_rad = degrees_to_radians(ny_lon_deg)
sydney_lat_rad = degrees_to_radians(sydney_lat_deg)
sydney_lon_rad = degrees_to_radians(sydney_lon_deg)

# Расчет расстояний
distance_ny = calculate_distance(tura_lat_rad, tura_lon_rad, ny_lat_rad, ny_lon_rad)
distance_sydney = calculate_distance(tura_lat_rad, tura_lon_rad, sydney_lat_rad, sydney_lon_rad)

# Вывод результатов
print("Расстояния от Туры до других городов:")
print(f"Тура - Нью-Йорк: {distance_ny:.0f} км")
print(f"Тура - Сидней: {distance_sydney:.0f} км")
