import utils
import config.probability as config
import numpy as np

def selectGProd(record):
    record.append(f"G{str(np.random.choice(54, 1, p=list(config.gProb.distribution.values()))[0]+1).zfill(2)}")
    return record

def selectIProd(record):
    record.append(f"I{str(np.random.choice(35, 1, p=list(config.iProb.distribution.values()))[0]).zfill(2)}")
    while(utils.constraints.checkI(record) is False):
        record[1] = f"I{str(np.random.choice(35, 1, p=list(config.iProb.distribution.values()))[0]).zfill(2)}"
    return record

def selectJProd(record):
    record.append(f"J{str(np.random.choice(70, 1, p=list(config.jProb.distribution.values()))[0]+1).zfill(2)}")
    return record

def selectAProd(record):
    record.append(f"A{str(np.random.choice(8, 1, p=list(config.aProb.distribution.values()))[0]+1).zfill(2)}")
    return record

def selectBProd(record):
    record.append(f"B{str(np.random.choice(16, 1, p=list(config.bProb.distribution.values()))[0]).zfill(2)}")
    while(utils.constraints.checkB(record) is False):
        record[4] = f"B{str(np.random.choice(16, 1, p=list(config.bProb.distribution.values()))[0]).zfill(2)}"
    return record

def selectCProd(record):
    record.append(f"C{str(np.random.choice(8, 1, p=list(config.cProb.distribution.values()))[0]+1).zfill(2)}")
    return record

def selectDProd(record):
    record.append(f"D{str(np.random.choice(41, 1, p=list(config.dProb.distribution.values()))[0]).zfill(2)}")
    return record

def selectEProd(record):
    record.append(f"E{str(np.random.choice(25, 1, p=list(config.eProb.distribution.values()))[0]+1).zfill(2)}")
    return record

def selectFProd(record):
    record.append(f"F{str(np.random.choice(41, 1, p=list(config.fProb.distribution.values()))[0]+1).zfill(2)}")
    while(utils.constraints.checkF(record) is False):
        record[8] = f"F{str(np.random.choice(41, 1, p=list(config.fProb.distribution.values()))[0]+1).zfill(2)}"
    return record

def selectHProd(record):
    record.append(f"H{str(np.random.choice(38, 1, p=list(config.hProb.distribution.values()))[0]).zfill(2)}")
    while(utils.constraints.checkH(record) is False):
        record[9] = f"H{str(np.random.choice(38, 1, p=list(config.hProb.distribution.values()))[0]).zfill(2)}"
    return record

def selectKProd(record):
    record.append(f"K{str(np.random.choice(21, 1, p=list(config.kProb.distribution.values()))[0]+1).zfill(2)}")
    return record

def selectLProd(record):
    record.append(f"L{str(np.random.choice(52, 1, p=list(config.lProb.distribution.values()))[0]).zfill(2)}")
    while(utils.constraints.checkL(record) is False):
        record[11] = f"L{str(np.random.choice(52, 1, p=list(config.lProb.distribution.values()))[0]).zfill(2)}"
    return record

def selectF(record):
    record.append(f"F{str(np.random.choice(37, 1, p=list(config.fProb.distribution.values()))[0]+1).zfill(2)}")
    while(utils.constraints.checkF(record) is False):
        record[5] = f"F{str(np.random.choice(37, 1, p=list(config.fProb.distribution.values()))[0]+1).zfill(2)}"
    return record

def selectG(record):
    record.append(f"G{str(np.random.choice(47, 1, p=list(config.gProb.distribution.values()))[0]+1).zfill(2)}")
    while(utils.constraints.checkG(record) is False):
        record[6] = f"G{str(np.random.choice(47, 1, p=list(config.gProb.distribution.values()))[0]+1).zfill(2)}"
    return record

def selectH(record):
    record.append(f"H{str(np.random.choice(38, 1, p=list(config.hProb.distribution.values()))[0]+1).zfill(2)}")
    while(utils.constraints.checkH(record) is False):
        record[7] = f"H{str(np.random.choice(38, 1, p=list(config.hProb.distribution.values()))[0]+1).zfill(2)}"
    return record 

def selectI(record):
    record.append(f"I{str(np.random.choice(33, 1, p=list(config.iProb.distribution.values()))[0]+1).zfill(2)}")
    while(utils.constraints.checkI(record) is False):
        record[8] = f"I{str(np.random.choice(33, 1, p=list(config.iProb.distribution.values()))[0]+1).zfill(2)}"
    return record 

def selectJ(record):
    record.append(f"J{str(np.random.choice(67, 1, p=list(config.jProb.distribution.values()))[0]+1).zfill(2)}")
    while(utils.constraints.checkJ(record) is False):
        record[9] = f"J{str(np.random.choice(67, 1, p=list(config.jProb.distribution.values()))[0]+1).zfill(2)}"
    return record 

def selectK(record):
    record.append(f"K{str(np.random.choice(21, 1, p=list(config.kProb.distribution.values()))[0]+1).zfill(2)}")
    while(utils.constraints.checkK(record) is False):
        record[10] = f"K{str(np.random.choice(21, 1, p=list(config.kProb.distribution.values()))[0]+1).zfill(2)}"
    return record 

def selectL(record):
    record.append(f"L{str(np.random.choice(50, 1, p=list(config.lProb.distribution.values()))[0]+1).zfill(2)}")
    while(utils.constraints.checkL(record) is False):
        record[11] = f"L{str(np.random.choice(50, 1, p=list(config.lProb.distribution.values()))[0]+1).zfill(2)}"
    return record 