from GFXCard import *
myCard = GFXCard("Hello banana turtlels", 500.00, 1200)
myCard2 = GFXCard("Hello now never", 1000.00, 1500)
myCard3 = GFXCard("intel i7 4700k", 3000.00, 15000)

gfxCardList = [myCard2, myCard, myCard3]






def truncateList(list, score):
    for index, item in enumerate(list):
        if item.score >= score:
            continue
        else:
            return index
    return list


def printGPUs(gpuList):
    for item in gpuList:
        print(item.title + "\t" + "Value: " + str(item.value) + "\t" + "Score: " + str(item.score) + "\t" + "Price: " + str(item.price))

# Sort by score descending
a = sorted(gfxCardList, key = lambda card: card.score, reverse = True)
a = truncateList(a, 1100)

printGPUs(a)
