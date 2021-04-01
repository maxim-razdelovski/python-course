first_day_run = float(input("input 1st day run in km: "))

desired_run = int(input("input desired distance in km: "))

current_run = first_day_run
day_count = 1

while current_run < desired_run:
    day_count += 1
    current_run += current_run * 0.1
    # print(f"ran {current_run:.2f} at day {day_count}")

print(f"runner reached desired distance in {day_count} days")

