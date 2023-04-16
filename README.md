<!-- README Template Source => https://www.grepper.com/tpc/readme+template/273816 -->

# Car Rental System

Car Rental Internal Booking System created using Odoo framework

## Table of Contents

- [Car Rental System](#car-rental-system)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
    - [Task Description](#task-description)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Demo Videos](#demo-videos)
  - [Setup](#setup)
  - [Features to be Added](#features-to-be-added)
  - [Acknowledgements](#acknowledgements)
  - [Contact](#contact)

&nbsp;

## General Information

- Car Rental System is a simple internal car booking system.
- Technical assignment requested by Leading Point Software for practicing
  the Odoo framework after finishing the first 8 chapters from [
  Odoo 14 Development Cookbook - Fourth Edition](https://github.com/PacktPublishing/Odoo-14-Development-Cookbook-Fourth-Edition) book.

### Task Description

> Car Rental System
>
> Build a simple internal (not a website) car booking system using Odoo with basic functionalities mentioned below:
>
> 1.  We will have two kinds of users (groups): managers (have full access - CRUD, and normal users (read-only and can reserve cars).
> 2.  Simple page showing list of available cars to be rented.
> 3.  In car list, user can select car and open a form view to show car details.
> 4.  In form view: show car info and offer a reserve button to reserve the car.
> 5.  Reserve button will record the reserved car, user who did the reservation, and reservation date.
> 6.  From user form view, we need to have a smart button to show the list of reserved cars. Users can do unreserve (store return date).
> 7.  Managers can create, edit, mark cars as damaged, reserve, and unreserve cars (store return date).
> 8.  We will have three states for the car: Available, Rented, and Damaged.
> 9.  Create a page to list all reservation history for each car, the result should be grouped by car, list will have car name, username, state, and date.
> 10. Workflow for return car (second approval).

&nbsp;

## Technologies Used

- [Odoo Framework](https://www.odoo.com/) | An Open Source ERP and CRM.

&nbsp;

## Features

- User can explore the available cars for rent, and see all the car details like name, price, ..etc.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313448-a22ea0d7-e641-4e49-a67f-ec9b6a1e37bd.gif' width='75%'/>
</div>
<br />

- User can reserve the available cars.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313493-03e1f813-dce3-4656-8f40-0f6cfa836115.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313503-f51d17ca-3e22-4106-8eb9-dda8962dd2ab.gif' width='75%'/>
</div>
<br />

- User can explore all his reservation history.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313525-507eb06f-7a7c-493b-90c0-514995be5196.gif' width='75%'/>
</div>
<br />

- User can request to unreserve car.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313531-90e2579d-7d72-4e21-8633-cda2282ef7d2.gif' width='75%'/>
</div>
<br />

- Manager user can create, update, delete the cars.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313556-be4208fa-a195-4acb-aeb3-9dd97e0fed01.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313566-20a0b558-6f96-4393-bbb0-8488766797c9.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313573-ae16d2ac-b2ff-41a6-aa0d-0d2863522d8f.gif' width='75%'/>
</div>
<br />

- Manager user can reserve the cars to users.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313583-8ccfb8d3-8dc5-4b58-99ad-72cec9878635.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313598-432b99c2-ad36-4301-a4c9-bbe162ae7815.gif' width='75%'/>
</div>
<br />

- Manager user can explore all reservation history for all cars and users.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313604-444e8d49-3255-416a-816c-668b75c66205.gif' width='75%'/>
</div>
<br />

- Manager user can unreserve the rented cars.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313614-4a846d2a-36ac-4d0d-b88b-64f981b1b424.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313626-95c030c0-c714-4ce1-bd1a-1dbd13f41f09.gif' width='75%'/>
</div>
<br />

- Manager user can mark the car as damaged, which will not be available for rent, and vice versa.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232313640-a3804c5b-dbec-4f43-b6b6-b52519810feb.gif' width='75%'/>
</div>
<br />

&nbsp;

## Demo Videos

<h2 align="center">Normal User Features</h2>
<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232314306-ff227f21-8019-4d0b-b5d1-561ac292d4e9.gif' width='75%'/>
</div>
<br />

<h2 align="center">Manger User Features</h2>
<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/232314382-dfd67246-952a-424d-871c-18c103a221b5.gif' width='75%'/>
</div>
<br />

&nbsp;

## Setup

```bash
# Initialize a Virtual Environment
$ virtualenv -p python3 car_rental_system
$ cd car_rental_system
$ source bin/activate

# If you don't have Odoo 15 installed on your device
$ git clone --branch 15.0 --single-branch --depth 1 git@github.com:odoo/odoo.git
$ pip3 install -r odoo/requirements.txt
$ sudo npm install -g rtlcss

# Clone the Repo
$ git clone git@github.com:yahiaqous/Car-Rental-System.git src
$ cd src
$ ../odoo/odoo-bin -c config.cfg --dev=all -i car_rental_system
```

Then open your browser on [http://localhost:8069](http://localhost:8069) to see the result.

&nbsp;

## Features to be Added

- Hide the duplicated borrower field in the "Reserve a Car" wizard for the manager form.
- Display notifications when request to unreserve a car.
- Create Dark mode button.

&nbsp;

## Acknowledgements

- This project was inspired and requested by Leading Point Software.
- This [Odoo 14 Development Cookbook - Fourth Edition](https://github.com/PacktPublishing/Odoo-14-Development-Cookbook-Fourth-Edition) book which is a complete source that explains Odoo concepts.
- This [Answer](https://www.odoo.com/forum/help-1/make-a-field-not-editable-by-user-but-by-code-211749) helped me how to make a field not editable by user.
- This [Answer](https://www.odoo.com/forum/help-1/how-to-filter-records-for-tree-view-based-on-logged-in-user-for-admin-manager-i-want-show-evrey-record-for-normal-user-i-want-show-records-created-by-that-particular-user-only-129051) helped me how to filter records for tree view based on logged in user.
- This [Answer](https://www.odoo.com/forum/help-1/how-to-make-buttons-invisible-based-on-a-condition-82326) helped me how to make buttons invisible based on a condition.
- This [Answer](https://www.odoo.com/forum/help-1/button-call-function-from-another-module-in-xml-47838) helped me how make a button call function from another module in xml.
- This [Answer](https://www.odoo.com/forum/help-1/how-to-add-a-default-group-by-filter-to-tree-view-29874) and this [Answer](https://www.odoo.com/forum/help-1/group-by-expand-search-view-default-context-action-act-window-in-odoo13-191752) helped me for grouping the records in tree view.

&nbsp;

## Contact

Created by [Yahia Qous](https://github.com/yahiaqous) - feel free to contact me!
