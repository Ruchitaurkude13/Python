# User will enter the start date and end date. Ask user to enter the task to be done on weekdays. 
# If it is weekend then no task should be allotted. 


from datetime  import datetime, timedelta

start_date_str=input("Enter the  start date  (YYYY-MM-DD): ")
end_date_str=input("Enter the end date (YYYY-MM-DD): ")


start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

if start_date > end_date:
  print("Start date cannot be after the end date.")
        

current_date = start_date
tasks = {}

while current_date <= end_date:
  
        if current_date.weekday() < 5:  # 0 = Monday, 4 = Friday
            task = input(f"Enter task for {current_date.strftime('%Y-%m-%d')} (Weekday): ")
            tasks[current_date.strftime('%Y-%m-%d')] = task
        else:
            print(f"{current_date.strftime('%Y-%m-%d')} is a {current_date.strftime("%A")} weekend. No task allotted.")
        
       
        current_date += timedelta(days=1)


print("\nTasks scheduled:")
for date, task in tasks.items():
        print(f"{date}: {task}")