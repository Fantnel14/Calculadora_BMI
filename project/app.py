from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate_bmi(weight, height):
    if height > 3:  # Assuming height greater than 3 is in cm
        height = height / 100

    if weight <= 0 or height <= 0:
        return None, None, "Weight and height must be positive numbers."

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi < 24.9:
        classification = "Normal weight"
    elif 25 <= bmi < 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"

    return round(bmi, 2), classification, None

def get_recommendation(bmi, gender, age, weight, height, activity_level=None, body_fat=None):
    if bmi is None:
        return None

    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)

    if activity_level:
        activity_factors = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725,
            'extra_active': 1.9
        }

        activity_factor = activity_factors.get(activity_level, 1.2)
        daily_calories = bmr * activity_factor
    else:
        daily_calories = bmr * 1.2

    if body_fat is not None:
        if body_fat < 25:
            body_fat_message = f"Your body fat percentage is {body_fat}%, which is classified as healthy for your activity level. Keep up the good work!"
        else:
            body_fat_message = f"Your body fat percentage is {body_fat}%, which is higher than recommended for your activity level. Consider focusing on reducing body fat."
    else:
        body_fat_message = ""

    if bmi < 18.5:
        recommendation = "You should consider increasing your calorie intake to maintain a healthy weight."
    elif 18.5 <= bmi < 24.9:
        recommendation = "Keep up the good work!"
    elif 25 <= bmi < 29.9:
        recommendation = "Consider reducing your calorie intake and increasing physical activity."
    else:
        recommendation = "It's important to consult a healthcare professional for a personalized plan."

    return recommendation, round(daily_calories, 2), body_fat_message

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    bmi = None
    classification = None
    recommendation = None

    if request.method == 'POST':
        name = request.form['name']
        weight = request.form['weight']
        height = request.form['height']
        gender = request.form['gender']
        age = int(request.form['age'])
        activity_level = request.form.get('activity_level')
        body_fat = request.form.get('body_fat')

        try:
            weight = float(weight)
            height = float(height)
            body_fat = float(body_fat) if body_fat else None

            bmi, classification, error_message = calculate_bmi(weight, height)

            if bmi:
                recommendation, daily_calories, body_fat_message = get_recommendation(bmi, gender, age, weight, height, activity_level, body_fat)

                return redirect(url_for('results', name=name, bmi=bmi, classification=classification, recommendation=recommendation, daily_calories=daily_calories, body_fat_message=body_fat_message))

        except ValueError:
            error_message = "Invalid input. Weight and height must be numbers."
            bmi = classification = None

    return render_template('index.html', error_message=error_message, bmi=bmi, classification=classification, recommendation=recommendation)

@app.route('/results')
def results():
    name = request.args.get('name')
    bmi = float(request.args.get('bmi'))
    classification = request.args.get('classification')
    recommendation = request.args.get('recommendation')
    daily_calories = request.args.get('daily_calories')
    body_fat_message = request.args.get('body_fat_message')

    return render_template('results.html', name=name, bmi=bmi, classification=classification, recommendation=recommendation, daily_calories=daily_calories, body_fat_message=body_fat_message)

if __name__ == '__main__':
    app.run(debug=True)
