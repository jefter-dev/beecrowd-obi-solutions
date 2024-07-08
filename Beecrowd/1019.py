# Conversão de Tempo
seconds = int(input())

hours = seconds // 60 // 60
minutes = (seconds - (hours * 60 * 60)) // 60
seconds = (seconds - (hours * 60 * 60) - (minutes * 60))

print("{0}:{1}:{2}".format(hours, minutes, seconds))