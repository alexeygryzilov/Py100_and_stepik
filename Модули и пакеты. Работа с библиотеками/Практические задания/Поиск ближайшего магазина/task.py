# TODO Отрефакторите код
# def get_distance(shop_point: tuple[float, float]) -> float:
#    """Функция для вычисления евклидово расстояния до магазина."""
#    return (shop_point[0] ** 2 + shop_point[1] ** 2) ** 0.5


# def get_nearest_shop(shop_points: list[tuple]) -> tuple:
#    return min(shop_points, key=get_distance)

def get_nearest_shop(shop_point: tuple[float, float]) -> float:
    result = min(shop_point, key=lambda x: x[0] ** 2 + x[1] ** 2)
    return result

if __name__ == '__main__':
    points = [
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    nearest_shop = get_nearest_shop(points)
    print(f"Ближайший магазин находится в координатах: {nearest_shop}")
