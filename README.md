# Flask Python Tutorial

Today we'll make a Flask-driven website that gives users a tutorial on basic Python concepts. We'll be doing this to practice concepts we've learned in class, such as: 

* Rendering templates, redirecting, and other routing
* Passing variables to templates
* Making `GET` and `POST` routes
* Parsing form data

## Deliverables

To complete this assignment:

* Fork and clone this repository!
* Implement the requirements below
* Push the changes to your own repository
* Open a pull request against this repository

For this assignment you will be creating ONE Flask app. Each problem listed below will direct you to create a route or feature within that app.

*Reminder: On your laptop, you can run your server from your command line with the following command:*

```
flask run
```

## Requirements:

### Routes

By the end of this, you should have ONE Flask app that implements the following routes:

| METHOD | PATH | FUNCTIONALITY |
| ------ | ------------- | ---------------------------------------------------------- |
| GET | `/` | Render a home page that includes the Python logo somewhere on the page |
| GET | `/loops` | Make a page describing for loops, while loops, and ranges in Python |
| GET | `/operators` | Make a page detailing at least 3 different operators |
| POST | `/operators` | Enable user to enter new operators |


### Database

Your `operators` documents in Mongo should look something like this: 

```json
{
  "name": "Floor Division",
  "description": "Division that rounds down to the nearest integer. Also known as integer division.",
  "symbol": "//",
  "example": "3 // 2 == 1",
  "uses": "A common situation we might see this operator is when we need to calcuate a 
  list index, which will need to be a whole number. For example, perhaps we are trying to 
  find the middle index of a list, but there are an even number of elements. In this case, 
  we could use floor division to select the leftmost element in the list by default."
}
```

### Additional Requirements

* Your site should have a `static` folder that includes a style.css with styling for your site. 
* Your site should have a nav bar/header and footer that is present on every page.
  * Navbar should include links to "Home", "Operators", and "Loops" pages


------------

## Getting Started

### Home Page

This page should include the Python logo and at least one other image. Luckily, we've already started you off with this image in the static folder of the repository. Try to make this page an appealing advertisement for your site!

### Loops Page

On this page, make at least 3 sections: 

* One section should explain how to do a basic for-in loop in Python (e.g., `for fruit in basket`)
* One section should explain how to use a basic while loop and how to set up a boolean expression without making an endless loop.
* The final section can be one of your choice - if you don't have another idea, you can tackle explaining `range` and the different options that can be provided or left out.

### Operators Page

#### GET route

The operators page should have explanations on how to use three operators of your choice. You're welcome to snag the `floor division` one from above! This page should be **completely dynamic**, meaning all this info should be stored in a mongo database in a collection called `operators`. You can do a for loop in your template page to display a section for each operator. Show code snippets for examples of each of the operators.

You should allow the user to create new operators to display on the page. You can put the form on the bottom of the same page that the operators are displayed on, or you can create a separate route to render the templates.

#### POST route

This route accepts form data that the user submits. You should validate this data before you put it into your database and if there is an issue you should send the user an error page or render some sort of error message.

## Bonus

Put your HTML and CSS skills to the test - figure out how to format your code snippets so they actually look like code. Or, at least format them so they're somewhat distinct from other text! 
