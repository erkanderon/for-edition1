# online.learning.turkiye

Django projesini çalıştırabilmek için 3 toola ihtiyaç var.

python 3.6.6 -> 3.5 ve üzeri iş görür (3 üzeri bile iş görebilir)

pip -> python package management tool. Thirt party library yükleyecekseniz pip install <package-name> şeklinde çalışır. Yine pip versiyonu 3.6 olmalı 3.5 üzeri iş görür. pip --versiyon yazdığında 3.6 şeklinde göstermeli yada pip3.6 şeklinde kullanılabiliyor terminalde. Yani bir paket yükleyeceğin zaman pip3.6 install <package-name> yazmak gerekir. 

	Ubuntu install -> sudo apt-get install python3-pip

virtualenv (Şart değil) -> Çok basit bir comman line tool. İşletim sistemine izolasyon yapıyor. Yani third party paketleri OS üzerinde yüklü olan library yerine oluşturduğun environment klasöründen çekiyor. Örnek: sistemde python versiyonun 2.7 diyelim, virtualenv aktif iken python versiyon 3.6ysa sen python la birşey çalıştırmak istersen 3.6 olan ile çalıştırıyor. Deaktif ise 2.7 ile. Aynı şekilde virtualenv aktif iken pyqt paketi yüklediysen, deaktif olduğunda yüklü olmuyor :)

	Yeni bir virtualenv yaratmanız gerekiyor 1 seferlik -> virtualenv -p python3 myenv -> çalıştırdığın yerde myenv klasörü altına izole bir environment yaratıyor.  Git içerisinde tutmayın :D

	aktif hale getirmek için -> source myenv/bin/activate
	deaktif hale getirmek için -> deactivate

requirement.txt içerisinde env içine yüklenmesi gereken libraryler var.

	Kısa yolu -> pip3.6 install -r requirement.txt
	Uzun yolu -> pip3.6 install <package name>

	Eğer ekstra bir paket yüklerseniz ENV AKTİF İKEN pip freeze > requirement.txt şeklinde yeniden generate edebilirsiniz.


DJANGO

MVC Framework

Django da built in User modeli tanımlıdır.

Proje oluşturma -> django-admin startproject <project-name>

Yeni bir model eklerseniz ya da değiştirirseniz, bunu DBye tanımlamak için 2 command kullanıyoruz.

	Model değişikliğini algılar -> python manage.py makemigrations
	DB'ye enjekte eder -> python manage.py migrate

	Projeyi ilk oluşturduğunda 1 kez yapabilirsin, built-in User modelini enjekte eder. -> manage.py hiyerarşisine db.sqlite oluşturur.

	User modelini enjekte ettikten sonra -> python manage.py createsuperuser
	ile bir admin user oluşturabilirsiniz.

Run etmek için -> python manage.py runserver (8000)

manage.py -> Django uygulamasını comman line ile yönettiğin dosya.
setting.py -> Django ile ilgili bütün konfigürasyonların tutulduğu yer.

views.py -> modellerle render edilen sayfaya hangi dataları gönderceksin, logiclerin olduğu yer.
url.py -> Urllerin hangi viewlarla hangi url de çalışması gerektiğini define ettiğin yer.
models.py -> Modelleri tanımladığın dosya, şuanda boş doc dan örnek bakabilirsiniz. DB Table gibi modeller oluşturuyorsun.
admin.py -> Object Relation Mapping sayesinde admin panelini Django kendisi oluşturur :) bu dosyada hangi modeli panele eklemek istersen ekleyebiliyorsun.

UYGULAMAYI ÇALIŞTIRMAK İÇİN

Uygulamayı clone edip, virtualenv oluşturup aktif edip, pip install Django ile Djangoyu yükleyip, manage.py hiyerarşisinde python manage.py runserver yapmalısınız.


Yoruldum kankalar :D eksik anlatmadım diye düşünüyorum ama bir problem olursa arayıp sorun :D



