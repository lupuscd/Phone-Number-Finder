import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

ph_number = input('Enter the phone number: \n')

number_info = phonenumbers.parse(ph_number)
number_info_car = phonenumbers.parse(ph_number, 'RO')

number_country = geocoder.description_for_number(number_info, 'en')
number_carrier = carrier.name_for_number(number_info_car, 'en')

print(number_country, number_carrier)