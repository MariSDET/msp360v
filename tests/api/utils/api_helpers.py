import random
import string
import datetime
import hashlib

from tests.api.data_models import UserDetails

def generate_user_details():
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    email = f"testusername_{current_time}@example.com"
    password = hashlib.md5(current_time.encode()).hexdigest()
    first_name = generate_random_string()
    last_name = generate_random_string()
    return UserDetails(email=email, password=password, first_name=first_name, last_name=last_name)

def generate_random_string(min_length=5, max_length=12):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

