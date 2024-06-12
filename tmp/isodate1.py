import re
#x = "PT1H3M2S"
x = "PT2S"
print(re.findall('PT(\d+)H(\d+)M(\d+)S',x)[0])
h, m, s = re.findall('PT(\d+)H(\d+)M(\d+)S',x)[0]
total_seconds = 3600*int(h) + 60*int(m) + int(s)
print(total_seconds)