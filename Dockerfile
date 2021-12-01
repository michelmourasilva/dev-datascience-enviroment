FROM continuumio/miniconda3

#------------------------------------
#Dependências do sistema
#------------------------------------
RUN apt-get update -y
RUN apt-get install -y python3-dev python3-pip build-essential graphviz

#------------------------------------
#Instalação jupyter
#------------------------------------
RUN conda install -c conda-forge jupyterlab
RUN conda install -c conda-forge nodejs
RUN conda install xeus-python -c conda-forge
RUN conda install -c conda-forge jupyterlab_code_formatter
#RUN conda install -c conda-forge jupyterlab jupyterlab-git
#RUN jupyter labextension install jupyterlab-gitlab
RUN jupyter labextension install @jupyterlab/debugger
#RUN jupyter labextension install @krassowski/jupyterlab_go_to_definition
RUN conda install -c conda-forge 'jupyterlab>=3.0.0,<4.0.0a0' jupyterlab-lsp

#------------------------------------
#Instalação python - requeriments
#------------------------------------
COPY requirements.txt /requirements.txt 
RUN pip3 install --upgrade pip #Atualização do gerenciador de pacotes
RUN pip3 install -r requirements.txt  #Instalação dos pacotes listados

#------------------------------------
# bibliotecas mais comuns utilizadas
# Serão previamente instaladas para que o arquivo 
# requirements possua só o que pode ser específico de cada projeto/assunto
#------------------------------------
RUN pip3 install 'python-language-server[all]'
RUN pip3 install numpy==1.20.1
RUN pip3 install pandas==1.2.3
RUN pip3 install SciPy==1.6.1
RUN pip3 install StatsModels==0.12.2
RUN pip3 install Matplotlib==3.3.4
RUN pip3 install Seaborn==0.11.1
RUN pip3 install Plotly==4.14.3
RUN pip3 install Bokeh==2.3.0
RUN pip3 install Pydot==1.4.2
RUN pip3 install Scikit-learn==0.24.1
RUN pip3 install Scrapy==2.4.1
RUN pip3 install Requests==2.24.0
RUN pip3 install beautifulsoup4==4.9.3
RUN pip3 install df2gspread==1.0.4
RUN pip3 install oauthlib==3.1.0  # autenticacao OAuth1 ou OAuth2
RUN pip3 install gspread==3.7.0 # planilhas google sheet
RUN pip3 install kafka-python==2.0.2
RUN pip3 install black==20.8b1
RUN pip3 install isort==5.7.0
RUN pip3 install pandas-profiling==2.11.0
RUN pip3 install psycopg2-binary==2.8.6
RUN pip3 install explainerdashboard==0.3.3.1
RUN pip3 install diagrams==0.19.1

# pip install pydl4j
RUN apt-get install -y python3-opencv

#------------------------------------
#MICROSOFT SQL - DEPENDENCIAS
#------------------------------------
#RUN apt-get -y install apt-transport-https
#RUN apt-get -y install curl
#RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
#RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
#RUN apt-get update
#RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17
#RUN apt-get -y install unixodbc-dev

#------------------------------------
#ORACLE - DEPENDENCIAS
#------------------------------------
#ENV ORACLE_INSTANTCLIENT_MAJOR 12.2
#ENV ORACLE_INSTANTCLIENT_VERSION 12.2.0.1.0
#ENV ORACLE /usr/local/oracle
#ENV ORACLE_HOME $ORACLE/lib/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64
#ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$ORACLE_HOME/lib
#ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$ORACLE/include/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64

#RUN apt-get update && apt-get install -y libaio1 \
#        curl rpm2cpio cpio \
#    && mkdir $ORACLE && TMP_DIR="$(mktemp -d)" && cd "$TMP_DIR" \
#    && curl -L https://github.com/sergeymakinen/docker-oracle-instant-client/raw/assets/oracle-instantclient$ORACLE_INSTANTCLIENT_MAJOR-basic-$ORACLE_INSTANTCLIENT_VERSION-1.x86_64.rpm -o basic.rpm \
#    && rpm2cpio basic.rpm | cpio -i -d -v && cp -r usr/* $ORACLE && rm -rf ./* \
#    && ln -s libclntsh.so.12.1 $ORACLE/lib/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64/lib/libclntsh.so.$ORACLE_INSTANTCLIENT_MAJOR \
#    && ln -s libocci.so.12.1 $ORACLE/lib/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64/lib/libocci.so.$ORACLE_INSTANTCLIENT_MAJOR \
#    && curl -L https://github.com/sergeymakinen/docker-oracle-instant-client/raw/assets/oracle-instantclient$ORACLE_INSTANTCLIENT_MAJOR-devel-$ORACLE_INSTANTCLIENT_VERSION-1.x86_64.rpm -o devel.rpm \
#    && rpm2cpio devel.rpm | cpio -i -d -v && cp -r usr/* $ORACLE && rm -rf "$TMP_DIR" \
#    && echo "$ORACLE_HOME/lib" > /etc/ld.so.conf.d/oracle.conf && chmod o+r /etc/ld.so.conf.d/oracle.conf && ldconfig \
#    && rm -rf /var/lib/apt/lists/* && apt-get purge -y --auto-remove curl rpm2cpio cpio

#------------------------------------
#Diretório do usuário docker
#------------------------------------
RUN mkdir -p /home/user
WORKDIR /home/user

EXPOSE 5432
