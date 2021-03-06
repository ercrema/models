#!/usr/bin/python3

import decisionmaking, random

def singleRun():
    params = decisionmaking.Params()
    params.decisionType = 'probabilistic'
    params.memory = False 
    params.nSteps = 1000
    params.nAgents = 1
    params.output = 'output_dmp_0.csv'
    decisionmaking.run(params)


def convergence():
   # experiment
    numRuns = 10

    decisionTypeSweep = ['greedy']
    memoryMapSweep = [False]

    params = decisionmaking.Params()
    params.nSteps = 500

    totalRuns = 0
    for i in decisionTypeSweep:
        for j in memoryMapSweep:
            params.decisionType = i
            params.memory = j
            for run in range(0, numRuns):
                print('run:',totalRuns+1,'of:',numRuns*len(memoryMapSweep)*len(decisionTypeSweep))
                params.numRun = totalRuns
                params.nAgents = random.randint(1,200)
                params.output = 'output_dmp_'+str(params.numRun)+'.csv'
                totalRuns += 1
                decisionmaking.run(params)


def all():
    # experiment
    numRuns = 10

    decisionTypeSweep = ['greedy','probabilistic']
    memoryMapSweep = [True, False]

    params = decisionmaking.Params()

    totalRuns = 0
    for i in decisionTypeSweep:
        for j in memoryMapSweep:
            params.decisionType = i
            params.memory = j
            for run in range(0, numRuns):
                print('run:',totalRuns+1,'of:',numRuns*len(memoryMapSweep)*len(decisionTypeSweep))
                params.numRun = totalRuns
                params.output = 'output_dmp_'+str(params.numRun)+'.csv'
                totalRuns += 1
                decisionmaking.run(params)

def main():
    all()

if __name__ == "__main__":
    main()

