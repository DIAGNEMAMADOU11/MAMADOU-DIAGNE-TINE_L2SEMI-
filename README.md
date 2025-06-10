# MAMADOU-DIAGNE-TINE_L2SEMI-
📡 Cartographie des Appareils Connectés – Rapport Technique
📝 Description du projet
Cette application permet de scanner un réseau local et d’afficher sur une carte interactive les appareils détectés (adresse IP, adresse MAC, nom d’hôte). Elle est conçue pour un usage en réseau privé, principalement à des fins d’audit ou de visualisation rapide.

🧱 Architecture du projet
bash
Copier
Modifier
cartographie_reseau/
├── app.py               # Application Flask (serveur backend)
├── scan.py              # Fonction de scan du réseau avec Nmap
├── frontend/
│   ├── index.html       # Interface utilisateur (carte interactive)
│   ├── script.js        # JS pour charger les données depuis l’API (intégré dans index.html)
│   └── style.css        # Feuilles de style éventuelles (CSS)
⚙️ Fonctionnement technique
1. Scan réseau (scan.py)
Utilise la bibliothèque python-nmap pour lancer un scan de type ping scan (-sn) sur le réseau local (192.168.1.0/24 par défaut).
Chaque appareil détecté renvoie :

l’adresse IP

l’adresse MAC

le nom d’hôte (si disponible)
le os 
les ports ouverts 
la vulnerabilite 


2. API Flask (app.py)
GET /api/devices : Lance un scan et retourne les appareils détectés au format JSON.

/ et /<path> : Servez l’interface web depuis le dossier frontend.

3. Interface web (index.html)
Carte interactive centrée sur Dakar (Sénégal) avec Leaflet.js

Marqueurs positionnés avec un léger décalage aléatoire autour de Dakar (car les vrais appareils ne sont pas géolocalisables par IP localement)

Chaque marqueur affiche un popup contenant :

le nom de l’appareil (ou "Appareil inconnu")

l’adresse IP

l’adresse MAC

✅ Fonctionnalités principales
 Scan réseau local avec nmap

 API REST en Flask

 Affichage dynamique sur carte Leaflet

 Interface légère et réactive

 Détection en temps réel à chaque chargement

🚀 Lancement du projet
1. Prérequis
Python 3.x

Nmap installé (accessible dans le terminal)

Pip packages :

bash
Copier
Modifier
pip install flask python-nmap
2. Démarrage
bash
Copier
Modifier
python app.py
Ouvrir le navigateur à l’adresse :
📍 http://127.0.0.1:5000

🔒 Sécurité et limitations
Cette application utilise un ping scan, ce qui nécessite parfois des droits administrateur.

À ne pas utiliser tel quel en environnement de production.

👤 Auteur
Projet réalisé par [MAMADOU DIAGNE TINE ], dans le cadre de [/ projet personnel /AVEC M. TOP ISI_DAKAR].

