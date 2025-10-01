from bs4 import BeautifulSoup

xml = open('map.xml', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'xml')

cnt = 0

# Поиск суши-баров
sushi_bars = []
for node in soup.find_all('node'):
    is_sushi = False
    name = "Без названия"

    for tag in node('tag'):
        if tag['k'] == 'cuisine' and ('sushi' in tag['v'].lower() or 'japanese' in tag['v'].lower()):
            is_sushi = True

        elif tag['k'] == 'description' and 'sushi' in tag['v'].lower():
            is_sushi = True

        elif tag['k'] == 'name':
            name = tag['v']
            if 'суши' in name.lower() or 'sushi' in name.lower():
                is_sushi = True

    if is_sushi:
        sushi_bars.append(name)

print("=" * 50)
print("НАЙДЕННЫЕ СУШИ-БАРЫ")
print("=" * 50)

for i, name in enumerate(sushi_bars, 1):
    print(f"{i}. {name}")

print(f"\nИТОГО: найдено {len(sushi_bars)} суши-баров")

# Поиск остановок общественного транспорта
print("\n" + "=" * 50)
print("ПОИСК ОСТАНОВОК")
print("=" * 50)

# Список для хранения найденных остановок
stops = []
specific_stops = ["ВГУЭС", "Некрасовская, 50", "ТГМУ", "ДВФУ"]
found_specific_stops = {}

for node in soup.find_all('node'):
    is_stop = False
    stop_name = "Без названия"
    stop_type = ""
    
    for tag in node('tag'):
        # Проверяем, является ли узел остановкой
        if tag['k'] == 'public_transport' and tag['v'] == 'stop_position':
            is_stop = True
            stop_type = "остановка транспорта"
        elif tag['k'] == 'highway' and tag['v'] == 'bus_stop':
            is_stop = True
            stop_type = "автобусная остановка"
        elif tag['k'] == 'bus' and tag['v'] == 'yes':
            is_stop = True
            stop_type = "автобусная остановка"
        
        # Получаем название остановки
        if tag['k'] == 'name':
            stop_name = tag['v']
            
            # Проверяем, является ли это одной из искомых остановок
            if stop_name in specific_stops:
                found_specific_stops[stop_name] = {
                    'id': node['id'],
                    'lat': node['lat'],
                    'lon': node['lon']
                }
    
    if is_stop:
        stops.append({
            'name': stop_name,
            'type': stop_type,
            'id': node['id'],
            'lat': node.get('lat'),
            'lon': node.get('lon')
        })

# Вывод всех остановок
print("\nВСЕ ОСТАНОВКИ ОБЩЕСТВЕННОГО ТРАНСПОРТА:")
print("-" * 50)
for i, stop in enumerate(stops, 1):
    print(f"{i}. {stop['name']} ({stop['type']})")
    if stop['lat'] and stop['lon']:
        print(f"   Координаты: {stop['lat']}, {stop['lon']}")

print(f"\nОБЩЕЕ КОЛИЧЕСТВО ОСТАНОВОК: {len(stops)}")

# Вывод конкретных искомых остановок
print("\n" + "=" * 50)


# Подсчет остановок по типам
bus_stops_count = len([stop for stop in stops if 'автобус' in stop['type']])
transport_stops_count = len([stop for stop in stops if 'транспорт' in stop['type']])

print(f"\nСТАТИСТИКА:")
print(f"Автобусных остановок: {bus_stops_count}")
print(f"Остановок транспорта: {transport_stops_count}")
print(f"Всего остановок: {len(stops)}")