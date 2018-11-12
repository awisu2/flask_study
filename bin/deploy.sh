#!bin/bash

# change directory project
DIR=$(dirname ${0})
cd "${DIR}/.."

MODE="update"
if [ "${1}" != "" ]; then
  MODE="${1}"
fi

# create venv
create_venv() {
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
}

# clear venv
clear_venv() {
  deactivate
  rm -rf venv
}

run() {
  MODE=${1}
  create_venv
  zappa "${MODE}"
  clear_venv
}

# deploy
case "${MODE}" in
  "deploy" ) run "deploy" ;;
  "update" ) run "update" ;;
  "undeploy" ) run "undeploy" ;;
  "*" ) echo "deploy, update, undeployのいずれかを指定してください。(default: update)";;
esac

exit 0