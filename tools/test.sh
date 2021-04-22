echo "running tests"
. .venv/bin/activate
pytest tests/ --html-report=./tests/report
echo "tests over"