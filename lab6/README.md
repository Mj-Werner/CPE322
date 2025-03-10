# Lab 6 - Node.js and Pystache
In this lab we made use of [Node.js](https://nodejs.org/en/about) and [Pystache](https://github.com/defunkt/pystache) to view basic use cases about them.
---
## Node.js - [hello-world.js](hello-world.js)
This was a very simple code to run and use. It displays "Hello, World!" on the specified IP.   
`hello-world.js`
```sh
$ node hello-world.js 
Server running at http://127.0.0.1:3000/
```
After going to the IP specified it looked like the following:
![hello-world.js-running](https://github.com/user-attachments/assets/ad550d7c-1ff7-45fd-a2f3-2755ea73432c)


## Node.js - [hello.js](hello.js)
This code is slightly different than the previous one. After refreshing the page in the browser, the terminal shows updates. This was not present in the "hello-world.js" file and is what separates the 
two codes.
`hello.js`
```sh
$ node hello.js
Server running at http://127.0.0.1:8080/
response end call done
request end event fired
response end call done
request end event fired
```
The "response end call done" and "request end event fired" messages appeared after refreshing the browser and after it finished refreshing, respectively.
![hello.js running](https://github.com/user-attachments/assets/87472499-a78f-41ee-9c36-11721dfbfba9)



## Node.js - [http.js](http.js)
This code is different than the rest of the ones that I have run thus far. This code will display the number of times that the page was refreshed. This is achieved by writing to the [test.txt](test.txt) text file,
the number of times that the page has been refreshed to "save" the change and remember it. The picture shows the text file with "6" written inside after the page was refreshed 6 times. 
This also means that these refresh values will stay the same from running the code at different times.
`https.js`
```sh
$ node http.js 
0

1
2
3
4
5
```
![https runnning](https://github.com/user-attachments/assets/608a5886-df7b-4687-b697-07c540fcc485)

## Pystache - say_hello.mustache say_hello.py
This part of the lab showcases, "[Pystache](http://defunkt.github.com/pystache) is a Python
implementation of [Mustache](http://mustache.github.com/). Mustache is a
framework-agnostic, logic-free templating system inspired by
[ctemplate](http://code.google.com/p/google-ctemplate/) and
[et](http://www.ivan.fomichev.name/2008/05/erlang-template-engine-prototype.html).
Like ctemplate, Mustache "emphasizes separating logic from presentation:
it is impossible to embed application logic in this template language." "

`say_hello.py`
```sh
$ python3 say_hello.py 
Hi Alexa!
Hello, World!

['Hey ', _SectionNode(key='who', index_begin=12, index_end=18, parsed=[_EscapeNode(key='.'), '!'])]
Hey Google!
Hey Siri!
```


