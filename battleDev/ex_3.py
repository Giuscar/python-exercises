""""
Input
Row 1: The number of agents in network N, between 1 and 1000
Rows 2 to N : Two integers A and B separated by as space, meaning that agent B is the
superior of agent A.
Output
10 integers separated by spaces, representing the number of agents on each level between
1 and 10.

Notes :
- There is a maximum of 1000 agents in the network.
- No agent has a level of more than 10
- Each agent has exactly one superior, except for Dolan, who has no superior.
- Dolan Grump is represented by the integer 0.

Example
For the input :
5
1 4
3 1
4 0
2 4

The output should be:
1 1 2 1 0 0 0 0 0 0
"""

def scan_tree(key, linked_agents_dict):
    if key in linked_agents_dict:
        print(len(linked_agents_dict[key]))
        for val in linked_agents_dict[key]:
            scan_tree(val, linked_agents_dict)
    else: print("0")


def number_of_agents_per_level(number_of_agents, linked_agents):
    linked_agents_dict = {}

    for linked_agent in linked_agents:
        A, B = linked_agent.split(" ")
        if not B in linked_agents_dict:
            linked_agents_dict[B] = []
        linked_agents_dict[B].append(A)
    print(1)
    scan_tree('0', linked_agents_dict)


if __name__ == "__main__":
    number_of_agents = 5
    linked_agents = ["1 4", "3 1", "4 0", "2 4"]
    number_of_agents_per_level(number_of_agents, linked_agents)