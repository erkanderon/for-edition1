# online.learning.turkiye


	$> sudo docker build -t online.learning:latest .
	$> sudo docker-compose build
	$> sudo docker-compose run app sh -c "python manage.py makemigrations"
	$> sudo docker-compose run app sh -c "python manage.py migrate"
	$> sudo docker-compose run app sh -c "python manage.py createsuperuser"
	$> sudo docker-compose up

Say Hello to Docker :)


# docker hints


	$> docker rmi $(docker images -q) -f
	$> docker-compose down

quickest way copy paste

	sudo docker rmi $(sudo docker images -q) -f && sudo docker-compose down

	sudo docker build -t online.learning:latest . && sudo docker-compose build && sudo docker-compose run app sh -c "python manage.py makemigrations" && sudo docker-compose run app sh -c "python manage.py migrate" && sudo docker-compose run app sh -c "python manage.py createsuperuser"
--------------------------------------------------------------------------

	$> docker-compose up

ile servisleri ayağa kaldırdıktan sonra -> yeni sekmede aşağıdaki command ile test datalarını yükleyebilirsiniz.

	$> sudo docker-compose run app sh -c "python manage.py loaddata fixtures/sample.yaml"