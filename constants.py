from random_useragent.random_useragent import Randomize
from typing import List
MIXPANNEL_TOKENS: List[str] = [
    '520a47b63098ffbb27467bc2756a295b', '7c0ae2b86bddaf03a7030d956f677b1a'
FINNISH_IP_ADDRESSES = [
    ('37.33.0.0', '37.33.255.255'),
    ('37.136.0.0', '37.136.255.255'),
    ('62.78.128.0', '62.78.255.255'),
    ('80.220.0.0', '80.220.0.0'),
]
RANDOM_USERS_URL: str = 'https://randomuser.me/api/'
MUFFIN_BANANA = 'Banana muffin'
MUFFIN_DARK = 'Dark Chocolate muffin'
MUFFIN_RAISINS = 'Raisins muffin'
MUFFIN_VANILLA = 'Vanilla muffin'
MAX_NUMBER_OF_REGISTERED_USERS = 900
SHOP_PRODUCTS = [
    (MUFFIN_DARK, 40),
    (MUFFIN_BANANA, 20),
    (MUFFIN_RAISINS, 20),
    (MUFFIN_VANILLA, 20),
]
PRODUCTS_PRICES = {
    MUFFIN_BANANA: 1,
    MUFFIN_DARK: 1.5,
    MUFFIN_RAISINS: 0.75,
    MUFFIN_VANILLA: 1
}
DEVICE_OS_CHOICES = [
    ('desktop', 'windows'),
    ('desktop', 'linux'),
    ('desktop', 'mac'),
    ('smartphone', 'android'),
    ('smartphone', 'ios')
]

STEP_MAIN = 'main'
STEP_VIEW_ITEM = 'view_item'
STEP_ADD_ITEM_TO_CART = 'add_item_to_cart'
STEP_CHECKOUT = 'checkout'
STEP_REGISTER = 'register'
STEP_PAY = 'pay'
STEP_DROP = 'drop'
STEPS = {
    STEP_MAIN: {
        'human_readable': 'Home Page Viewed',
        'next_steps': [(STEP_VIEW_ITEM, 80), (STEP_DROP, 20)]
    },
    STEP_VIEW_ITEM: {
        'human_readable': 'Item Page Viewed',
        'next_steps': [(STEP_VIEW_ITEM, 30), (STEP_ADD_ITEM_TO_CART, 30), (STEP_MAIN, 30), (STEP_DROP, 10)],
        'generates': ['item_name']
    },
    STEP_ADD_ITEM_TO_CART: {
        'human_readable': 'Item Added To Cart',
        'next_steps': [(STEP_VIEW_ITEM, 35), (STEP_MAIN, 25), (STEP_DROP, 10), (STEP_CHECKOUT, 30)],
        'generates': ['item_count'],
        'requires': ['item_name'],
    },
    STEP_CHECKOUT: {
        'human_readable': 'Checkout Initiated',
        'next_steps': [(STEP_REGISTER, 80), (STEP_DROP, 20)],
        'requires': ['cart_content']
    },
    STEP_REGISTER: {
        'human_readable': 'Customer Registered',
        'next_steps': [(STEP_PAY, 80), (STEP_MAIN, 20)],
        'requires': ['register_user'],
    },
    STEP_PAY: {
        'human_readable': 'Order Paid',
        'next_steps': [(STEP_DROP, 100)],
        'requires': ['cart_value']
    },
    STEP_DROP: {
        'human_readable': 'Drop',
        'next_steps': []
    }
}
