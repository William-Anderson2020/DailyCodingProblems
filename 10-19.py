"""
This problem was asked by Uber.

On election day, a voting machine writes data in the form (voter_id,
candidate_id) to a text file. Write a program that reads this file as a stream
and returns the top 3 candidates at any given time. If you find a voter voting
more than once, report this as fraud.

"""

with open("voterstats.txt") as f:
    stats = f.readlines()
    print(stats)
    confirmedVoters = []
    voteStats = {}
    duplicateVotes = []
    for vote in stats:
        vote = vote.split()
        #print(vote[1])
        if vote[0] not in confirmedVoters:
            confirmedVoters.append(vote[0])
            if vote[1] not in voteStats.keys():
                voteStats[vote[1]] = 0
            voteStats[vote[1]] += 1
        else:
            duplicateVotes.append(vote[0])
    order = []
    for i in voteStats:
        if len(order) == 0:
            order.append(i)
        else:
            for c in order:
                cDex = order.index(c)
                print(c)
                if int(voteStats[i]) > int(voteStats[c]):
                    order = order[:cDex] + [i] + order[cDex:]
            if i not in order:
                order.append(i)
    #print(order)
            
    #print(voteStats, duplicateVotes)
    print("{} ({} votes), {} ({} votes), and {} ({} votes) are the front runners. {} placed fraudulent vote(s).".format(order[0], voteStats[order[0]],order[1], voteStats[order[1]],order[2], voteStats[order[2]],duplicateVotes))
            
            
            