def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if ".com" in recipient:
        recipient_adress = True
    elif ".ru" in recipient:
        recipient_adress = True
    elif ".net" in recipient:
        recipient_adress = True
    else:
        recipient_adress = False
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    if ".com" in sender:
        sender_adress = True
    elif ".ru" in sender:
        sender_adress = True
    elif ".net" in sender:
        sender_adress = True
    else:
        sender_adress = False
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return


    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')