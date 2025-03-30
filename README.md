# ChatToPDF - Convertisseur de conversations en PDF

Un outil Python pour convertir des conversations texte avec équations mathématiques en PDF bien formatés.

## Fonctionnalités
- Conversion des conversations texte vers PDF
- Support des équations LaTeX (entre \( \))
- Mise en forme des textes en gras (**texte**)
- Génération de PDF via LaTeX ou matplotlib

## Exemple de conversation

Voici un extrait du fichier `chat.txt` :

```
### USER
Dis moi quelles formules, théorèmes ou critère je dois apprendre pour un DS sur les séries numériques et explique les moi

### ASSISTANT  
1. **Séries géométriques**  
   - Formule : La série \(\sum_{n=0}^{\infty} a^n\) converge si et seulement si \(|a| < 1\), et sa somme est \(\frac{1}{1-a}\).  
   - Explication : C'est une série fondamentale où chaque terme est une puissance d'un nombre réel \(a\)...

2. **Séries de Riemann**  
   - Critère : La série \(\sum \frac{1}{n^\alpha}\) converge \(\iff \alpha > 1\)...
```

## PDF Généré

Le fichier PDF résultant est disponible ici : [chat_clean.pdf](chat_clean.pdf)

## Utilisation

1. Installez les dépendances :
```bash
pip install -r requirements.txt
```

2. Exécutez le script :
```bash
python chat_to_pdf.py
```

3. Le PDF sera généré dans le même dossier

## Configuration requise
- Python 3.8+
- MiKTeX ou LaTeX (pour la meilleure qualité)
- OU matplotlib (pour une solution sans LaTeX)