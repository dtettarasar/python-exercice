mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
mdp_que_nb = "votre mot de passe ne contient que des nombres."
mdp_ok = "inscription terminée"

mdp_length = len(mdp)

# print(f"mot de passe: {mdp}")
# print(f"longueur du mot de passe: {mdp_length}")

if mdp_length == 0:
    print(mdp_trop_court.upper())
elif mdp_length < 8:
    print(mdp_trop_court.capitalize())
elif mdp.isdigit():
    print(mdp_que_nb.capitalize())
else:
    print(mdp_ok.capitalize())
