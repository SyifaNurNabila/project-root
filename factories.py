from faker import Faker
import random

fake = Faker()

# Factory to create fake products
def create_fake_product():
    return {
        'name': fake.word(),
        'category': fake.word(),
        'availability': random.choice([True, False]),
        'price': random.uniform(10.0, 1000.0)
    }
