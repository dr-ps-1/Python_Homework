from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S25", "+71111111111"),
    Smartphone("Samsung", "Galaxy S25 Ultra", "+72222222222"),
    Smartphone("Xiaomi", "Redmi Note 14", "+73333333333"),
    Smartphone("Apple", "iPhone 17", "+74444444444"),
    Smartphone("Honor", "400 Pro", "+75555555555")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
