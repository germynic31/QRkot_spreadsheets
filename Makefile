.PHONY: lint
lint:
	flake8
	isort -qc .


.PHONY: cm
cm:
	alembic revision --autogenerate -m "$(msg)"

msg:
	@echo "Введите комментарий для миграции:"
	@read comment; \
	echo $comment


.PHONY: migrate
cm:
	alembic upgrade head
