#!/bin/bash

while read line;do
    number=`echo $line|cut -d '|' -f 1`
    name=`echo $line|cut -d '|' -f 2`
    scm=`echo $line|cut -d '|' -f 6`
    link=`echo $line|cut -d '|' -f 7`
    echo $number
    if [ ! -e $name ]
    then
        mkdir  $number
    fi
    cd $number
    if [ $scm = "Subversion" ]
    then
        svn checkout $link
    elif [ $scm = "GIT" ]
    then
        git clone $link
    elif [ $scm = "Mercurial" ]
    then
        hg clone $link
    elif [ $scm = "Bazaar" ]
    then
        bzr checkout $link
    fi
    echo $number,$? >> ../status.txt
    cd ..
done
