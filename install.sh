#!/bin/bash
# Caso dê algum erro na criação da imagem em ambiente windows, talvez seja necessário desligar a ferramenta buildkit do docker. 
# >> Settings >> Docker Engine >> Editar Json de configuração (alterar "buildkit" para false)

versao="latest"
BASEDIR=$(dirname "$0")
update=$1
listacontainers=($2)

function createDocker() {
	
	parentdir="$(dirname "$PWD")"

	[ ! -z $(docker images -q img_dev_ciencia_dados:$versao) ] || docker build --tag=img_dev_ciencia_dados:$versao . --no-cache
		
		
	echo "###########################################################"
	echo "############## CRIANDO CONTÊINER DOCKER ###############"
	echo "###########################################################"
	
	# Controle necessàrio pois no windows ocorre um problema ao recuperar a pasta atual que està sendo executado este script para poder utiliza-lo no comando de criação da imagem 
	if [ "$(uname)" == "Darwin" ] || [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]
	then
		echo " Utilizando plataforma Mac OS X ou Linux  "
		# Mac não testado 
		
		#[ -e "$parentdir/$1/install.sh" ] && rm "$parentdir/$1/install.sh"
		#[ -e "$parentdir/$1/Dockerfile" ] && rm "$parentdir/$1/Dockerfile"
		
		
		[ ! -z $(docker ps -a | grep ctn_dev_ciencia_dados-$1-dev) ] || docker create -t -i --name ctn_dev_ciencia_dados-$1-dev --network=host -p 4000:4000 -e JUPYTER_ENABLE_LAB=yes -v "$parentdir/$1/workdir":/home/user img_dev_ciencia_dados:$versao
		
	
	elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT"  ] || [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]
	then
		#echo " Utilizando plataforma Windows NT "
		workfolder="$(echo "$parentdir/$1/workdir" | sed 's/^\///' | sed 's/\//\\/g' | sed 's/^./\0:/')"
				
		#[ -e "$(echo "$parentdir/$1/install.sh" | sed 's/^\///' | sed 's/\//\\/g' | sed 's/^./\0:/')" ] && rm "$(echo "$parentdir/$1/install.sh" | sed 's/^\///' | sed 's/\//\\/g' | sed 's/^./\0:/')"
		#[ -e "$(echo "$parentdir/$1/Dockerfile" | sed 's/^\///' | sed 's/\//\\/g' | sed 's/^./\0:/')" ] && rm "$(echo "$parentdir/$1/Dockerfile" | sed 's/^\///' | sed 's/\//\\/g' | sed 's/^./\0:/')"
				
		[ ! -z $(docker ps -a | grep ctn_dev_ciencia_dados-$1-dev) ] || winpty docker create -t -i --name ctn_dev_ciencia_dados-$1-dev -p 4000:4000 -e JUPYTER_ENABLE_LAB=yes -v $workfolder:/home/user img_dev_ciencia_dados:$versao
		
	fi

}

if [ -z "$update" ] 
then
    
	echo -n "Qual o nome projeto? "
	read NOME_PROJETO 
	
	NOME_PROJETO=${NOME_PROJETO,,}
	NOME_PROJETO=${NOME_PROJETO//[^[:alnum:]]/}
	
	if [ -z "$NOME_PROJETO" ]
	then
		echo "Nome do projeto é obrigatório. " 
	else

		echo "Criando Docker do projeto $NOME_PROJETO"
	
		if [ -d ../$BASEDIR/$NOME_PROJETO ] 
		then 
			echo "Diretório do projeto já existe. Conteiner será criado caso não exista. Para iniciar o ambiente executar >> ./start.sh na pasta do projeto."			
			
	echo "###########################################################"
	echo "################ CRIANDO IMAGEM DOCKER ################"
	echo "###########################################################"
			
			createDocker $NOME_PROJETO			
		else
			cp -r $BASEDIR ../$BASEDIR/$NOME_PROJETO

	echo "###########################################################"
	echo "################ CRIANDO IMAGEM DOCKER ################"
	echo "###########################################################"

			createDocker $NOME_PROJETO		
			
			echo "Para iniciar o ambiente executar >> ./start.sh na pasta do projeto"
		fi	

	fi
	
else	
 
	[ -z $(docker images -q img_dev_ciencia_dados:$versao) ] || docker rmi img_dev_ciencia_dados:$versao
 
	[ ! -z $(docker images -q img_dev_ciencia_dados:$versao) ] || docker build --tag=img_dev_ciencia_dados:$versao . --no-cache --network=host

#echo ">>>>>>>>>>>>>>>>>>>>>> ${listacontainers[@]}"

	for i in "${listacontainers[@]}"
	do
		if [[ "$i" =~ .*"ctn_dev_ciencia_dados".* ]]
		then
			prefixo="ctn_dev_ciencia_dados-"			
			sufixo="-dev"
			subs=""
		
			projeto=$(echo "$i" | sed "s/$prefixo/$subs/")
			projeto=$(echo "$projeto" | sed "s/$sufixo/$subs/")


	echo "###########################################################"
	echo "##### ATUALIZANDO  CONTÊINER - PROJETO : $projeto #########"
	echo "###########################################################"


			#echo "Atualizando container: $projeto"
			createDocker "$projeto"
		 
		fi
	done
 
 
fi
