#!/bin/bash
. ./scripts_config.sh

#=================================Global actions===================================
ACTION_EXIT='0'
ACTION_INIT_CREATE_APPLY_MIGRATION='1'
ACTION_INIT_MIGRATION='2'
ACTION_CREATE_MIGRATION='3'
ACTION_APPLY_MIGRATION='4'

#=================================End global actions===============================

select_do=''
press_key_continue=''

migrationInit(){
    eval "$RUN_CONTAINER" flask --app manage db init
}

migrationCreate(){
    eval "$RUN_CONTAINER" flask --app manage db migrate
}

migrationApply(){
    eval "$RUN_CONTAINER" flask --app manage db upgrade
}

while [ "$select_do" != "$ACTION_EXIT" ]; do

    echo $'\n'
	echo "Actions in DOCKER:"

    echo -e "$COLOR_TEXT_GREEN[$ACTION_INIT_CREATE_APPLY_MIGRATION] - Migration: init, create, and apply"
    echo -e "$COLOR_TEXT_SKY_BLUE[$ACTION_INIT_MIGRATION] - Migration init"
    echo -e "$COLOR_TEXT_YELLOW[$ACTION_CREATE_MIGRATION] - Migration create"
    echo -e "$COLOR_TEXT_GREEN[$ACTION_APPLY_MIGRATION] - Migration apply"

    echo -e "$COLOR_RESET[$ACTION_EXIT] - exit"
	echo $'\n'

    echo -n "Select an action: "
	read select_do


    if [ "$select_do" == "$ACTION_INIT_MIGRATION" ]; then
        migrationInit
    elif [ "$select_do" == "$ACTION_CREATE_MIGRATION" ]; then
        migrationCreate
    elif [ "$select_do" == "$ACTION_APPLY_MIGRATION" ]; then
        migrationApply
    elif [ "$select_do" == "$ACTION_INIT_CREATE_APPLY_MIGRATION" ]; then
        migrationInit
        migrationCreate
        migrationApply
    else
		echo "Error action!"
    fi

    if [ "$select_do" != "$ACTION_EXIT" ]; then
        select_do=''
        echo "Press enter to continue..."
        read press_key_continue
    fi


done