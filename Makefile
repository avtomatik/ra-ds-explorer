# Makefile for GostRA CI/CD orchestration
# ---------------------------------------
# Targets:
#   make all           → full pipeline (validate, test, build, export)
#   make validate      → repo sanity + lockfile check
#   make test          → unit + integration + lint
#   make build         → docker build
#   make export        → docker save + checksum
#   make sbom          → generate SBOM JSON
#   make release       → tag current commit
# ---------------------------------------

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

VERSION := $(shell $(ROOT_DIR)/ci/release/version.sh)
IMAGE := gostra:$(VERSION)
ARTIFACT_DIR := $(ROOT_DIR)/artifacts
SBOM_DIR := $(ARTIFACT_DIR)/sbom

.PHONY: all validate test build export sbom release

# ------------------------
# Full pipeline
# ------------------------
all: validate test build export sbom

# ------------------------
# Validation
# ------------------------
validate:
	@echo "[STEP] repo sanity check"
	@bash $(ROOT_DIR)/ci/validate/repo_sanity.sh
	@echo "[STEP] lockfile check"
	@bash $(ROOT_DIR)/ci/validate/lock_check.sh

# ------------------------
# Testing
# ------------------------
test: 
	@echo "[STEP] unit tests"
	@bash $(ROOT_DIR)/ci/test/unit.sh
	@echo "[STEP] integration tests"
	@bash $(ROOT_DIR)/ci/test/integration.sh
	@echo "[STEP] lint check"
	@bash $(ROOT_DIR)/ci/test/lint.sh

# ------------------------
# Build Docker image
# ------------------------
build:
	@echo "[STEP] building Docker image $(IMAGE)"
	@bash $(ROOT_DIR)/ci/build/docker_build.sh

# ------------------------
# Export Docker artifact
# ------------------------
export: build
	@echo "[STEP] exporting Docker tar and checksum"
	@bash $(ROOT_DIR)/ci/artifact/export_docker_tar.sh

# ------------------------
# Generate SBOM
# ------------------------
sbom: build
	@echo "[STEP] generating SBOM"
	@bash $(ROOT_DIR)/ci/security/sbom.sh

# ------------------------
# Release tagging
# ------------------------
release:
	@echo "[STEP] tagging release $(VERSION)"
	@bash $(ROOT_DIR)/ci/release/tag_release.sh
