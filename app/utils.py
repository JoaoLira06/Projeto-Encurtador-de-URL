import random
import string


def generate_short_code(lenght: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=lenght))