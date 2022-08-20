from data_capture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()

print("Numbers: 3, 9, 3, 4, 6")
print("Stats:")
print("- less than 4 ->", stats.less(4))
print("- greater than 4 ->", stats.greater(4))
print("- between 3 and 6 ->", stats.between(3, 6))
