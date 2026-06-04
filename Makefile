# .PHONY: help build run test clean

# PYTHON=python3
# VENV=.venv
# DOCKER_IMAGE=gostra:latest

# help:
# 	@echo "Targets:"
# 	@echo "  build       Install dependencies and optionally build Docker image"
# 	@echo "  run         Run FastAPI locally"
# 	@echo "  test        Run all unit tests"
# 	@echo "  clean       Remove caches and __pycache__"

# # Build virtualenv and install flattened requirements
# build:
# 	$(PYTHON) -m venv $(VENV)
# 	$(VENV)/bin/pip install --upgrade pip
# 	$(VENV)/bin/pip install -r requirements.txt

# # Run FastAPI locally
# run:
# 	$(VENV)/bin/uvicorn gostra.interfaces.main:app --reload --host 0.0.0.0 --port 8000

# # Run all tests
# test:
# 	$(VENV)/bin/pytest -v tests/

# clean:
# 	find . -name "__pycache__" -type d -exec rm -rf {} +
# 	find . -name ".pytest_cache" -type d -exec rm -rf {} +
# 	rm -rf $(VENV)

APP=gostra-gui

.PHONY: build export run clean offline

build:
	@./build/build.sh

offline:
	@OFFLINE=1 ./build/build.sh

export:
	@mkdir -p artifacts

run:
	@sudo podman run --rm -p 8000:8000 $(APP):1.0

clean:
	@sudo buildah rm -a || true
	@rm -rf /tmp/gostra-build artifacts
