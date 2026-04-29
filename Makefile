run:
	uv run streamlit run home.py

install:
	uv sync

add:
	uv add $(pkg)

clean:
	rm -rf .venv

.PHONY: run install add clean
