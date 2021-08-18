# scripts

we use pure sql for talking to database (at least, in creating that), and the purpose of this directory is
to maintain all the sql commands at a place.

although for simplicity we are tended to use sqlalchemy query builder api for getting data, but sometimes
some queries may handle here in raw sql format.

## folder structure

there are 2 main directory:

1. `ddl` which contains all the scripts related to creating and updating tables. 
   commands like `create`, `alter`, etc.
   

2. `dml` which contain all the scripts related to DQL and DML (Data Query-Manipulation Language) in SQL. 
   commands like `select`, `update`, `insert`, `delete`, etc.