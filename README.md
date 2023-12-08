
# Aïe aïe IA

Dans le cadre de la competition de la nuit de l'info 2023:
On a developpé une application simple HTML, vanilla JS, flask qui communique avec le API de OPENAI deployé en Azure.

Pour test ce projet vous devez copier le fichier de cles et le remplir par le vos:
```bash
cp .env.example .env
```

Pour installer les dependances de Python:
```bash
virtualenv venv
pip3 install -r requirements.txt
```

puis lancer le serveur avec :
```
python3 app.py
```

et dans un autre terminal lancer:

```
npx serve -p 3000
```

Tester le en tapant dans le navigateur http://localhost:3000

Merci!