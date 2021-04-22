echo "deploying on production"
gunicorn -w 1 -b localhost:8001 src:app