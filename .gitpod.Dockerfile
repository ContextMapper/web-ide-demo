FROM gitpod/workspace-full

# Install Graphviz
RUN sudo apt-get update \
    && sudo apt-get -y install graphviz

# Install JHipster
RUN npm install -g generator-jhipster
