"""Name: Tse-Lun Hsu, Student ID: 61737979"""
"""Game Description: It is called Traveling Salesman game, to find the shortest path to travel 50 cities in US"""

from random import *
from math import *

def read_cities(file_name):
    """Read in the cities from the given file_name, and return them as a list of four-tuples: [(state, city, latitude, longitude), ...]
    Use this as your initial road_map, that is, the cycle Alabama → Alaska → Arizona → ... → Wyoming → Alabama."""
    road_map = []
    file = open("city_data.txt", "r")
    for line in file.readlines():
        road_map.append(tuple(line.strip().split("\t")))
    file.close()
    return road_map 
       
def print_cities(road_map):
    """Prints a list of cities, along with their locations. Print only one or two digits after the decimal point."""
    cities_and_location = []
    for i in range(0, len(road_map)):
        cities_and_location.append((road_map[i][1], round(float(road_map[i][2]), 1), round(float(road_map[i][3]), 1)))
    print (cities_and_location)

def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    earth_radius = 3956  
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    return earth_radius * c
        
def compute_total_distance(road_map):
    """Returns, as a floating point number, the sum of the distances of all the connections in the road_map.
    Remember that it's a cycle, so that (for example) in the initial road_map, Wyoming connects to Alabama.."""
    total_distance = 0 
    for i in range(len(road_map)):
        total_distance += distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[(i + 1) % len(road_map)][2]), float(road_map[(i + 1) % len(road_map)][3]))
    return total_distance
                   
def swap_adjacent_cities(road_map, index):
    """Take the city at location index in the road_map, and the city at location index+1
    (or at 0, if index refers to the last element in the list), swap their positions in the road_map, compute the new total distance,
    and return the tuple (new_road_map, new_total_distance)."""
    new_road_map = road_map[:]
    new_road_map[index], new_road_map[(index + 1) % len(road_map)] = new_road_map[(index + 1) % len(road_map)], new_road_map[index]    
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance)
   
def swap_cities(road_map, index1, index2):
    """Take the city at location index in the road_map, and the city at location index2,
    swap their positions in the road_map, compute the new total distance, and return the tuple (new_road_map, new_total_distance).
    Allow the possibility that index1=index2, and handle this case correctly."""
    if  index1 != index2:
        new_road_map = road_map[:]
        new_road_map[index1], new_road_map[index2] = new_road_map[index2], new_road_map[index1]
        new_total_distance = compute_total_distance(new_road_map)
    else:
        new_road_map = road_map[:]
        new_total_distance = compute_total_distance(road_map)
    return (new_road_map, new_total_distance)
   

def find_best_cycle(road_map):
    """Using a combination of swap_cities and swap_adjacent_cities, try 10000 swaps,
    and each time keep the best cycle found so far. After 10000 swaps, return the best cycle found so far."""
    new_road_map = road_map[:]
    best_distance = compute_total_distance(road_map)
    for i in range(0, 10000):       
        if i < 1000:
            index1 = randint(0, len(new_road_map) - 1)
            (road_map1, road_map1_distance) = swap_adjacent_cities(new_road_map, index1)
            if road_map1_distance < best_distance:
                best_distance = road_map1_distance
                new_road_map = road_map1[:]               
        if 1000 <= i < 5000:
            index1 = randint(0, len(new_road_map) - 1)
            index2 = randint(0, len(new_road_map) - 1)
            (road_map2, road_map2_distance) = swap_cities(new_road_map, index1, index2)
            if road_map2_distance < best_distance:
                    best_distance = road_map2_distance
                    new_road_map = road_map2[:]
        else:
            index1 = randint(0, len(new_road_map) - 1)
            (road_map1, road_map1_distance) = swap_adjacent_cities(new_road_map, index1)
            if road_map1_distance < best_distance:
                best_distance = road_map1_distance
                new_road_map = road_map1[:]              
    return new_road_map
               
def print_map(road_map):
    """Prints, in an easily understandable format, the cities and their connections,
    along with the cost for each connection and the total cost."""   
    for i in range(len(road_map)):       
        cost = distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[(i + 1) % len(road_map)][2]), float(road_map[(i + 1) % len(road_map)][3]))
        print ("The city is {} and connection is {}, the cost is {}". format(road_map[i][1], road_map[(i + 1) % len(road_map)][1], cost))       
    print ("The total cost is", compute_total_distance(road_map))

def main():
    """Reads in and prints out the city data, then creates the "best" cycle and prints it out."""
    road_map = read_cities("city_data.txt")
    print_cities(road_map)
    new_road_map = find_best_cycle(road_map)
    print_map(new_road_map)
     
if __name__ == "__main__":
    main()
