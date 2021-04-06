# %%
# imports
import pyautogui
import numpy as np
import d3dshot
import time
# %%
states = ['left', 'right']
py_pause = 0.04
pixel_pause = 0.005
right_branch_coords = (1340, 1000, 1341, 1001)
left_branch_coords = (1220, 1000, 1221, 1001)
brown = np.array((161, 116, 56))

d = d3dshot.create(capture_output = "numpy")
d.display
# py 0.041 pixel 0.003 fastest 532


pyautogui.PAUSE = py_pause

# %%
def check_pixel(location): # returns if pixel at this location == brown of the branch
    image_left = d.screenshot(region = left_branch_coords)
    image_right = d.screenshot(region = right_branch_coords)
    time.sleep(pixel_pause)
    if location == 'left':
        if (image_left[0][0] == brown)[0]:
            print("left")
            return True
    else:
        if (image_right[0][0] == brown)[0]:
            print("right")
            return True

    return False

# %%
def check_pixel_ver_2(location): 
    if location == 'left':
        image = d.screenshot(region = left_branch_coords)
    else:
        image = d.screenshot(region = right_branch_coords)

    if (image[0][0] == brown)[0]:
        time.sleep(pixel_pause)
        print("SIAM")
        return True
    else:
        return False
# %%
def click_arrow(direction):
    pyautogui.keyDown(f"{direction}")
    pyautogui.keyUp(f"{direction}")

# %%
def play():
    time.sleep(5)
    print("started")
    curr_state = 0
    while True:
        if check_pixel_ver_2(states[curr_state]): # if above is the branch
            curr_state = 1 - curr_state # toggles curr_state
        click_arrow(states[curr_state])
# %%
play()
# %%
