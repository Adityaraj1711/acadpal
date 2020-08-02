# AcadPal Django Backend Assignment
### Project Features
- API backend for an application with the following entity relation table given in the below diagram. Appropriate relational ﬁelds has been used to relate Person to one of the City/ Town objects.
- APIs for Creation, reading, editing and deleting (CRUD) for all of the entities, with the DRF’s APIView’s get, post, put, delete methods
-  DRF’s serialisers for all the CRUD operations.
-  CRUD API for Country. Representation like dictionary of Cities inside the states of the country.
- Added people of the Person class to City and Town.
- Pagination API to list all the Persons from the database. With ﬁltering based on City, Town, State and Country.
-  For all API’s return DRF’s Response object with appropriate http status codes. Handling of cases of invalid data, duplicate entry for the same Country, State, City/Town object has been taken care.




## License
[MIT](https://choosealicense.com/licenses/mit/)