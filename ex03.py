max_inputs = 4
bricks = []
layer2 = []
layer3 = []
layer4 = []

for i in range(max_inputs):
    bricks.append(int(input("Enter the number of bricks: ")))

for j in range(1,len(bricks)):
    layer2.append(bricks[j] + bricks[j-1])
    if(j>1):
        layer3.append(layer2[j-1] + layer2[j-2])
        if(j>2):
            layer4.append(layer3[j-2] + layer3[j-3])
print("Layer 4:       ", layer4)
print("Layer 3:     ", layer3)
print("Layer 2:   ", layer2)
print("Layer 1: ", bricks)

     