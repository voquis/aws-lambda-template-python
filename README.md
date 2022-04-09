# AWS Lambda function python template
Opinionated starter repository for creating python Lambda functions.

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
- pytest is used to run unit tests

### Build
- GitHub Actions are used to test and produce build artifacts

### Deployment
- A zip bundle is created and pushed to a publicly accessible AWS S3 bucket
- A public Docker image is created and pushed to AWS public gallery

## Local development
### Docker
Developing inside a Docker container ensures a consistent experience and more closely matches the final build.
To develop inside a container, mount the entire project into a container with:
```shell
docker run public.ecr.aws/lambda/python:3 \
  -i -t --rm  \
  -v $(pwd):/project \
  -w /project \
  bash
```
