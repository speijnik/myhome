#!/bin/bash

set -eu
set -o pipefail

THIS_PATH=$(readlink -f $0)
THIS_DIR=$(dirname ${THIS_PATH})

source "${THIS_DIR}/generator_common.sh"

echo "Removing old generated API docs..."
rm -rf "${THIS_DIR}/../doc/api"
mkdir -p "${THIS_DIR}/../doc/api"

echo "Generating API docs..."
${OPENAPI_GENERATOR} generate \
		     -g markdown \
		     -c "${THIS_WORK_PATH}/.openapi_codegen_docs.yml" \
		     -i "${THIS_WORK_PATH}/openapi.yml" \
		     -o "${WORK_PATH}/doc/api"
