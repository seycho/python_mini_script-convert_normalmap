from numpy import gradient, float32, hstack, uint8, zeros, sqrt, max
from cv2 import COLOR_BGR2RGB, GaussianBlur, cvtColor, imread


def ComputeNormalmap(nameInput, sigma=7, intensity=100):
    
    img = imread(nameInput, 0)
    
    gradiX, gradiY = gradient(img)
    gradiX = GaussianBlur(gradiX*-1, (sigma*2-1, sigma*2-1), sigma)
    gradiY = GaussianBlur(gradiY*-1, (sigma*2-1, sigma*2-1), sigma)
    
    width = img.shape[1]
    height = img.shape[0]
    valueMax = max(hstack([gradiX, gradiY]))
    
    normalmap = zeros((height, width, 3), dtype=float32)
    
    normalmap[..., 0] = gradiY / valueMax
    normalmap[..., 1] = gradiX / valueMax
    normalmap[..., 2] = 1 / intensity
    
    valueNormalize = sqrt(normalmap[..., 0]**2 + normalmap[..., 1]**2 + normalmap[..., 2]**2)

    normalmap[..., 0] /= valueNormalize
    normalmap[..., 1] /= valueNormalize
    normalmap[..., 2] /= valueNormalize
    
    normalmap *= 0.5
    normalmap += 0.5
    normalmap *= 255
    
    return cvtColor(normalmap.astype(uint8), COLOR_BGR2RGB)