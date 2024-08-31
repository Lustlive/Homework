def send_email(message, recipient, *, sender="university.help@gmail.com"):
    Num = ".com", ".ru", ".net"
    Num1 = "@"
    send = "university.help@gmail.com"
    if not recipient.endswith(Num) or not sender.endswith(Num) or not Num1 in recipient or not Num1 in send:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    if sender == send:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

