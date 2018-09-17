import os


def top_menu():
    data = [
        {"name": "Новости", "slug": "news", "visible": True, "content": None},
        {"name": "Каталог", "slug": "catalogue", "visible": True, "content": None},
        {"name": "Справочник", "slug": "handbook", "visible": True, "content": None},
        {"name": "прайс товаров, услуг", "slug": "price", "visible": True, "content": None},
        {"name": "фотогалерея базы", "slug": "gallery", "visible": True, "content": None},
        {"name": "о компании", "slug": "about", "visible": True, "content": None},
        {"name": "технокад", "slug": "technocad", "visible": True, "content": None},
        {"name": "контакты", "slug": "contact", "visible": True, "content": None},
    ]
    return data


def organization():
    data = {
        "logo": os.path.join("static" , "pic", "logo.jpg"),
        "phone": "362-29-00",
        "email": "trachukaf@yandex.ru",
        "phone_prefix": "343",
        "contact_text": "как к нам добраться?",
        "footer_email": "cherkasov.kirill@gmail.com",
        "footer_phone": "323-32-18",
        "footer_desc": "г. Екатеринбург, ул. Монтажников, 32а <br/> ул. Начдива Васильева, 3а",
        "name": "ЗАО Металлгазснаб",
    }
    return data
