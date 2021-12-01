#!/bin/bash
# Caso dê algum erro na criação da imagem em ambiente windows, talvez seja necessário desligar a ferramenta buildkit do docker. 
# >> Settings >> Docker Engine >> Editar Json de configuração (alterar "buildkit" para false)

BASEDIR=$(dirname "$0")

parentdir="$(dirname "$PWD")"

NOME_PROJETO=${PWD##*/}


if [ ! "$(docker ps -a | grep ctn_dev_ciencia_dados-$NOME_PROJETO-dev)" ] 
then

	echo "Container do projeto não existe portanto será criado"

	printf "$NOME_PROJETO" | ./install.sh
	
	./start.sh

else

	 docker stop ctn_dev_ciencia_dados-$NOME_PROJETO-dev

	docker start ctn_dev_ciencia_dados-$NOME_PROJETO-dev
	
	docker  cp requirements.txt ctn_dev_ciencia_dados-$NOME_PROJETO-dev:/home/user



	# Controle necessàrio pois no windows ocorre um problema ao recuperar a pasta atual que està sendo executado este script para poder utiliza-lo no comando de criação da imagem 
	if [ "$(uname)" == "Darwin" ] || [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]
	then
		echo " Utilizando plataforma Mac OS X ou Linux  "
		# Mac não testado 
		
		docker exec -it ctn_dev_ciencia_dados-$NOME_PROJETO-dev bash -c "pip3 install -r requirements.txt; jupyter lab --ip 0.0.0.0 --port 4000 --allow-root" 
		
		
	elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT"  ] || [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]
	then
		#echo " Utilizando plataforma Windows NT "
		winpty  docker exec -it ctn_dev_ciencia_dados-$NOME_PROJETO-dev bash -c "pip3 install -r requirements.txt; jupyter lab --ip 0.0.0.0 --port=4000 --no-browser --allow-root" 
		
	fi

fi

