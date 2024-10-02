from operator import index


def send_email(message, recipient, sender="university.help@gmail.com"):

    if (recipient.count('@') == 0
        or sender.count('@') == 0
        or (recipient[len(recipient) - 4:] != '.com'
            and recipient[len(recipient) - 3:] != '.ru'
            and recipient[len(recipient) - 4:] != '.net'
            )
        or (sender[len(sender) - 4:] != '.com'
            and sender[len(sender) - 3:] != '.ru'
            and sender[len(sender) - 4:] != '.net'
            )
        ):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

#s = 'vasyok1337@gmail.com'
#print(s[len(s) - 4:])
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
