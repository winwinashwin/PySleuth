SHELL       := /bin/bash
MAKEFLAGS   += --no-print-directory

.DEFAULT_GOAL := all

PRJ_ROOT   := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
ENTRYPOINT := main.py

define banner
	@echo -e "************************************************************\n"
	@echo -e "\tPySleuth : $(1)\n"
	@echo -e "************************************************************\n"
endef

all: run clean

.PHONY: run
.SILENT: run
run:
	$(call banner, "🚀 Run")
	source ${PRJ_ROOT}/venv/bin/activate && \
	python ${ENTRYPOINT}

.PHONY: clean
.SILENT: clean
clean:
	$(call banner, "🧹 Clean")
	py3clean ${PRJ_ROOT}

.PHONY: update
.SILENT: update
update:
	$(call banner, "Update")
	source ${PRJ_ROOT}/venv/bin/activate && \
	pip freeze -l > ${PRJ_ROOT}/requirements.txt
	git add ${PRJ_ROOT}/requirements.txt
	git commit -m "[update] requirements.txt"

.PHONY: format
.SILENT: format
format:
	$(call banner, "✨ Format - AutoPEP8")
	find pysleuth -type f -name "*.py" | xargs autopep8 --in-place
