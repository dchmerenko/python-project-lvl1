build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

install:
	poetry install

brain-calc:
	poetry run brain-calc

brain-even:
	poetry run brain-even

brain-games:
	poetry run brain-games

brain-prime:
	poetry run brain-prime

brain-progression:
	poetry run brain-progression

lint:
	poetry run flake8 brain_games
