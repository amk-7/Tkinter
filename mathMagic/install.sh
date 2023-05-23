#!/bin/bash

if test $# -ne 0; then 
	if (($1=='-u')); then
		echo "::::::::::::::::::::::::::::::::::::::Désinstallation::::::::::::::::::::::::::::::::::::::"
		rm /usr/bin/mathmagic
		exit 1
	fi
fi

#pip install -r requirements.txt
#python3 setup.py build

touch mathmagique.desktop
echo "[Desktop Entry]" > mathmagique.desktop
echo "Version=1.0" >> mathmagique.desktop
echo "Name=MathMagic" >> mathmagique.desktop
echo "Comment=Application de génération de figure mathématique tel que les fonctions" >> mathmagique.desktop
echo "Exec="$(pwd)"/build/exe.linux-x86_64-3.8/MathMagique" >> mathmagique.desktop
echo "Icon="$(pwd)"/icon/logo.png" >> mathmagique.desktop
echo "Terminal=false" >> mathmagique.desktop
echo "Type=Application" >> mathmagique.desktop
echo "Categories=ApplicationCategory" >> mathmagique.desktop

mv mathmagique.desktop ~/.local/share/applications/



