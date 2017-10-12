#!/bin/bash

IFS=$'\;'

LIST="(bull)shit;piss;fuck;cunt;cocksucker;motherfucker;tits;bitch;ass(hole)"

#"$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "${1}")"
AUTHOR=${1}
SONG=${2}

echo -e "\n${1} - ${2}"

URL="http://www.lyrics007.com/${1} Lyrics/${2} Lyrics.html"
#echo ${URL}
wget -q ${URL}
NAME="${2} Lyrics.html"

if [ -f "404.html" ] #|| "`egrep 'Sorry, this song or the artist is deleted.' "${NAME}"`" == "" ]
then
	echo -e "  great jumpin' jacks, charlie brown! this song doesn't exist!\n"
	rm "404.html"
	echo ${AUTHOR} | tee auth
	echo ${SONG} | tee song
	perl -pi -e 's/\ /\-/g' auth
	perl -pi -e 's/\ /\-/g' song
	#AUTHOR=`sed -i 's/ /-/g' auth`
	#SONG=`sed -i 's/ /-/g' song`
	URL="http://www.lyricstime.com/"`cat auth`"-"`cat song`"-lyrics.html"
	rm auth
	rm song
	wget -q ${URL}
fi

BIT=0
for i in ${LIST}
do
	TEST=`egrep -io " [^\s]*${i}[^\s]* " "${NAME}"`
	if [ "${TEST}" != "" ]
	then
		T2=`echo ${TEST} | sort | uniq`
		echo -e "\n dirteh wordz alert!: ${i}"
		echo -e " possible matches:\n${T2}"
		BIT=1
	#else
		#echo "none of ${i}"
	fi
done

if [ ${BIT} = 1 ]
then
	echo -e "\n  dirteh song!"
else
	echo "  no 'cocks' on this block (of text) - carry on"
fi

rm "${2} Lyrics.html"
