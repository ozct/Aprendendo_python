import matplotlib.pyplot as plt  
import random 

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

index = [index + 1 for index in range(len(labels))]
print(index)

sizes = [a for a in random.sample(range(7, 100), len(labels))]
print(sizes)
print(len(index), len(sizes), len(labels))

plt.bar(index, sizes, tick_label=labels, color=('red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan'))

plt.xlabel("Labels")
plt.ylabel("Sizes")
plt.title("Bar Plot")
plt.show()
