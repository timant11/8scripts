to_inp = input("Кому письмо:\n")
from_inp = input("От кого письмо:\n")
subj_inp = input("Тема письма:\n")
in_last_email_inp = input("О чём просил в прошлом письме:\n")
body_inp = input("Повествование:\n")
question_in_end_inp = input("Вопрос в конце письма:\n")
print(f"""
To: {to_inp.capitalize()}
From: {from_inp.capitalize()}
Subject: {subj_inp.capitalize()}
Dear {to_inp.capitalize()},
Thanks for your email! I’m always glad to hear from you. How are you?
In your email you asked me about {in_last_email_inp.lower()}. {body_inp.capitalize()}
{question_in_end_inp.capitalize()}? Write back soon.
Best wishes,
{from_inp.capitalize()}
""")
