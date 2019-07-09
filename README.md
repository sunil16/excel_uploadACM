# Find latitude and longitude

find Lat and Lng is a django application where you can upload excel file, which conatinas address, after process you can download resultant excel along with Lat and Lng.

  - upload excel
  - wait for result
  - download resultant excel along latitude and longitude

#### Sample Excel file

[See](https://github.com/sunil16/excel_uploadACM/blob/master/static/demo.xlsx) [DOWNLOAD](https://github.com/sunil16/excel_uploadACM/raw/master/static/demo.xlsx)
### Tech

Find Lat and Lng uses a number of open source projects to work properly:

* [Python] - Python is an interpreted, high-level, general-purpose programming language.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps.
* [jQuery] - jQuery is a fast, small, and feature-rich JavaScript library.
* [Geopy] - geopy is a Python 2 and 3 client for several popular geocoding web services.
* [Pandas] - pandas is a software library written for the Python programming language for data manipulation and analysis.

And of course Find Lat and Lng itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Find Lat and Lng requires [Django](https://www.djangoproject.com/download/) v1.8.4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd excel_uploadACM
$ pip install -r requirements.txt
$ python manage.py runserver

```
Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://127.0.0.1:8000/excel/upload/
```

### API Endpoints

#### Uploads

* **/excel/upload/** (Excel upload endpoint)


License
----

MIT


**Free Software

   [dill]: <https://github.com/sunil16/excel_uploadACM.git>
   [git-repo-url]: <https://github.com/sunil16/excel_uploadACM.git>
   [Python]: <https://www.python.org/>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [Geopy]: <https://geopy.readthedocs.io/en/stable/>
   [Pandas]: <https://github.com/pandas-dev/pandas/blob/master/README.md>



   
