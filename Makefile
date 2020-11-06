SHELL       := /bin/bash
MAKEFLAGS   += --no-print-directory

.DEFAULT_GOAL := all

.SILENT       : run clean update

PRJ_ROOT   := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
ENTRYPOINT := pysleuth

define banner
	@echo -e "************************************************************\n"
	@echo -e "\tPySleuth : $(1)\n"
	@echo -e "************************************************************\n"
endef

all: run clean

run:
	$(call banner,Run)
	source ${PRJ_ROOT}/venv/bin/activate && \
	python ${ENTRYPOINT}

clean:
	$(call banner,Cleanup)
	py3clean ${PRJ_ROOT}

update:
	$(call banner,Update)
	source ${PRJ_ROOT}/venv/bin/activate && \
	pip freeze -l > ${PRJ_ROOT}/requirements.txt
	git add ${PRJ_ROOT}/requirements.txt
	git commit -m "[update] requirements.txt"

format:
	$(call banner,Format - AutoPEP8)
	find pysleuth -type f -name "*.py" | xargs autopep8 --in-place
