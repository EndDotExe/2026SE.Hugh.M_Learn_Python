itsgifnotjif = input(" ")

name, filetype = itsgifnotjif.split(".")
filetype = filetype.lower()

match filetype:
    case "png"|"gif"|"jpeg"|"jpg":
        print(f"image/{filetype}")
    case "mp4"|"mov":
        print(f"video/{filetype}")
    case "mp3"|"wav":
        print(f"audio/{filetype}")
    case "pdf"|"txt"|"zip":
        print (f"application/{filetype}")
    case _:
        print("application/octet-stream")