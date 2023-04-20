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
  <img src='https://user-images.githubusercontent.com/80676788/233330429-33b092ae-5028-4bc2-98a9-bdb38773b6b4.gif' width='75%'/>
</div>
<br />

- User can reserve the available cars.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233330519-4d92e133-f20f-4828-918d-469d310bfd0d.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233330557-88511c78-6de4-4b85-9f79-6a7bd8c06b70.gif' width='75%'/>
</div>
<br />

- User can explore all his reservation history.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233330651-b40386ef-5f40-4742-8937-87699bd4a477.gif' width='75%'/>
</div>
<br />

- User can request to unreserve car.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233330763-33d1dbe1-6d8f-4eab-b1fc-aaf120012cc2.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233330840-f94101f8-27bf-43e9-9c24-9f719c1dc5f8.gif' width='75%'/>
</div>
<br />

- Manager user can create, update, delete the cars.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233330884-df8a4660-ca14-4f3a-9887-7f3dd3040101.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233330938-603f2e8c-8a31-4d5d-84b6-32e51dcdd068.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233330999-56ffbebc-3073-4599-987f-c5b145534d2f.gif' width='75%'/>
</div>
<br />

- Manager user can reserve the cars to users.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233331064-12d1b71c-43d9-4e6d-b76a-50815633f2d7.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233331117-7ae7335f-7f29-4a41-95bc-6da7ec7d9ce1.gif' width='75%'/>
</div>
<br />

- Manager user can explore all reservation history for all cars and users.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233331171-d50a9ed8-da05-4b0c-9a7b-52b168a09bba.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233331269-b8726405-0848-4ef0-b290-718ba2182e71.gif' width='75%'/>
</div>
<br />

- Manager user can unreserve the rented cars.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233331329-ab1afcc0-095e-4c44-81e1-2af214ffb696.gif' width='75%'/>
</div>
<br />

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233331371-f4f523d1-bd19-4f75-8d93-59ec47c1a7e7.gif' width='75%'/>
</div>
<br />

- Manager user can mark the car as damaged, which will not be available for rent, and vice versa.

<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233331431-7744e1a5-c294-455a-96dd-bfd28ab9ae54.gif' width='75%'/>
</div>
<br />

&nbsp;

## Demo Videos

<h2 align="center">Normal User Features</h2>
<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233336797-a4772abd-0a7d-45d4-aa29-193643072aed.gif' width='75%'/>
</div>
<br />

<h2 align="center">Manager User Features</h2>
<div align="center">
  <img src='https://user-images.githubusercontent.com/80676788/233336859-faf011f0-54d2-479b-a996-4a31e876efd9.gif' width='75%'/>
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
$ ../odoo/odoo-bin -d cardb --addons-path=../odoo/addons,. -i car_rental_system --dev all --db-filter '.*'
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
- This [Tutorial](https://www.cybrosys.com/blog/how-to-add-smart-buttons-in-odoo-15) helped me how to add a smart button.
- This [Answer](https://www.odoo.com/forum/help-1/make-a-field-not-editable-by-user-but-by-code-211749) helped me how to make a field not editable by user.
- This [Answer](https://www.odoo.com/forum/help-1/how-to-filter-records-for-tree-view-based-on-logged-in-user-for-admin-manager-i-want-show-evrey-record-for-normal-user-i-want-show-records-created-by-that-particular-user-only-129051) helped me how to filter records for tree view based on logged in user.
- This [Answer](https://www.odoo.com/forum/help-1/how-to-make-buttons-invisible-based-on-a-condition-82326) helped me how to make buttons invisible based on a condition.
- This [Answer](https://www.odoo.com/forum/help-1/button-call-function-from-another-module-in-xml-47838) helped me how to make a button call function from another module in xml.
- This [Answer](https://www.odoo.com/forum/help-1/how-to-get-the-logged-user-111605) helped me how to get the current logged in user.
- This [Answer](https://stackoverflow.com/questions/74223259/how-to-set-a-domain-for-a-view-odoo-15) helped me how to set a domain for a view.
- This [Answer](https://www.odoo.com/forum/help-1/how-to-add-a-default-group-by-filter-to-tree-view-29874) and this [Answer](https://www.odoo.com/forum/help-1/group-by-expand-search-view-default-context-action-act-window-in-odoo13-191752) helped me for grouping the records in tree view.

&nbsp;

## Contact

Created by [Yahia Qous](https://github.com/yahiaqous) - feel free to contact me!
