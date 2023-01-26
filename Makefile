venv:
	python -m venv venv

clear-venv:
	rm -rf venv

req-dev: clear-venv	
	python -m venv venv
	python -m pip install --upgrade pip
	pip install -r requirements/develop.txt

cp:
	cp ./devtools/dotenv.dev .env


# Instala pacotes pessoal em modo editavel
e:
	pip install -e .

# Instala pacotes pessoal na lista de pacotes do pip
i:
	pip install .
