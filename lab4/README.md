# Lab 4 - Django and Flask
For this Lab, we are learning the basics of Django which is a, "..free and open-source, Python-based web framework that runs on a web server[(1)](https://en.wikipedia.org/wiki/Django_(web_framework)). I am once again using the Ubuntu Linux environment to run the software in absence of a Linux terminal on my Windows desktop. All the steps to download the software can be learned from this [repo](https://github.com/django/django). In this lab, I also worked with a Flask which is a "...lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications." [(2)](https://palletsprojects.com/projects/flask/). I have only uploaded the part 3 folder since I do not want to compromise my API keys and Django keys.

## Django Tutorial
To prepare myself for the lab I followed the tutorials found in this [repo](https://github.com/django/django/blob/main/docs/intro/tutorial01.txt). This started by creating a new project folder and then linking it to the Django framework.  
After successfully setting up my server and running it. I got this message:  
![ROCKET SUCESS](https://github.com/user-attachments/assets/6d724090-68ff-4d85-a2f5-5dfa8c7082a6)

After editing the Python files in the Visual Studio code editor. I was able to link my first site and display the message inside of the code:  
![Success](https://github.com/user-attachments/assets/b344a995-6320-46b8-a169-dc95df80bba4)

# Lab 4 part 1 Running 'Stevens'
This tutorial came from the class [repo](https://github.com/kevinwlu/iot/tree/master/lesson4). Following these directions, I was able to create the site and access the login page here.  
![Login Screen](https://github.com/user-attachments/assets/5c1a0bd3-8428-4dbe-a4b1-f50611be51fd)

After logging into the site, I was able to add the temperature data from today into the database.  

![Adding temp data](https://github.com/user-attachments/assets/147358f8-363e-4d05-be5e-45241d3c510a)

Then I was finally able to view the final website with the Google Maps attached via an API key.  
![final website](https://github.com/user-attachments/assets/39a82a22-5e0d-4632-b7fe-413d757e9a7f)

`Console Log lab4 part 1`
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

# Lab 4 Part 2 Running MyCPU
This project also came from the class [repo](https://github.com/kevinwlu/iot/tree/master/lesson4). I followed the steps that were posted there to run the 'MyCPU' REST project. For starting the Django app I used python3 instead of python for my environment.:
`Changed input`
```sh
~/mycpu $ python3 manage.py startapp myapp
```
I also decided to change all the passwords to 'ubuntu' in both of the files requested for ease of use. For creating the migrations for the site I used these options, most notably using 'python3' instead of 'python':  
`Migration`
```sh
ubuntu@ubuntu:~/shared/lab4/mycpu$ python3 manage.py makemigrations myapp
Migrations for 'myapp':
  myapp/migrations/0001_initial.py
    + Create model Cpu
    + Create model Dt
    + Create model LocationData
    + Create model Mem
ubuntu@ubuntu:~/shared/lab4/mycpu$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying myapp.0001_initial... OK
  Applying sessions.0001_initial... OK
ubuntu@ubuntu:~/shared/lab4/mycpu$ python3 manage.py createsuperuser
Username (leave blank to use 'ubuntu'): 
Email address: mwerner3@stevens.edu
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

After running the site from the terminal I was able to log into the site at the address http://127.0.0.1:8000/admin/:  
![logged in](https://github.com/user-attachments/assets/716a936c-a76d-4a43-b647-18d192bc99c0)

Adding the Location data successfully I was greeted with this message:  
![Success](https://github.com/user-attachments/assets/1c54f44f-6e5d-4ac2-a91b-951b308274a7)

The final part of the tutorial had me post these three values to the corresponding address.     
![DT list](https://github.com/user-attachments/assets/da345e39-25a1-4fdb-92c9-118cb1ef10ab)
![CPU list](https://github.com/user-attachments/assets/c3b0be54-4abb-4976-9e3f-8089fa98c8f9)
![mem list](https://github.com/user-attachments/assets/769e90f0-e62b-4f75-a508-0ef8783f94be)

After running the controller.py in another window. I was able to view the website and the data.  
![Success](https://github.com/user-attachments/assets/bd90b072-e909-4516-99a9-a1d58a8e16ec)

The console log from the Django server is as follows:  
`Console Log lab4 part 2`
```sh
ubuntu@ubuntu:~/shared/lab4/mycpu$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 25, 2025 - 15:08:01
Django version 5.1.6, using settings 'mycpu.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[25/Feb/2025 15:08:16] "GET /admin/ HTTP/1.1" 302 0
[25/Feb/2025 15:08:16] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4165
[25/Feb/2025 15:08:21] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[25/Feb/2025 15:08:21] "GET /admin/ HTTP/1.1" 200 6714
[25/Feb/2025 15:08:21] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[25/Feb/2025 15:08:21] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[25/Feb/2025 15:08:25] "GET /admin/login/?next=/admin/ HTTP/1.1" 302 0
[25/Feb/2025 15:08:25] "GET /admin/ HTTP/1.1" 200 6714
[25/Feb/2025 15:08:26] "GET /admin/ HTTP/1.1" 200 6714
[25/Feb/2025 15:08:32] "GET /admin/ HTTP/1.1" 200 6714
[25/Feb/2025 15:09:59] "GET /admin/myapp/locationdata/add/ HTTP/1.1" 200 9942
[25/Feb/2025 15:09:59] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[25/Feb/2025 15:10:28] "POST /admin/myapp/locationdata/add/ HTTP/1.1" 302 0
[25/Feb/2025 15:10:28] "GET /admin/myapp/locationdata/ HTTP/1.1" 200 9379
[25/Feb/2025 15:10:28] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[25/Feb/2025 15:10:28] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[25/Feb/2025 15:10:28] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[25/Feb/2025 15:11:36] "GET /dt HTTP/1.1" 301 0
[25/Feb/2025 15:11:36] "GET /dt/ HTTP/1.1" 200 8939
[25/Feb/2025 15:11:36] "GET /static/rest_framework/css/prettify.css HTTP/1.1" 200 817
[25/Feb/2025 15:11:36] "GET /static/rest_framework/css/default.css HTTP/1.1" 200 1152
[25/Feb/2025 15:11:36] "GET /static/rest_framework/css/bootstrap-tweaks.css HTTP/1.1" 200 3426
[25/Feb/2025 15:11:36] "GET /static/rest_framework/js/ajax-form.js HTTP/1.1" 200 3796
[25/Feb/2025 15:11:36] "GET /static/rest_framework/js/csrf.js HTTP/1.1" 200 1793
[25/Feb/2025 15:11:36] "GET /static/rest_framework/js/default.js HTTP/1.1" 200 1268
[25/Feb/2025 15:11:36] "GET /static/rest_framework/js/prettify-min.js HTTP/1.1" 200 13632
[25/Feb/2025 15:11:36] "GET /static/rest_framework/js/bootstrap.min.js HTTP/1.1" 200 39680
[25/Feb/2025 15:11:36] "GET /static/rest_framework/css/bootstrap.min.css HTTP/1.1" 200 121457
[25/Feb/2025 15:11:36] "GET /static/rest_framework/js/jquery-3.7.1.min.js HTTP/1.1" 200 87533
[25/Feb/2025 15:11:36] "GET /static/rest_framework/js/load-ajax-form.js HTTP/1.1" 200 59
[25/Feb/2025 15:11:36] "GET /static/rest_framework/img/grid.png HTTP/1.1" 200 1458
[25/Feb/2025 15:12:00] "POST /dt/ HTTP/1.1" 201 9235
[25/Feb/2025 15:12:13] "GET /cpu HTTP/1.1" 301 0
[25/Feb/2025 15:12:13] "GET /cpu/ HTTP/1.1" 200 8957
[25/Feb/2025 15:12:19] "POST /cpu/ HTTP/1.1" 201 9253
[25/Feb/2025 15:12:48] "GET /mem HTTP/1.1" 301 0
[25/Feb/2025 15:12:48] "GET /mem/ HTTP/1.1" 200 8957
[25/Feb/2025 15:12:56] "POST /mem/ HTTP/1.1" 201 9253
[25/Feb/2025 15:13:12] "GET /admin/ HTTP/1.1" 302 0
[25/Feb/2025 15:16:28] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:16:29] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:16:29] "PUT /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:16:39] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:16:40] "PUT /mem/1/ HTTP/1.1" 200 65
[25/Feb/2025 15:16:40] "PUT /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:16:50] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:16:51] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:16:52] "PUT /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:17:02] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:03] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:03] "PUT /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:17:14] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:14] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:14] "PUT /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:17:19] "GET /home HTTP/1.1" 301 0
[25/Feb/2025 15:17:19] "GET /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:20] "GET /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:20] "GET /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:17:20] "GET /home/ HTTP/1.1" 200 1649
[25/Feb/2025 15:17:20] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 200 60356
[25/Feb/2025 15:17:20] "GET /static/myapp/jquery.min.js HTTP/1.1" 200 87464
[25/Feb/2025 15:17:20] "GET /static/myapp/bootstrap.min.css HTTP/1.1" 200 232920
[25/Feb/2025 15:17:25] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:25] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:25] "PUT /cpu/1/ HTTP/1.1" 200 52
[25/Feb/2025 15:17:32] "GET /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:32] "GET /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:33] "GET /cpu/1/ HTTP/1.1" 200 52
[25/Feb/2025 15:17:33] "GET /home/ HTTP/1.1" 200 1650
[25/Feb/2025 15:17:33] "GET /static/myapp/jquery.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:17:33] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:17:36] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:37] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:37] "PUT /cpu/1/ HTTP/1.1" 200 52
[25/Feb/2025 15:17:44] "GET /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:44] "GET /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:45] "GET /cpu/1/ HTTP/1.1" 200 52
[25/Feb/2025 15:17:45] "GET /home/ HTTP/1.1" 200 1650
[25/Feb/2025 15:17:45] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:17:45] "GET /static/myapp/jquery.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:17:48] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:49] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:49] "PUT /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:17:55] "GET /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:56] "GET /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:17:57] "GET /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:17:57] "GET /home/ HTTP/1.1" 200 1649
[25/Feb/2025 15:17:57] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:17:57] "GET /static/myapp/jquery.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:18:00] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:00] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:01] "PUT /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:18:08] "GET /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:08] "GET /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:09] "GET /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:18:09] "GET /home/ HTTP/1.1" 200 1649
[25/Feb/2025 15:18:09] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:18:09] "GET /static/myapp/jquery.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:18:12] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:12] "PUT /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:13] "PUT /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:18:20] "GET /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:21] "GET /mem/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:21] "GET /cpu/1/ HTTP/1.1" 200 51
[25/Feb/2025 15:18:21] "GET /home/ HTTP/1.1" 200 1649
[25/Feb/2025 15:18:21] "GET /static/myapp/jquery.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:18:21] "GET /static/myapp/bootstrap.min.js HTTP/1.1" 304 0
[25/Feb/2025 15:18:23] "PUT /dt/1/ HTTP/1.1" 200 66
[25/Feb/2025 15:18:24] "PUT /mem/1/ HTTP/1.1" 200 65
[25/Feb/2025 15:18:24] "PUT /cpu/1/ HTTP/1.1" 200 51
```
#Lab 4 Part 3 Running 'hello_world.py'
Following the instructions on this [website](https://flask.palletsprojects.com/en/stable/installation/) I was able to download [Flask](https://palletsprojects.com/projects/flask/). Running the file with the following commands I was able to get the text to display on the website:  
![Flask](https://github.com/user-attachments/assets/d94e5cca-c3ab-4395-a50c-4ee9d051f956)

The console log for the server looked like this:  
`Console Log lab4 part2`
```sh
ubuntu@ubuntu:~/shared/lab4/helloworld$ python3 hello_world.py 
 * Serving Flask app 'hello_world'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [25/Feb/2025 15:28:30] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [25/Feb/2025 15:28:30] "GET /favicon.ico HTTP/1.1" 404 -
```




