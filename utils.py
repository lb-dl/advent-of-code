from faker import Faker

def open_file():

    with open ('requirements.txt', encoding = 'utf-8') as file:
        return file.read()




def generate_fake_users(users_number: int = 100):
    faker = Faker()
    fake_names = ''
    for _ in range(users_number):
        fake_names += (faker.name() + ' ' + faker.email() + ' ')
    return fake_names


