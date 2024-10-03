from contextlib import nullcontext as does_not_raise
from datetime import date

PARAMS_TEST_LAST_TRADING_DATES = [
    # positive case
    (
        '/trades/last_dates',
        200,
        {
            'limit': 1,
            'offset': 0,
        },
        {
            'data': [{'date': '2023-12-26'}],
        },
        does_not_raise(),
    ),
    (
        '/trades/last_dates',
        200,
        {
            'limit': 5,
            'offset': 0,
        },
        {
            'data': [{'date': '2023-12-26'}],
        },
        does_not_raise(),
    ),
    # positive case with an empty answer
    (
        '/trades/last_dates',
        200,
        {
            'limit': 1,
            'offset': 2,
        },
        {
            'data': [],
        },
        does_not_raise(),
    ),
]

PARAMS_TEST_GET_DYNAMICS = [
    # positive case
    (
        '/trades/dynamics',
        200,
        {
            'start_date': date.fromisoformat('2023-12-26'),
            'end_date': date.fromisoformat('2023-12-27'),
            'limit': 1,
            'offset': 0,
        },
        {
            'data': [
                {
                    'id': 1,
                    'exchange_product_id': 'A100ANK060F',
                    'exchange_product_name': 'Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)',
                    'oil_id': 'A100',
                    'delivery_basis_id': 'ANK',
                    'delivery_basis_name': 'Ангарск-группа станций',
                    'delivery_type_id': 'F',
                    'volume': 60,
                    'total': 3684360,
                    'count': 1,
                    'date': '2023-12-26',
                    'created_on': '2024-10-03',
                    'updated_on': '2024-10-03',
                },
            ],
        },
        does_not_raise(),
    ),
    (
        '/trades/dynamics',
        200,
        {
            'start_date': date.fromisoformat('2023-12-26'),
            'end_date': date.fromisoformat('2023-12-27'),
            'limit': 1,
            'offset': 0,
            'oil_id': 'A100',
            'delivery_basis_id': 'ANK',
            'delivery_type_id': 'F',
        },
        {
            'data': [
                {
                    'id': 1,
                    'exchange_product_id': 'A100ANK060F',
                    'exchange_product_name': 'Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)',
                    'oil_id': 'A100',
                    'delivery_basis_id': 'ANK',
                    'delivery_basis_name': 'Ангарск-группа станций',
                    'delivery_type_id': 'F',
                    'volume': 60,
                    'total': 3684360,
                    'count': 1,
                    'date': '2023-12-26',
                    'created_on': '2024-10-03',
                    'updated_on': '2024-10-03',
                },
            ],
        },
        does_not_raise(),
    ),
    # positive case with an empty answer
    (
        '/trades/dynamics',
        200,
        {
            'start_date': date.fromisoformat('2023-12-28'),
            'end_date': date.fromisoformat('2023-12-29'),
            'limit': 1,
            'offset': 0,
            'oil_id': 'A100',
            'delivery_basis_id': 'ANK',
            'delivery_type_id': 'F',
        },
        {
            'data': [],
        },
        does_not_raise(),
    ),
]

PARAMS_TEST_TRADING_RESULTS = [
    # positive case
    (
        '/trades/last_results',
        200,
        {
            'limit': 1,
            'offset': 0,
            'oil_id': 'A100',
            'delivery_basis_id': 'ANK',
            'delivery_type_id': 'F',
        },
        {
            'data': [
                {
                    'id': 1,
                    'exchange_product_id': 'A100ANK060F',
                    'exchange_product_name': 'Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)',
                    'oil_id': 'A100',
                    'delivery_basis_id': 'ANK',
                    'delivery_basis_name': 'Ангарск-группа станций',
                    'delivery_type_id': 'F',
                    'volume': 60,
                    'total': 3684360,
                    'count': 1,
                    'date': '2023-12-26',
                    'created_on': '2024-10-03',
                    'updated_on': '2024-10-03',
                },
            ],
        },
        does_not_raise(),
    ),
    (
        '/trades/last_results',
        200,
        {
            'limit': 1,
            'offset': 0,
        },
        {
            'data': [
                {
                    'id': 1,
                    'exchange_product_id': 'A100ANK060F',
                    'exchange_product_name': 'Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)',
                    'oil_id': 'A100',
                    'delivery_basis_id': 'ANK',
                    'delivery_basis_name': 'Ангарск-группа станций',
                    'delivery_type_id': 'F',
                    'volume': 60,
                    'total': 3684360,
                    'count': 1,
                    'date': '2023-12-26',
                    'created_on': '2024-10-03',
                    'updated_on': '2024-10-03',
                },
            ],
        },
        does_not_raise(),
    ),
    (
        '/trades/last_results',
        200,
        {
            'limit': 1,
            'offset': 0,
            'oil_id': 'A100000',
            'delivery_basis_id': 'ANK',
            'delivery_type_id': 'F',
        },
        {
            'data': [],
        },
        does_not_raise(),
    ),
]
