def bouncing_ball(h, bounce, window):
    if h > 0 and 0 <= bounce < 1 and window < h:
        falls = 0
        while h > window:
            h = h * bounce
            falls += 1
        app = falls + (falls - 1)вввв
        return app
    else:
        return -1


print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
