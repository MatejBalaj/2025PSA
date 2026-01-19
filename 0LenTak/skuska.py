vstup = "ID: 553; NAME: Matej Balaj; EMAIL: matej.balaj@example.com; SCORE: 87; STATUS: active"
id, cele_meno, email, skore, status = vstup.split(";")

# ID
id = id.strip()
id2 = int(id.split(":")[1])

# Meno a priezvisko
cele_meno = cele_meno.split(":")[1].strip()
meno, priezvisko = cele_meno.split(" ")

# Email
email = email.split(":")
email2 = email[1].strip()

# Skóre
skore = skore.split(":")
score = int(skore[1].strip())

# Status
status = status.split(":")
status2 = status[1].strip() == "active"

# Výsledok
vysledok = {
    "id": id2,
    "first_name": meno,
    "last_name": priezvisko,
    "email": email2,
    "score": score,
    "active": status2
}

print(vysledok)
