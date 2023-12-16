"""
RECONSTRUCT ITINERARY

You are given a list of airline `tickets` where `tickets[i] = [fromi, toi]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
"""


def reconstruct_itinerary(tickets):
    graph = {}

    for src, dest in tickets:
        if src in graph:
            graph[src].append(dest)
        else:
            graph[src] = [dest]

    for src in graph.keys():
        graph[src].sort(reverse=True)

    stack = []
    res = []
    stack.append("JFK")

    while len(stack) > 0:
        elem = stack[-1]
        if elem in graph and len(graph[elem]) > 0:
            stack.append(graph[elem].pop())
        else:
            res.append(stack.pop())
    return res[::-1]


print("Reconstruct Itinerary: ", reconstruct_itinerary(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
