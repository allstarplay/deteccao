def p():
    import screenshot 
    #image = pyscreenshot.grab() 
    image = screenshot.grab(bbox=(10, 10, 680, 540))
    image.show() 
    image.save("print.png") 

