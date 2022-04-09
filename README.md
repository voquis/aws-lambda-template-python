# AWS Lambda function python template
Opinionated starter repository for creating python Lambda functions that use AWS services.

## Assumptions
This starter repository makes the following assumptions.

### Dependency management
- Poetry is used to manage dependencies and run tasks

This project was initiated with:
```shell
poetry new example --src
```

### Development environment
- A shell-capable environment is available
- Docker is used as the local development environment

### Testing
- pytest is used to run tests with coverage via GitHub Actions

### Build
- GitHub Actions are used to test and produce build artifacts
- A zip bundle is created
- A wheel package is created

## Local development
### Docker
Developing inside a Docker container ensures a consistent experience and more closely matches the final build.

To develop inside a container, first build an image that sets up a limited-privilege user with the following. Note that will run tests and produce builds.

```shell
docker build -t python-lambda .
```

To then develop inside a container using this image, mount the entire project into a container (in addition to the local AWS config directory) with:

```shell
docker run -i -t --rm \
  -v $(pwd):/project \
  -v $HOME/.aws:/home/lambda/.aws:ro \
  python-lambda
```

### Run tests

Change to the lambda directory with:
```shell
cd lambda
```

Install dependencies (including development) and run tests with:
```
../scripts/validate.sh
```
