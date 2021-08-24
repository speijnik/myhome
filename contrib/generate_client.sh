#!/bin/bash

set -eu
set -o pipefail

THIS_PATH=$(readlink -f $0)
THIS_DIR=$(dirname ${THIS_PATH})

source "${THIS_DIR}/generator_common.sh"

echo "Removing old generated client..."
rm -rf "${THIS_DIR}/../myhome/_gen"

echo "Generating API client..."
${OPENAPI_GENERATOR} generate \
		     -g python-legacy \
		     -c "${THIS_WORK_PATH}/.openapi_codegen_python.yml" \
		     -i "${THIS_WORK_PATH}/openapi.yml" \
		     -o "${WORK_PATH}"
