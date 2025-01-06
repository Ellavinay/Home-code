color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [color[i]
         for i in range(len(color))
            if i not in (0, 4, 5)]
print(color)

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del colors[0]
del colors[4]
del colors[2]
r=set(colors)
print(colors)
print(r)