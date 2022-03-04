import turtle

def get_state_corr():
    def get_mouse_click_coor(x, y):
        print(x, y)

    turtle.onscreenclick(get_mouse_click_coor)
    turtle.mainloop()