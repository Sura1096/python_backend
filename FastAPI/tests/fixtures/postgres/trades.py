from datetime import date, datetime

TRADES = {
    'exchange_product_id': 'A100ANK060F',
    'exchange_product_name': 'Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)',
    'oil_id': 'A100',
    'delivery_basis_id': 'ANK',
    'delivery_basis_name': 'Ангарск-группа станций',
    'delivery_type_id': 'F',
    'volume': 60,
    'total': 3684360,
    'count': 1,
    'date': datetime.strptime('2023-12-26', '%Y-%m-%d').date(),
    'created_on': date.today(),
    'updated_on': date.today(),
}
