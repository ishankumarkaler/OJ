if os.environ['USE_DOCKER'] == 'True':
		evaluate_docker(submission)
		return