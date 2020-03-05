def generate_clusters(means, elements, n_clusters):
    clusters = {}
    for mean in means:
        clusters[str(mean)] = []
    for element in elements:
        # print(element)
        distance = 9999
        assign = ''
        for mean in means:
            # print(mean)
            distance_new = abs(element - mean)
            if distance > distance_new:
                distance = distance_new
                assign = str(mean)
        clusters[assign].append(element)
    # print(clusters)
    return clusters


def string(l):
    st = ''
    for i in l:
        st += str(i)
    return st


def main():
    elements = input('Enter Data Elements: ')
    elements = list(map(int, elements.split()))
    # print(elements)
    n_clusters = int(input('Enter no. of clusters: '))
    flag = 1
    means = []
    # count = 0

    clusters = {}
    for i in range(n_clusters):
        means.append(elements[i])
        clusters[str(elements[i])] = []
    # print(clusters)
    clusters_old = clusters
    while flag:
        clusters_new = generate_clusters(means, elements, n_clusters)
        for cluster in clusters_new.values():
            # print('cluster', string(cluster))
            for cluster_old in clusters_old.values():
                # print('cold', string(cluster_old))
                if cluster == cluster_old:
                    flag = 0
                    break
                flag = 1
        means = []
        for cluster in clusters_new.values():
            means.append(average(list(cluster)))
        clusters_old = clusters_new
        # count += 1
    return clusters_old


if __name__ == '__main__':
    from statistics import mean as average
    print(main())
    print('Code ended')
