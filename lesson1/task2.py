seconds = int(input("input time value in seconds: "))

hours = seconds // 60 // 60
minutes = (seconds - hours * 60 * 60) // 60
seconds_remainder = seconds % 60

# decimal_places_formatter
dpf = "{:0>2d}".format

print(f"{dpf(hours)}:{dpf(minutes)}:{dpf(seconds_remainder)}")




