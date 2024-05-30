### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
~ an open source program that can create and modify SQL databases

- What is the difference between SQL and PostgreSQL?
~ SQL: language for querying 
~ PostgreSQL: program that we access databases through

- In `psql`, how do you connect to a database?
~ depending where you connect from either psql db_name OR c db_secondname

- What is the difference between `HAVING` and `WHERE`?
~ having is used to return rows that meet a specific condition
~ WHERE filters through each row 

- What is the difference between an `INNER` and `OUTER` join?
~ INNER joins will return data that both tables you are joining have in common
~ OUTER will also return the data that is not common

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
~ returns all records of specified join, and the matched data of the other.
~ for instance, LEFT OUTER would return all data from the left table

- What is an ORM? What do they do?
~ Object Relational Mapping, it provides a means to easily access data from a database by generating objects from that data that then can be easily manipulated in programming.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  ~ Client side AJAX requests include JavaScript and are useful for retrieving data from API's to quickly present information on the screen while server side requests allow data retrieval from things like forms that interact with our databases.

- What is CSRF? What is the purpose of the CSRF token?
CSRF stands for Cross-site request forgery, a token with this abbreviation is a secret unique value that is assigned in order to prevent cyber related attacks or hacks.


- What is the purpose of `form.hidden_tag()`?
This is a hidden area of an application that includes the CSRF token to prevent said cyber attacks.
