.venv:
	./configure

configure: .venv

run: configure
	.venv/bin/python main.py

clean:
	rm -Rf .venv
