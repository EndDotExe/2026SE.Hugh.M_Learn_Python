itsgifnotjif = input(" ")

match itsgifnotjif:
    case "png"|"gif"|"jpeg"|"jpg":
        print(f"image/{itsgifnotjif}")
    case "mp4"|"mov":
        print(f"video/{itsgifnotjif}")
    case "mp3"|"wav":
        print(f"audio/{itsgifnotjif}")