# online.learning.turkiye


	$> sudo docker build -t online.learning:latest .
	$> sudo docker-compose build
	$> sudo docker-compose run app sh -c "python manage.py makemigrations"
	$> sudo docker-compose run app sh -c "python manage.py migrate"
	$> sudo docker-compose run app sh -c "python manage.py createsuperuser"
	$> sudo docker-compose up

Say Hello to Docker :)


# docker hints


	$> docker rmi $(docker images -q)
	$> docker-compose down