#!/bin/sh

CUR=$(pwd)

CURRENT=$(cd "$(dirname "$0")" || exit;pwd)
echo "${CURRENT}"

cd "${CURRENT}" || exit
git pull --prune
result=$?
if [ $result -ne 0 ]; then
  cd "${CUR}" || exit
  exit $result
fi

if ! (disable-checkout-persist-credentials); then
  cd "${CUR}" || exit
  exit 1
fi

cd "${CURRENT}/mkpassword" || exit
if ! (cd "${CURRENT}/mkpassword" || exit && uv sync -U); then
  cd "${CUR}" || exit
  exit $result
fi
echo ""
pwd

if ! (cd "${CURRENT}/numpy-matplotlib-example" || exit && uv sync -U); then
  cd "${CUR}" || exit
  exit 1
fi
echo ""
pwd

if ! (cd "${CURRENT}/numpy-pandas-example" || exit && uv sync -U); then
  cd "${CUR}" || exit
  exit 1
fi
echo ""
pwd

cd "${CURRENT}" || exit
result=$?
if [ $result -ne 0 ]; then
  cd "${CUR}" || exit
  exit $result
fi
git pull --prune && git commit -am "Bumps node modules" && git push
result=$?
if [ $result -ne 0 ]; then
  cd "${CUR}" || exit
  exit $result
fi

cd "${CUR}" || exit
