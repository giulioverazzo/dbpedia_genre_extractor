f = open("output/genre_names.txt","r",encoding="utf8")
f2 = open("output/3_genresmod.txt","w",encoding="utf8")

for l in f:
    l = l.rstrip('\n')
    string = "\"%s\",\"%s\"\n" % (l, l)
    f2.write(string)
f2.close()
