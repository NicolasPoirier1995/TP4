import os

# Define the known good and bad commits
bad_commit = "c1a4be04b972b6c17db242fc37752ad517c29402"  # Update with your bad commit
good_commit = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"  # Update with your good commit

# Start bisecting
os.system(f"git bisect start {bad_commit} {good_commit}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
