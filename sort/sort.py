from pathlib import Path

"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""

"""
1 : récupérer en input, le chemin du dossier à analyser et dans lequel faire le tri
2 : faire la liste des fichiers à trier
3 : identifier les formats de fichiers. Ce sera nécessaire pour savoir quel dossier on doit créer
4 : si dossier de tri inexistant(s), créer le(s) dossier(s)
5 : déplacer les fichiers dans les bons dossiers
"""