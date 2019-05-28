from datetime import datetime
import random
import string


if __name__ == '__main__':
    user_id = 1
    current_date = datetime.now().strftime("%Y-%m-%d")
    csv = ''

    for i in range(2000):
        name = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
        mail = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
        phone = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        desc = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150))

        csv += str(user_id) + ',' + name + ',' + mail + ',' + phone + ',' + current_date + ','
        csv += str(random.randrange(1000, 100000)) + ',' + str(random.randrange(1000, 100000)) + ',' + desc + '\n'

        user_id += 1

    with open('../data.csv', 'w') as csv_file:
        csv_file.write(csv)
