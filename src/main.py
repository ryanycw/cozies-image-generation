import random
import numpy as np
import utils
import env
import core

def main():
    mode = "production"
    selectAmount = 5781
    np.random.seed(42)
    random.seed(42)

    utils.logs.mkdir(env.logResultPath)
    utils.logs.mkdir(env.imgResultPath)
    utils.logs.mkdir(env.jsonResultPath)

    #core.image.generateImgRecord(mode, selectAmount)
    core.image.genFinalJpgInBatch(env.logFile, env.propertiesListInOrder)
    #core.image.genJson(env.logFile)

    #core.ticket.genJson()

if __name__ == "__main__":
    main()