.PHONY: run migrate upgrade downgrade reset

run:
	uvicorn main:app --reload

migrate:
	alembic revision --autogenerate -m "$(m)"

upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade -1

reset:
	alembic downgrade base
	alembic upgrade head
