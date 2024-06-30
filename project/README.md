# BMI Calculator Project

#### Video Demo:  <URL HERE>

#### Description:
The BMI Calculator project is a web application built using Python and Flask. It allows users to calculate their Body Mass Index (BMI) based on their weight and height inputs. Additionally, users can optionally provide their gender, age, activity level, and body fat percentage to receive personalized recommendations related to their BMI results.

## Project Files

### app.py
This file contains the main Flask application logic. It handles routing, request handling, and BMI calculation based on user inputs. It integrates with templates and handles form submissions.

### templates/index.html
This HTML file defines the structure of the BMI Calculator web interface. It includes form elements for user input (weight, height, gender, age, activity level, and body fat percentage) and displays the calculated BMI result and recommendations.

### static/styles.css
The CSS file provides styling for the BMI Calculator interface. It defines colors, fonts, margins, and padding to enhance the visual appeal and usability of the web application.

## Design Choices

### Dark Theme
The project uses a dark theme for the interface to provide a modern and visually appealing look. The dark background with contrasting elements (white text and green accents) improves readability and user experience, especially in low-light environments.

### Optional Inputs
The application allows users to optionally provide additional information such as gender, age, activity level, and body fat percentage. This feature enhances the accuracy of BMI calculations and provides tailored recommendations for fitness and health management.

### Flask Framework
Flask was chosen for this project due to its simplicity and flexibility in building web applications with Python. It handles routing, form handling, and template rendering effectively, making it suitable for small to medium-sized web projects like this BMI Calculator.

## How to Use

To use the BMI Calculator:
1. Enter your name, weight (in kilograms), height (in centimeters), and optionally gender, age, activity level, and body fat percentage.
2. Click on "Calculate BMI" to see your BMI result and personalized recommendations.
3. View detailed recommendations for diet and exercise based on your BMI classification and additional inputs.

## Conclusion

The BMI Calculator project aims to provide users with a straightforward tool for understanding their BMI and receiving personalized health recommendations. It demonstrates practical application of web development skills using Python, Flask, HTML, and CSS.
