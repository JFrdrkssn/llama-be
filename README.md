<h1 align="center" style="font-size: 250%;"><b>
llAMA API
</b></h1>

llAMA API is a fully functional API built specifically for the [llAMA](https://github.com/JFrdrkssn/llama) frontend application.

Users can register an account to access full CRUD functionality for different interactions across the site.
Permissions are set for handling restricted access on the frontend application.

[Link to deployed API](https://llama-drf-api.herokuapp.com/).

<br/><br/>

# **Data Model**

<br/>

The backend API application is built with Django REST Framework.

<br/>

## ERD

![ERD](media/screenshots/erd.png "ERD")
<br/><br/>

## User Model (AllAuth)

- ID of User is linked via a ForeignKey relation in the Post Model owner field.
- ID of User is linked via a OneToOne relation in the Profile Model owner field.
- ID of User is linked via a ForeignKey relation in the Follower Model owner field.
- ID of User is linked via a ForeignKey relation in the Follower Model followed field.
- ID of User is linked via a ForeignKey relation in the Comment Model owner field.
- ID of User is linked via a ForeignKey relation in the Like Model owner field.
  <br/><br/>

## Post Model

- ID of Post is linked via a ForeignKey relation in the Comment Model post field.
  <br/><br/>

## Category Model

- ID of Category is linked via a ForeignKey relation in the Post Model category field.
  <br/><br/>

## Database

- SQLite is used in delevopment to store data.
- PostgreSQL is used in production to store data.

<br/><br/>

The Category model has not been fully completed and implemented and is therefore not currently used for the frontend application.

<br/><br/>