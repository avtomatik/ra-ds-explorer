build:
	./ci/build/docker_build.sh
	
test:
	./ci/test/unit.sh
	
integration:
	./ci/test/integration.sh
	
lint:
	./ci/test/lint.sh
	
export:
	./ci/artifact/export_docker_tar.sh
	
release:
	./ci/release/tag_release.sh
