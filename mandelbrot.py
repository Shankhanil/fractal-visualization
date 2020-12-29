from PIL import Image, ImageDraw

WIDTH = 600
HEIGHT = 400
MAX_ITER = 100
def mandelbrot(c):
    z = 0
    iter = 0
    while abs(z) <= 2 and iter < MAX_ITER:
        z = z*z + c
        iter += 1
    return iter
    
def drawMandelbrot(RE_START, RE_END, IM_START, IM_END):
  im = Image.new('RGB', (WIDTH, HEIGHT)) #, (0, 0, 0))
  draw = ImageDraw.Draw(im)
  
  palette = [
    (66,30,15),
    (25,7,26),
    (9,1,47),
    (4,4,73),
    (0,7,100),
    (12,44,138),
    (24,82,177),
    (57,125,209),
    (134,181,229),
    (211,236,248),
    (241,233,191),
    (248,201,95),
    (255,170,0),
    (204,128,0),
    (153,87,0),
    (106,52,3)
  ]
  
  for x in range(0, WIDTH):
      for y in range(0, HEIGHT):
          # Convert pixel coordinate to complex number
          c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                      IM_START + (y / HEIGHT) * (IM_END - IM_START))
          # Compute the number of iterations
          m = mandelbrot(c)
          # The color depends on the number of iterations
          # color = 255 - int(m * 255 / MAX_ITER)
          if (m == MAX_ITER) :
            color = (0,0,0)
          else:
            color = palette[m % 16]
          # palette.append(color)
          # color = palette[]
          # Plot the point
          draw.point([x, y], color)

  # im.show()
  print(set(palette))
  im.show()
  im.save('output.jpg', 'JPEG')