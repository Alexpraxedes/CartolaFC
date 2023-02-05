FROM python:3.10.2-slim

RUN useradd -ms /bin/bash python && \
    apt update && \
    apt install -y git ca-certificates \
    openjdk-11-jre \
    zsh \
    curl \
    wget \
    fonts-powerline  \
    procps

RUN pip install pipenv

USER python

WORKDIR /home/python/app

# Default powerline10k theme, no plugins installed
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t https://github.com/romkatv/powerlevel10k.git \
    -p git \
    -p git-flow \
    -p https://github.com/zdharma/fast-syntax-highlighting \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -a 'export TERM=xterm-256color'

RUN echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc && \
    echo 'HISTFILE=/home/python/zsh/.zsh_history' >> ~/.zshrc

ENV PIPENV_VEN_IN_PROJECT=True

CMD ["tail", "-f", "/dev/null"]