# napisac klasę o nazwie np SpamSender w oddzielnym pliku - wykorzystać kod z Day10\exercises\mail.py
# SpamSender w konstruktorze powinien mieć możliwość podania adresu email i hasła do skrzynki pocztowej,
# z ktorej bedzie wysylany spam
# nastepnie nalezy stworzyc metodę, która będzie umożliwiała wysyłąnie maila (w formacie HTML) -
# przykład wysłania prostej wiadomości HTML w wyżej wymienionym pliku
# do danego odbiorcy
# najlepiej rozbić projekt na dwa pliki - jeden w ktorym bedziemy przechowywac klase, drugi w ktorym bedziemy
# wysylac wiadomości SPAM
# jako rozszerzenie zadania utworzyć listę emaili do których należy wysłać wiadomość SPAM,
# i przy użyciu pętli wysłać wiadomość do wszystkich maili z listy :slightly_smiling_face:


from Homeworks.SpamSender import SpamSender

receiver_email = ["olamitolamit@gmail.com", "isa12python@gmail.com"]
text = "To jest tekst wiadomosci wpisana przez uzytkownika."

SpamSender("isa12python@gmail.com","iSAforever",receiver_email,text)