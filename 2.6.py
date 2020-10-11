art1 = "010203"
art2 = "040506"
art3 = "070809"
product1_properties = {"название": "компьютер", "цена": 1000, "количество": 5, "единицы измерения": "шт."}
product2_properties = {"название": "принтер", "цена": 800, "количество": 3, "единицы измерения": "шт."}
product3_properties = {"название": "сканер", "цена": 500, "количество": 10, "единицы измерения": "шт."}
product1 = (art1, product1_properties)
product2 = (art2, product2_properties)
product3 = (art3, product3_properties)
goods = [product1, product2, product3]
goods_length = len(goods)
analytics_name = []
analytics_price = []
analytics_quantity = []
analytics_units = set()
i = 0
while i < goods_length:
    analytics_name.append(goods[i][1].get("название"))
    analytics_price.append(goods[i][1].get("цена"))
    analytics_quantity.append(goods[i][1].get("количество"))
    analytics_units.add(goods[i][1].get("единицы измерения"))
    i += 1
analytics = [analytics_name, analytics_price, analytics_quantity, analytics_units]
print("Раздел 'Товары' содержит следующую номенклатуру:")
print(goods[0])
print(goods[1])
print(goods[2])
print("")
print("Аналитика по разделу")
print(analytics[0])
print(analytics[1])
print(analytics[2])
print(analytics[3])