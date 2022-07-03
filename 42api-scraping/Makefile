all: init

init: venv install

venv:
	python3 -m venv venv/

install: requirements.txt.lock

%.txt.lock: %.txt
	@( \
		source venv/bin/activate; \
		pip3 install -r $<; \
		cat $< > $@ \
	)

requirements.txt.lock: requirements.txt

run: init
	@( \
		source venv/bin/activate; \
		python main.py \
	)

.PHONY: all init install run
