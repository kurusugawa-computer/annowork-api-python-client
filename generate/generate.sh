#!/bin/bash -ex

DOCKER_IMAGE=openapitools/openapi-generator-cli:v5.2.1

PROGNAME=$(basename $0)

# このスクリプトの存在するディレクトリに移動する
SCRIPT_DIR=$(cd $(dirname $0); pwd)
pushd ${SCRIPT_DIR}



usage_exit() {
        echo "Usage: ${PROGNAME} [--download] [--github_token GITHUB_TOKEN]" 1>&2
        exit 1
}

FLAG_DOWNLOAD=false
GITHUB_TOKEN=""

if [ $# -gt 0 ]; then
    for OPT in "$@"
    do
    case ${OPT} in
        "--download")
            FLAG_DOWNLOAD=true
            shift 1
        ;;
        "--github_token")
            if [ -z "$2" ]; then
                echo "${PROGNAME}: ${1} オプションには値を設定してください" 1>&2
                exit 1
            fi
            GITHUB_TOKEN=$2
            shift 2
        ;;
        "-h" | "--help")
            usage_exit
        ;;
        -*)
            echo "${PROGNAME}: illegal option $1" 1>&2
            exit 1
        ;;
        *)
            if [ -n "$1" ] && [[ ! "$1" =~ ^-+ ]]; then
                echo "${PROGNAME}: illegal parameter $1" 1>&2
                exit 1
            fi
        ;;
    esac
    done
fi


if [[ ${FLAG_DOWNLOAD} == true ]] && [[ -z "${GITHUB_TOKEN}" ]]; then
    echo "${PROGNAME}: '--github_token' を指定してください。" 1>&2
    exit 1
fi

if "${FLAG_DOWNLOAD}"; then
  pushd swagger
  URL_PATH="https://${GITHUB_TOKEN}@raw.githubusercontent.com/kurusugawa-computer/annowork/develop/server/doc"
  curl --fail --remote-name "${URL_PATH}/swagger.yml"
  curl --fail --remote-name "${URL_PATH}/swagger-security-components.yml"
  curl --fail --remote-name "${URL_PATH}/swagger-error-components.yml"
  curl --fail --remote-name "${URL_PATH}/swagger-components.yml"
  popd
fi

# 事前にswagger.yamlから`components.securitySchemes`配下を削除する
sed '/components:/g' swagger/swagger.yml  --in-place
sed '/securitySchemes:/g' swagger/swagger.yml  --in-place
sed '/swagger-security-components.yml/g' swagger/swagger.yml  --in-place


JAVA_OPTS="-Dlog.level=info"

OPENAPI_GENERATOR_CLI_COMMON_OPTION="--generator-name python \
    --output /local/out \
    --type-mappings array=List,DateTime=str,date=str,object=__DictStrKeyAnyValue__"

# apiを生成
docker run --rm   -u `id -u`:`id -g`  -v ${PWD}:/local -w /local  -e JAVA_OPTS=${JAVA_OPTS} ${DOCKER_IMAGE} generate \
    --input-spec swagger/swagger.yml \
    ${OPENAPI_GENERATOR_CLI_COMMON_OPTION} \
    --template-dir /local/template \
    --global-property apis,apiTests=false,apiDocs=false \
    --ignore-file-override=/local/.openapi-generator-ignore 

cat partial-header/generated_api_partial_header.py out/openapi_client/api/*_api.py > ../annoworkapi/generated_api.py
rm -Rf out/openapi_client


# modelsを生成
cat swagger/swagger-partial-header.yml swagger/swagger-components.yml > swagger/swagger-models.yml

docker run --rm   -u `id -u`:`id -g`  -v ${PWD}:/local -w /local -e JAVA_OPTS=${JAVA_OPTS} ${DOCKER_IMAGE} generate \
    --input-spec swagger/swagger-models.yml \
    ${OPENAPI_GENERATOR_CLI_COMMON_OPTION} \
    --template-dir /local/template \
    --global-property ,models,modelTests=false,modelDocs=false \
    --ignore-file-override=/local/.openapi-generator-ignore

cat partial-header/models_partial_header.py out/openapi_client/model/*.py > ../annoworkapi/enums.py
rm -Rf out/openapi_client


sed  -e "s/JA-JP/JA_JP/g" ../annoworkapi/enums.py  --in-place
sed  -e "s/EN-US/EN_US/g" ../annoworkapi/enums.py  --in-place


cd ../

# Format
make format

popd
