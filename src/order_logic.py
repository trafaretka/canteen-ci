def calculate_total(items: list[float], discount_percent: float = 0.0) -> float:
    """Рассчитывает итоговую стоимость заказа с учётом скидки."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть от 0 до 100%")
    subtotal = sum(items)
    return round(subtotal * (1 - discount_percent / 100), 2)


def is_preorder_available(hour: int) -> bool:
    """Проверяет, открыт ли предзаказ (доступен с 8:00 до 16:00)."""
    return 8 <= hour <= 16
