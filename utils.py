from faker import Faker

def generate_fake_users(users_number: int = 100):
    faker = Faker()
    fake_names = ''
    fake_emails = ''
    for _ in range(users_number):
        fake_names += (faker.name() + ' ' + faker.email() + ' ')
    return fake_names + fake_emails

gi

