preparar-ambiente:	
	sudo apt update
	sudo apt -y upgrade
	sudo apt install python3.11
	python3 -V
	sudo apt install -y python3.11-venv
	python3 -m venv venv

venv:
	python3 -m venv venv

limpar-venv:
	rm -rf venv

