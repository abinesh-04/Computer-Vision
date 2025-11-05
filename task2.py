import cv2
import numpy as np

img = cv2.imread("assets/6.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found.")
    exit()

_, binary = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)

# connectivity here
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

output = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

# Label region
for i in range(1, num_labels):
    x, y, w, h, area = stats[i]
    cx, cy = int(centroids[i][0]), int(centroids[i][1])
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(output, f"ID:{i}", (cx - 20, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("Binary", binary)
cv2.imshow("Labeled Regions", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Total regions detected: {num_labels - 1}") 
