## workato-training-skills-and-mcp-tools pipeline
## Run from the repo root: make <target>

REPO_ROOT := $(shell git rev-parse --show-toplevel)
SKILL_PACKAGES := $(HOME)/code/skill-packages
PYTHON := python3

.PHONY: help build test sync deploy-skills deploy-mcp

help:
	@echo "Targets:"
	@echo "  build          Rebuild all skill zips + say-it-plain projection"
	@echo "  test           Run pillar regression tests"
	@echo "  sync           Run full sync pipeline (dry run)"
	@echo "  deploy-skills  Gate 1: push skill distro to GitHub + Confluence"
	@echo "  deploy-mcp     Gate 2: push to Workato + re-assign MCP tools"

build:
	@echo "Building skill zips..."
	cd $(SKILL_PACKAGES) && \
	mkdir -p dist/skills dist/bundles && \
	for skill in addie-plan file-workato-product-bug generate-kahoot the-once-over the-tape wow-plan; do \
	  zip -qr "dist/skills/$${skill}.zip" "$${skill}/" -x "*.DS_Store"; echo "  $$skill ✓"; \
	done
	@echo "Building say-it-plain projection..."
	cd $(SKILL_PACKAGES) && \
	mkdir -p say-it-plain && \
	cp the-once-over/pillars/say-it-plain.md say-it-plain/SKILL.md && \
	$(PYTHON) pipeline/build_projection.py && \
	zip -qr dist/skills/say-it-plain.zip say-it-plain/ -x "*.DS_Store" && rm -rf say-it-plain
	@echo "Building plugin bundles..."
	cd $(SKILL_PACKAGES) && \
	for plugin in workato-trainer-skills workato-education-skills workato-skills; do \
	  rm -f "dist/bundles/$${plugin}.zip"; \
	  (cd plugins && zip -qr "../dist/bundles/$${plugin}.zip" "$${plugin}/" -x "*.DS_Store"); \
	  echo "  $$plugin ✓"; \
	done
	@echo "✅ Build complete"

test:
	$(PYTHON) $(REPO_ROOT)/mcp/standards-desk/cli/sync_pipeline.py --stage test

sync:
	$(PYTHON) $(REPO_ROOT)/pipeline/sync_pipeline.py --check

deploy-skills:
	$(PYTHON) $(REPO_ROOT)/pipeline/sync_pipeline.py --gate skills

deploy-mcp:
	$(PYTHON) $(REPO_ROOT)/pipeline/sync_pipeline.py --deploy mcp
