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

# **Agile**

<br/>

## **Project Goals**

<br/>

The general goal of this project is to build a custom backend API for the [llAMA](https://github.com/JFrdrkssn/llama) frontend application and expand them in tandem.

The immediate goal of this project was to build a custom backend API for the [llAMA](https://github.com/JFrdrkssn/llama) frontend application. It is fully functional in relation to the needs of the frontend application right now, the primary goal for this project.

<br/>

## **User Stories**

<br/>

  - ### Admin: users

    - As an admin, I can create, edit and delete users. set user permissions and usernames.
    - As an admin, I can set user permissions and usernames.
    <br/><br/>

  - ### Admin: posts

    - As a admin, I can create, edit and delete posts.
    <br/><br/>

  - ### Admin: profiles

    - As an admin, I can create, edit and delete profiles.
    <br/><br/>

  - ### Admin: comments

    - As an admin, I can create, edit and delete comments.
    <br/><br/>

No agile workflow tool is used for this project currently.

<br/><br/>

# **Future Features**

<br/>


## _These features are planned._

- Expand the Category model
  - Expanding the category model and adding additional fields for subcategories etc.
    <br/><br/>
- Expand the Profile model
  - Additional fields for users to add more info about themselves, for example age or job title.
    <br/><br/>
- Image resizing and compression
  - Cloudinary, which is to store images, has an auto-transform function. This would help resize and compress images to prevent them from being too big and slowing down the site.
    <br/><br/>