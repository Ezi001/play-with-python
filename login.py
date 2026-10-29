def login_screen():
    while True:
        print("Brukernavn: ", end="")
        username = input()

        if username == "":
            break # Avbryter løkken

        if username != "admin":
            print("Fant ikke bruker")
            continue # Avbryter resten av iterasjonen

        print(f"Passord for {username}: ", end="")
        password = input()
        if password == "42":
            print("Du er nå logget inn")
            return # Avbryter hele resten av funksjonen

    print("Slår av maskinen nå.")

login_screen()
