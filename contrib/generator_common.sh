if test -f "/opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar"
then
    OPENAPI_GENERATOR="java -jar /opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar"
    WORK_PATH="${THIS_DIR}/.."
else
    echo "Using docker-based generator (dev-mode)..."
    OPENAPI_GENERATOR="docker run --rm=true -u $(id -u):$(id -g) -v ${THIS_DIR}/..:/tmp/schema openapitools/openapi-generator-cli:v5.2.1"
    WORK_PATH=/tmp/schema
fi

THIS_WORK_PATH="${WORK_PATH}/$(basename ${THIS_DIR})"
