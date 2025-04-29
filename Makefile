# Makefile for AI Security Training Lab

IMAGE_NAME=ai-security-training-lab
ENV_FILE=.env
HOST_DIR=$(shell pwd)

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run a script inside the container
run:
	@echo "Running script: $(SCRIPT)"
	docker run --rm --env-file $(ENV_FILE) -v $(HOST_DIR):/app -w /app $(IMAGE_NAME) python3 $(SCRIPT)

# Start an interactive shell
shell:
	docker run --rm --env-file $(ENV_FILE) -v $(HOST_DIR):/app -w /app -it $(IMAGE_NAME) bash
