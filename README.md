# Nanascreen

Projeto responsável por fazer detecção de placas

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

Requisitos necessários que você precisa para instalar o software e como instalá-lo.

```
Ubuntu > 18.04
```

### 🔧 Instalação

Exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Logo após fazer o clone, usar os seguintes comandos abaixo:


Usar este comando para o problema que ocorre devido as diferenças no registro da quebra de linha feito pelo Windows e pelo Linux. Para resolver, vamos utilizar uma expressão regular e o comando SED:
```
sed -i -e 's/\r$//' ./pre-lin.sh
```

Usar este comando para preparar o ambiente ou o comando abaixo:
```
./pre-lin.sh
```

Logo em seguida, usar o comando abaixo para ativar o ambiente:
```
source ./act-lin.sh
```
##### *Obs: Para agilizar o uso, recomenda-se recortar o act-lin.sh ou act-win.sh e colocar na raiz do projeto.
<br/>

Instala os pacotes:
```
make req-dev
```

Copie o arquivo dotenv.dev para o arquivo .env4
```
cp ./devtools/dotenv.dev .env
```
ou

```
make cp
```


###### Autor: George Augusto da Silva
