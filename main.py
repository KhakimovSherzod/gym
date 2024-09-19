

from flask import Flask, render_template, request

from fitness_plan import FitnessPlan
fitness_plan = FitnessPlan()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        exercise_text = request.form.get('exercise_text')
        workout_data = fitness_plan.track_progress(exercise_text)
        fitness_plan.log_to_sheet(workout_data)
        log_data = fitness_plan.get_workout_logs()
        return render_template('fitness_tracker.html', log_data=log_data)
    return render_template('fitness_tracker.html')

@app.route('/diet-planner')
def diet_planner():
    return render_template('diet_planner.html')

if __name__ == '__main__':
    app.run(debug=True)
