def k_nearest_post_offices_naive(post_offices, you, k):
    distances = []
    neighbors = []
    for i in range(len(post_offices)):
        d = (you[0] - post_offices[i][0]) ** 2 + (you[1] - post_offices[i][1]) ** 2
        if len(distances) < k:
            distances.append(d)
            neighbors.append(post_offices[i])
        else:
            maximum = max(distances)
            if d < maximum:
                n = distances.index(maximum)
                distances.pop(n)
                neighbors.pop(n)
                distances.append(d)
                neighbors.append(post_offices[i])
    return neighbors, distances
    
you = [0, 0]
post_offices = [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3

k_nearest_post_offices_naive(post_offices, you, k)

#returns ([[-1, 2], [4, 3], [0, 3]], [5, 25, 9])
