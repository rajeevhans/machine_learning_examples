import numpy as np
import matplotlib.pyplot as plt

def lineChart ():
    # Line Charts
    x = np.linspace(0,20,1000)

    y = np.cos(x) + .23

    plt.plot(x,y)
    plt.xlabel('Input')
    plt.ylabel('Cos function output')
    plt.title("Cos function visualizaion")

    plt.show()

def scatterPlot1():
    # Scatter plot
    X = np.random.randn(100, 2)
    print(X)

    #plt.scatter (X aaxis, Y aaxis)
    plt.scatter(X[:,0], X[:,1])
    plt.show()

def scatterPlot2():
    # Scatter plot
    X = np.random.randn(200, 2)

    X[:50] += 3
    Y = np.zeros(200)
    Y[:50] = 1

    plt.scatter(X[:,0], X[:,1], c=Y)
    plt.show()  

def histogramNormalDist ():
    X = np.random.randn(1000)
    plt.hist(X, bins=200)
    plt.show()

def histogramUniformDist ():
    X = np.random.random(1000)
    plt.hist(X, bins=200)
    plt.show()

# histogramUniformDist()

def plottingImages():
    from PIL import Image
    im = Image.open("/Users/rhans/Downloads/jade.png")

    print ("Image info", im.format)
    imageArray = np.array(im)

    grayImage = imageArray.mean(axis=2)

    print("Shape of Colored Image", imageArray.shape)
    # print("Colored Image array", imageArray)

    print("----------------------------------------------------------------")
    print("Shape of gray Image", grayImage.shape)
    # print("B/W Image array", grayImage)
    
    plt.imshow(grayImage, cmap='gray')
    plt.show()

plottingImages()