import os
import subprocess
import re

def clean_text(text):
    # Supprimer toutes les lignes contenant des #
    lines = text.split('\n')
    cleaned_lines = [line for line in lines if not re.search(r'#', line)]
    return '\n'.join(cleaned_lines)

def generate_latex_content(content):
    latex = r"""\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}

\begin{document}

\title{Conversation avec équations}
\author{Utilisateur \& Assistant}
\maketitle

"""

    sections = re.split(r'### (USER|ASSISTANT)\n', content)[1:]

    for i in range(0, len(sections), 2):
        speaker = sections[i]
        text = clean_text(sections[i+1])
        
        # Convertir les équations LaTeX
        text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text)
        text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
        
        title = "Utilisateur" if speaker == 'USER' else "Assistant"
        latex += f"\\section{{{title}}}\n{text}\n\n"

    latex += r"\end{document}"
    return latex

def convert_chat_to_pdf(input_file, output_file):
    # Chemin complet vers pdflatex
    pdflatex_path = r'C:\Users\Hugo\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe'
    
    if not os.path.exists(pdflatex_path):
        raise FileNotFoundError(f"pdflatex.exe introuvable à {pdflatex_path}")

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    latex_content = generate_latex_content(content)
    
    # Générer le fichier .tex
    tex_file = output_file.replace('.pdf', '.tex')
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    print(f"Fichier LaTeX généré: {os.path.abspath(tex_file)}")
    
    # Compiler avec pdflatex
    working_dir = os.path.dirname(os.path.abspath(tex_file))
    print(f"Compilation dans le répertoire: {working_dir}")
    
    try:
        result = subprocess.run(
            [pdflatex_path, '-interaction=nonstopmode', os.path.basename(tex_file)],
            check=True,
            cwd=working_dir,
            capture_output=True,
            text=True
        )
        print("Compilation LaTeX réussie")
        print(f"PDF généré avec succès: {output_file}")
        print(f"Ouvrir le PDF: explorer {os.path.abspath(output_file)}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la compilation LaTeX (code {e.returncode}):")
        print(f"Sortie pdflatex:\n{e.stdout}")
        print(f"Erreur pdflatex:\n{e.stderr}")
        return False

if __name__ == "__main__":
    input_file = "chat.txt"
    output_file = "chat_clean.pdf"
    convert_chat_to_pdf(input_file, output_file)