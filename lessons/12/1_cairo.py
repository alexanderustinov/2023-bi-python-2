import cairo
from math import pi

with cairo.SVGSurface('pic.svg', 200, 200) as surface:
    ctx = cairo.Context(surface)
    ctx.move_to(0, 0)
    ctx.set_source_rgb(255, 0 ,0)
    ctx.line_to(200, 200)
    ctx.stroke()

    ctx.set_source_rgba(0, 0, 0, 0.5)
    ctx.rectangle(50, 50, 100, 100)
    ctx.fill()

    ctx.rectangle(50, 50, 100, 100)
    ctx.set_line_width(5)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

    ctx.set_source_rgb(0, 255, 255)
    ctx.arc(100, 100, 50, 0, 3/2*pi)
    ctx.fill()

    ctx.set_source_rgb(0, 0, 0)
    ctx.set_font_size(30)
    ctx.move_to(50, 42) 
    ctx.show_text("hi")
    ctx.stroke()
    
