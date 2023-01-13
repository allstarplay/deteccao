FROM python:3.11-slim as builder

RUN mkdir -p /app
WORKDIR /app

# Aquivo de dependências
# ADD requirements.txt .
# ADD requirements ./requirements/
# Atualiza o apt do Linux
RUN apt update
RUN apt -y upgrade

RUN python3 -m venv venv 
#     # && venv/bin/python -m pip install --no-cache-dir -r requirements.txt

ADD . .

# FROM python:3.11-slim

# Envs
# ENV HOME="/app"
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV PATH="/${HOME}/venv/bin:$PATH"
# ENV PYTHONPATH "${PYTHONPATH}:${HOME}"
# ENV PORT 5000

# Cria e define o diretório padrão de trabalho
# RUN mkdir -p ${HOME}
# WORKDIR ${HOME}

# # Copia o código fonte da aplicação
# COPY --from=builder ${HOME} ${HOME}

# #Cria o grupo, usuário e prepara o venv
# RUN addgroup --quiet --gid 2000 nanascreen \
#     && useradd nanascreen --uid=2000 --gid=2000 --home-dir ${HOME} --no-create-home --shell /bin/bash \
#     && chown -R nanascreen:nanascreen ${HOME}

# # Define o usuário padrão para essa imagem
# USER nanascreen

# Resolve problema de linas entre Win e Linux
RUN sed -i -e 's/\r$//' ./ativar-ambiente.sh