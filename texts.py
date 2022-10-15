def welc(text):
    welcome = f'Добро пожаловать, в бота {text}, здесь вы сможете приобрести товары различных категорий.'
    return welcome

main_btns = [
    'Поды',
    'Жидкости', 
    'Картриджи',
    'Мой профиль',
    'Тех. Поддержка'
]


pods_btns = [
    'Xros 2',
    'Aegis',
    'Drag 2',
    'Xros mini'
]

def txt_xros2(text):
    text_xros2 = "➖➖➖➖➖➖➖➖➖➖➖➖" + f"\nТовар: {text}" + f"\nВ наличии: ⭕ or ✅" + "\n➖➖➖➖➖➖➖➖➖➖➖➖"
    return text_xros2
    



