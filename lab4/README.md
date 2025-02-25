# Lab 4 - Django and Flask
For this Lab we are learning the basics of Django which is a, "Django (/ˈdʒæŋɡoʊ/ JANG-goh; sometimes stylized as django) is a free and open-source, Python-based web framework that runs on a web server[(1)](https://en.wikipedia.org/wiki/Django_(web_framework)). I am once again using the Ubuntu Linux environment to run the software in absence of a Linux terminal on my windows desktop. All the steps to download the software can be learned from this [repo](https://github.com/django/django). In this lab I also worked with a flask which is a "hjfbnherbnvhnberhv"[2](wiki).

## Django Tutorial
To prepare myself for the lab I followed the tutorials found in this [repo](https://github.com/django/django/blob/main/docs/intro/tutorial01.txt). This started by creating a new project folder and then linking it to the Django framework.
After successfully setting up my server and running it. I got this message:
![ROCKET SUCESS](https://github.com/user-attachments/assets/6d724090-68ff-4d85-a2f5-5dfa8c7082a6)

To edit the Python files in the Visual Studio code editor. I was able to link my first site and display the message inside of the code:
![Success](https://github.com/user-attachments/assets/b344a995-6320-46b8-a169-dc95df80bba4)

# Lab 4 part 1
This tutorial came from the class [repo](https://github.com/kevinwlu/iot/tree/master/lesson4). Following these directions, I was able to create the site and access the login page here.
![Login Screen](https://github.com/user-attachments/assets/5c1a0bd3-8428-4dbe-a4b1-f50611be51fd)

After logging into the site, I was able to add the temperature data from today into the database.

![Adding temp data](https://github.com/user-attachments/assets/147358f8-363e-4d05-be5e-45241d3c510a)

Then I was finally able to view the final website with the Google Maps attached via an API key.
![final website](https://github.com/user-attachments/assets/39a82a22-5e0d-4632-b7fe-413d757e9a7f)

`console log for the website`
```sh
ubuntu@ubuntu:~/shared/lab4/stevens$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 25, 2025 - 14:28:04
Django version 5.1.6, using settings 'stevens.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[25/Feb/2025 14:28:16] "GET /admin HTTP/1.1" 301 0
[25/Feb/2025 14:28:16] "GET /admin/ HTTP/1.1" 302 0
[25/Feb/2025 14:28:16] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4165
[25/Feb/2025 14:28:16] "GET /static/admin/js/theme.js HTTP/1.1" 200 1653
[25/Feb/2025 14:28:16] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3063
[25/Feb/2025 14:28:16] "GET /static/admin/css/login.css HTTP/1.1" 200 951
[25/Feb/2025 14:28:16] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 2804
[25/Feb/2025 14:28:16] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2810
[25/Feb/2025 14:28:16] "GET /static/admin/css/base.css HTTP/1.1" 200 22092
[25/Feb/2025 14:28:16] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17972
[25/Feb/2025 14:28:58] "POST /admin/login/?next=/admin/ HTTP/1.1" 200 4341
[25/Feb/2025 14:29:09] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[25/Feb/2025 14:29:09] "GET /admin/ HTTP/1.1" 200 6825
[25/Feb/2025 14:29:09] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 441
[25/Feb/2025 14:29:09] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[25/Feb/2025 14:29:09] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[25/Feb/2025 14:29:27] "GET /admin/myapp/temperaturedata/add/ HTTP/1.1" 200 10727
[25/Feb/2025 14:29:27] "GET /static/admin/css/forms.css HTTP/1.1" 200 8794
[25/Feb/2025 14:29:27] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[25/Feb/2025 14:29:27] "GET /static/admin/js/core.js HTTP/1.1" 200 6208
[25/Feb/2025 14:29:27] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 9097
[25/Feb/2025 14:29:27] "GET /static/admin/js/actions.js HTTP/1.1" 200 8076
[25/Feb/2025 14:29:27] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[25/Feb/2025 14:29:27] "GET /static/admin/js/urlify.js HTTP/1.1" 200 7887
[25/Feb/2025 14:29:27] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[25/Feb/2025 14:29:27] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 285314
[25/Feb/2025 14:29:27] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 325171
[25/Feb/2025 14:29:27] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[25/Feb/2025 14:29:27] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 586
[25/Feb/2025 14:29:27] "GET /static/admin/css/widgets.css HTTP/1.1" 200 11564
[25/Feb/2025 14:30:29] "POST /admin/myapp/temperaturedata/add/ HTTP/1.1" 302 0
[25/Feb/2025 14:30:29] "GET /admin/myapp/temperaturedata/ HTTP/1.1" 200 9565
[25/Feb/2025 14:30:29] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6878
[25/Feb/2025 14:30:29] "GET /static/admin/js/filters.js HTTP/1.1" 200 978
[25/Feb/2025 14:30:29] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[25/Feb/2025 14:30:29] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[25/Feb/2025 14:30:29] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[25/Feb/2025 14:31:25] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:25] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 200 60356
[25/Feb/2025 14:31:25] "GET /static/myapp/jquery.min.js HTTP/1.1" 200 87464
[25/Feb/2025 14:31:25] "GET /static/myapp/bootstrap.min.css HTTP/1.1" 200 232920
[25/Feb/2025 14:31:55] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:56] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:57] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:57] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:57] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:58] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:58] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:58] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:31:59] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:03] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:05] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:09] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:09] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 304 0
[25/Feb/2025 14:32:09] "GET /static/myapp/bootstrap.min.css HTTP/1.1" 304 0
[25/Feb/2025 14:32:09] "GET /static/myapp/jquery.min.js HTTP/1.1" 304 0
[25/Feb/2025 14:32:10] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:10] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:10] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:11] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:11] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:11] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:36] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:37] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:37] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:37] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:37] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:38] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:38] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:38] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:38] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:38] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:39] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:39] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:39] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:39] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:32:40] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:36:04] "GET /static/myapp/bootstrap.min.css.map HTTP/1.1" 404 1895
[25/Feb/2025 14:38:49] "GET / HTTP/1.1" 200 1538
[25/Feb/2025 14:38:49] "GET /static/myapp/bootstrap.min.css HTTP/1.1" 304 0
[25/Feb/2025 14:38:49] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 304 0
[25/Feb/2025 14:38:49] "GET /static/myapp/jquery.min.js HTTP/1.1" 304 0
```

# Lab 4 part 2
This project also came from the class [repo](https://github.com/kevinwlu/iot/tree/master/lesson4). I followed the steps that were posted there to run the 'MyCPU' REST project.



