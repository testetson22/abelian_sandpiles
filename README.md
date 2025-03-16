# Abelian sandpiles 
Simulates gravity being applied to a sandpile per the Abelian sandpile model. Simple implemention; may have some bugs with large sand piles.

## Run CLI
- Install: `bash ./setup.sh`
- Run: `sandpiles x y z` where `x` and `y` are the dimensions of a 2D array and `z` is the height of a center pile of sand.

## Run Tests
### Locally
Run : `pytest --cov=sandpiles tests/` from repository root
### GitHub Actions
1. `Run Pytest w/ linting and coverage`
2. `Demo Sandpiles Module CLI`


## TODO 
- matplotlib visuals
- Integrate with a Flask App