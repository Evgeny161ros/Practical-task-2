number_of_homework_completed = '12'
number_of_hours_spent = '1.5'
course_name = 'Python'
time_for_one_task = float(number_of_hours_spent)/int(number_of_homework_completed)
punctuation = ","
print('Курс:', course_name + punctuation, 'всего задач:', number_of_homework_completed + punctuation, 'затрачено часов:', number_of_hours_spent + punctuation, 'среднее время выполнения', time_for_one_task, 'часа.')
