#!/bin/bash

if [ "${PWD##*/}" == "dev-datascience-enviroment" ]
then

git pull
declare -a containers

declare -a StringArray=$(docker container ls  -a --format "{{.Names}}") 
#echo $StringArray

for i in ${StringArray[@]}
do
	
	if  [ ${i:0:25} == "ctn_dev_ciencia_dados" ]
	then
		#echo "$i"
		containers+=("$i")
	fi
done

if [ ! -z "$containers" ]; then
    docker container stop "${containers[@]}"
	docker container rm "${containers[@]}"
	#echo "${containers[@]}"
else
    echo "Não existe contêiners"
fi

for j in ${containers[@]}
do
	./install.sh 1 "$j"
done



else

	echo "########################################################################"
	echo " Este comando deve ser executado dentro da pasta /dev-datascience-enviroment"
	echo "########################################################################"

fi


 
