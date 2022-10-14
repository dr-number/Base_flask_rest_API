#!/bin/bash
#===============================Colors============================================
COLOR_TEXT_BLACK='\033[30m'
COLOR_TEXT_RED='\033[31m'
COLOR_TEXT_GREEN='\033[32m'
COLOR_TEXT_YELLOW='\033[33m'
COLOR_TEXT_BLUE='\033[34m'
COLOR_TEXT_VIOLET='\033[35m'
COLOR_TEXT_SKY_BLUE='\033[36m'
COLOR_TEXT_GRAY='\033[37m'

COLOR_BG_BLACK='\033[40m'
COLOR_BG_RED='\033[41m'
COLOR_BG_GREEN='\033[42m'
COLOR_BG_YELLOW='\033[43m'
COLOR_BG_BLUE='\033[44m'
COLOR_BG_VIOLET='\033[45m'
COLOR_BG_SKY_BLUE='\033[46m'
COLOR_BG_GRAY='\033[47m'

COLOR_RESET='\033[0m'
#===============================End colors========================================

#============================For docker============================================
RUN="docker exec -it"
INTERPRETATOR="python3"
CONTAINER="base_flask_api"

RUN_CONTAINER="$RUN $CONTAINER"
MANAGER_PY="$RUN_CONTAINER $INTERPRETATOR manage.py"
