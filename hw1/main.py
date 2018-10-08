"""PROBLEM 1: The greedy algorithm for fragment assembly (60 points) Write a function, greedy_assemble, that takes as
input a list of read strings and uses the greedy fragment assembly algorithm to output a single superstring that
contains all reads as substrings. You must use the graph-based (Hamiltonian path) version of the greedy algorithm. We
will assume that:

we are assembling a single-stranded sequence and
that no read is a substring of any other read.

To keep things  simple, for this homeowork, we will allow overlaps of any length (including zero). In practice,
for sequence assembly we would typically require some minimum overlap length.

For the purpose of making this algorithm deterministic, we must establish tiebreaking criteria for edges in the
overlap graph that have the same weight. For two edges with the same weight, we will first choose the edge whose
source vertex read is first in lexicographical order. If the source vertices are identical, then we choose the edge
whose target vertex read is first in lexicographical order. For example, if e1 = ATCGGA → GGAT and e2 = ATCGGA →
GGAA, we will attempt to use edge e2 first because GGAA < GGAT according to lexicographical order """

# Code for PROBLEM 1
# You are welcome to develop your code as a separate Python module
# and import it here if that is more convenient for you.
from hw1 import hw1_helper
from hw1 import graph


def read_strings_from_file(filename):
    strings = []
    with open(filename) as f:
        for line in f:
            strings.append(line.rstrip())

    return strings


def _test_greedy_assemble_with_files(reads_filename, superstring_filename):
    reads = read_strings_from_file(reads_filename)
    [superstring] = read_strings_from_file(superstring_filename)
    assert greedy_assemble(reads) == superstring

def greedy_assemble(reads):
    """Returns a string that is a superstring of the input reads, which are given as a list of strings.
    The superstring computed is determined by the greedy algorithm as described in HW1, with specific tie-breaking
    criteria.
    """
    #
    return hw1_helper.shortest_superstring(reads)

def find_max_weight_edge(edge_list):
    #return index 0 for left, 1 for right
    max_weight = 0
    return_val = 0
    for tuple in edge_list:
        if tuple[2] > max_weight:
            max_weight = tuple[2]
            return_val = tuple
    return return_val




if __name__ == '__main__':
    # TEST: greedy_assemble returns a string
    sanity_test_reads = read_strings_from_file("tests/test_reads.txt")
    #assert isinstance(greedy_assemble(sanity_test_reads), str)
    print(sanity_test_reads)
    print(hw1_helper.merge_ordered_reads(["abc","de"]))
    #hellogithub??
    print("hello??")
    list.sort(sanity_test_reads)
    g = graph.FullyConnectedWeightedGraph(sanity_test_reads,hw1_helper.overlap_length)
    print(g)
    path = g.highest_weight_path(lambda x, y: x > y)
    print(path)
    superstring = hw1_helper.merge_ordered_reads(path)
    print(superstring)
    # num_vertices = g.num_vertices()
    # untraversed_reads = sanity_test_reads
    # max_edge = find_max_weight_edge([edge for edge in g.edges()])
    # start, vertex, _ = max_edge
    # untraversed_reads.remove(start)
    # untraversed_reads.remove(vertex)
    # superstring = hw1_helper.merge_two_strings(start,vertex)
    # while untraversed_reads:
    #     max_edge = find_max_weight_edge([out_edge for out_edge in g.out_edges(g.get_vertex_index(vertex)) if out_edge[1] in untraversed_reads])
    #     vertex = max_edge[1]
    #     untraversed_reads.remove(vertex)
    #     superstring = hw1_helper.merge_two_strings(superstring,vertex)
    #     print(max_edge, superstring)



    # for i in range(num_vertices-1):
    #     next_edge = find_max_weight_edge([out_edge for out_edge in g.out_edges(g.get_vertex_index(vertex)) if)
    #     next = next_edge[1]
    #     print(next_edge)
    #     untraversed_edges.remove(next_edge)
    #     superstring = hw1_helper.merge_two_strings(superstring,next)
    #     print(superstring)

    # graph = graph.WeightedGraph(sanity_test_reads,hw1_helper.merged_string_length)
    # print(graph)
    # edges = []
    # edge_weights = []
    # for edge in graph.edges():
    #     edges.append(edge)
    #     edge_weights.append(graph.get_edge_weight(edge))
    # merged_read = ''
    # max_weight = edge_weights.index(min(edge_weights))
    # next_vertex = max_weight
    # read_vertices = [0]
    # while(len(read_vertices) < len(sanity_test_reads)):
    #     max_weight = float('+inf')
    #     for edge in graph.out_edges(next_vertex):
    #         if edge[1] not in read_vertices and graph.get_edge_weight(edge) < max_weight:
    #             max_weight = graph.get_edge_weight(edge)
    #             next_vertex = edge[1]
    #     merged_read = hw1_helper.merge_two_strings(merged_read,graph.get_vertex_value(next_vertex))
    #     read_vertices.append(next_vertex)
    #     print(merged_read)
    # print(edges)
