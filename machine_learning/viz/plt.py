import matplotlib.pyplot as plt
## box plot
## it shows the median, the 25th and 75th percentiles as boxes, and the whiskers that extend to the furthest data point that is within 1.5 times the interquartile range
plt.boxplot(array1)
plt.show()

## violin plot
plt.violinplot(array1)
plt.show()

## histogram
plt.hist(array1)
plt.show()

## heatmap
plt.imshow(array1, cmap='hot', interpolation='nearest')
plt.show()

## scatter plot
plt.scatter(array1, array2)
plt.show()

## 折线图
#plt.plot does not accept the arguments as "x= array1, "y= array2", but "array1, array2"
plt.plot(array1, array2)
plt.show()

## mosaic plot
layout = """AAA 
            BCD"""
fig, ax = plt.subplot_mosaic(layout, figsize=(5,5))
ax['A'].plot(random_data) 
ax['B'].hist(random_data) 
ax['C'].boxplot(random_data) 
ax['D'].violinplot(dataset=random_data)
plt.tight_layout() 
plt.show()
