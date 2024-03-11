import random
import math

def generate_points(num_points, square_side):
    points = []
    for _ in range(num_points):
        x = random.uniform(0, square_side)
        y = random.uniform(0, square_side)
        points.append((x, y))
    return points

def is_in_circle(point, square_side):
    distance = math.sqrt((point[0] - square_side / 2) ** 2 + (point[1] - square_side / 2) ** 2)
    return distance <= square_side / 2

def estimate_pi(points, square_side):
    circle_count = sum(1 for point in points if is_in_circle(point, square_side))
    return 4 * circle_count / len(points)

def main():
    num_points = 100000
    square_side = 2
    points = generate_points(num_points, square_side)
    pi_estimate = estimate_pi(points, square_side)
    print(f"Estimated value of Pi: {pi_estimate}")
    print(f"Accuracy: {abs(math.pi - pi_estimate) / math.pi * 100}%")

if __name__ == "__main__":
    main()
