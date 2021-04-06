# %%
# imports
import pyautogui
from PIL import ImageGrab as imagegrab
import numpy as np
import d3dshot

# %%
d = d3dshot.create(capture_output = "numpy")
d.display
# %%
# right (1340, 1000)
right_branch_test = (1340, 1000, 1341, 1001)
left_branch_test = (1220, 1000, 1221, 1001)
image_2 = d.screenshot(region = left_branch_test)
# print(list(image_2.getdata()))
# %%
brown = np.array((161, 116, 56))
while True:
    right_branch_image = d.screenshot(region = right_branch_test)
    left_branch_image = d.screenshot(region = left_branch_test)
    if (right_branch_image[0][0] == brown)[0]:
        print("right brown")
    elif (left_branch_image[0][0] == brown)[0]:
        print("left brown")
# %%
d = d3dshot.create()
d.screenshot_to_disk(region = None)
# %%
print(image_2)
# %%
if (image_2[0][0] == np.array((161, 116, 56)))[0]:
    print("yay")
# %%
