#!/bin/bash

IFS=$'\n'

clear

echo -e "\n\n\nThou hast invoked the sacred PLAYLIST FILTER"
echo "OUTPUT shall exist in the current directory under a name thou chooseth"
echo "CTRL+C if thou wishes to leave this accursed task"
echo "- the management"

echo -e "\ncurrent files in directory :\n"

ls -1

echo -ne "\ninput file : "
read IN
echo -n "output file (default 'log') : "
read OUT

if [ "${OUT}" == "" ]
then
	OUT="log"
fi

if [ -f ${OUT} ]
then
	while [ "${RE}" != "yes" ] && [ "${RE}" != "no" ]
	do
		echo -e "\n(please write 'yes' or 'no')"
		echo -n "overwrite file (yes/no) ? "
		read RE
	done

	if [ "${RE}" == "yes" ]
	then
		echo -e "\n\n\nup and down arrows to scroll, q to quit\n" > ${OUT}
	else
		echo -e "\n\n\nup and down arrows to scroll, q to quit\n" >> ${OUT}
	fi
else
	echo -e "\n\n\nup and down arrows to scroll, q to quit\n" > ${OUT}
fi	

if [ "${OUT}" == "" ]
then
	OUT="log"
fi

echo "-------------------- THE ACCURSED LOG FILE -------------------" >> ${OUT}
echo "-------------------- CIRCA "`date +"%B %d %Y (%a)"` >> ${OUT}

echo -e "\nworking..."

for i in `cat ${IN}`
do
	echo ${i} | tee tmp
	AUTHOR=`cut -f1 tmp`
	SONG=`cut -f2 tmp`
	bash lyrics.sh "${AUTHOR}" "${SONG}" >> ${OUT}
	rm tmp
done
echo

cat ${OUT} | less

exit 0
