#!bin/bash

# echo help information
help() {
  cat << EOF
Usage: bin/migrate.sh COMMAND ...

  Available commands:
    upgrade           - upgrade by migrate file
    downgrade VERSION - downgrade for specific versioin
EOF
}

# get args
if [ "${1}" = "" ]; then
  help
  exit 0
fi

MODE="${1}"
ARG2="${2}"

upgrade() {
  python manage.py version_control
  python manage.py upgrade
}

downgrade() {
  VERSION="${1}"
  if [ "${VERSION}" = "" ]; then
    help
    exit 0
  fi

  python manage.py downgrade ${VERSION}
}

# change directory project
DIR=$(dirname ${0})
cd "${DIR}/../migrate"

# deploy
case "${MODE}" in
  "upgrade" ) upgrade ;;
  "downgrade" ) downgrade "${ARG2}" ;;
  * ) help;;
esac

exit 0
