from detect_circle import Detect_circle

for mss in range(3394, 7106):
    detect_circle = Detect_circle()
    filename = './original_sample/158117' + str(mss) + '.jpg'
    # detect_circle.save_file(filename)
    detect_circle.save_rotate_file(filename)