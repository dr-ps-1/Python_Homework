from address import Address
from mailing import Mailing

to_address = Address("112233", "Казань", "Казанская", "1", "10")
from_address = Address("445566", "Москва", "Московская", "2", "20")


mailing = Mailing(to_address, from_address, 100, "TRACK10000")


output = (f"Отправление {mailing.track} из {mailing.from_address.index}, "
          f"{mailing.from_address.city}, {mailing.from_address.street}, "
          f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
          f"{mailing.to_address.index}, {mailing.to_address.city}, "
          f"{mailing.to_address.street}, {mailing.to_address.house} - "
          f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")

print(output)
