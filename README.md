# AcadPal Django Backend Assignment
### Project Features
- API backend for an application with the following entity relation table given in the below diagram. Appropriate relational ﬁelds has been used to relate Person to one of the City/ Town objects.
- APIs for Creation, reading, editing and deleting (CRUD) for all of the entities, with the DRF’s APIView’s get, post, put, delete methods
-  DRF’s serialisers for all the CRUD operations.
-  CRUD API for Country. Representation like dictionary of Cities inside the states of the country.
- Added people of the Person class to City and Town.
- Pagination API to list all the Persons from the database. With ﬁltering based on City, Town, State and Country.
-  For all API’s return DRF’s Response object with appropriate http status codes. Handling of cases of invalid data, duplicate entry for the same Country, State, City/Town object has been taken care.


## Find Postman API documentation [here](https://documenter.getpostman.com/view/5616249/T1Dv9FKP?version=latest)
<a href="https://documenter.getpostman.com/view/5616249/T1Dv9FKP?version=latest" target="_blank">
    <a href = "https://documenter.getpostman.com/view/5616249/T1Dv9FKP?version=latest"><button style="background-color: #4CAF50; margin: 4px 2px; cursor: pointer; padding: 15px 32px;"> View API Docs</buttom></a>
</a>


### Features that are taken into consideration while building.
- **Backend written using Django Framework** - Django provides simplicity, flexibility, reliability, and scalability. Django has its own naming system for all functions and components
 - **Easy to Customize** - Pluggable and easy to customize emitters, parsers, validators.
 - **Response Handling** - HTTP response handling, content type negotiation using HTTP Accept headers.
 - **Views for request/response** - Clean, simple, views for Resources, using Django's class-based views.
 - **Converting data into valid HTTP request** - Powerful serialization engine using Django's rest framework.
 - **Feature encapsulation** - Django follows a file naming convention to manage the apps and so different feature are group together.

### Models
<p align="center">
    <img src="https://raw.githubusercontent.com/Adityaraj1711/acadpal/master/acadpal.png?raw=true">
</p>
<br>


## License
[MIT](https://choosealicense.com/licenses/mit/)