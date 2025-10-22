#Fill all possible starting scores
startScores = []

for i in range(98):

    startScores.append(i+2)

#Fill singles
singles = []

for i in range(1,21):

    singles.append(i)

singles.append(25)

#Fill doubles
doubles = []

for i in range(1,21):

    doubles.append(i * 2)

doubles.append(50)

#Fill triples
triples = []

for i in range(1,21):

    triples.append(i * 3)

#Initialise checkout list
checkouts = []

#Define functions
def oneGo(num):

    if num in doubles:

        checkout = ['NULL', 'NULL', 'D' + str(int(doubles[doubles.index(num)] / 2))]

        if checkout not in checkouts:

            checkouts.append(['NULL', 'NULL', 'D' + str(int(doubles[doubles.index(num)] / 2))])

        return checkout

    

def twoGoes(num):

    twoGoCheckouts = []

    for score in singles:

        if (num - score) >= 2 and (num - score) % 2 == 0:

            if oneGo(num - score):

                checkout = ['NULL', 'S' + str(score), oneGo(num - score)[2]]

                if checkout not in checkouts:

                    checkouts.append(checkout)
                    
                twoGoCheckouts.append(checkout)

    for score in doubles:

        if (num - score) >= 2 and (num - score) % 2 == 0:

            if oneGo(num - score):

                checkout = ['NULL', 'D' + str(int(score/2)), oneGo(num - score)[2]]

                if checkout not in checkouts:

                    checkouts.append(checkout)
                    
                twoGoCheckouts.append(checkout)

    for score in triples:

        if (num - score) >= 2 and (num - score) % 2 == 0:

            if oneGo(num - score):

                checkout = ['NULL', 'T' + str(int(score/3)), oneGo(num - score)[2]]

                if checkout not in checkouts:

                    checkouts.append(checkout)
                
                twoGoCheckouts.append(checkout)

    return twoGoCheckouts

def threeGoes(num):

    for score in singles:

        if (num - score) >= 4:

            if twoGoes(num - score):

                for twoGoCheckout in twoGoes(num-score):

                    checkout = ['S' + str(score), twoGoCheckout[1], twoGoCheckout[2]]
                    falseCheckout = [twoGoCheckout[1], 'S' + str(score), twoGoCheckout[2]]

                    if checkout not in checkouts and falseCheckout not in checkouts:

                        checkouts.append(checkout)

    for score in doubles:

        if (num - score) >= 4:

            if twoGoes(num - score):

                for twoGoCheckout in twoGoes(num-score):

                    checkout = ['D' + str(int(score/2)), twoGoCheckout[1], twoGoCheckout[2]]
                    falseCheckout = [twoGoCheckout[1], 'D' + str(int(score/2)), twoGoCheckout[2]]


                    if checkout not in checkouts and falseCheckout not in checkouts:

                        checkouts.append(checkout)

    for score in triples:

        if (num - score) >= 4:

            if twoGoes(num - score):

                for twoGoCheckout in twoGoes(num - score):

                    checkout = ['T' + str(int(score/3)), twoGoCheckout[1], twoGoCheckout[2]]
                    falseCheckout = [twoGoCheckout[1], 'T' + str(int(score/3)), twoGoCheckout[2]]

                    if checkout not in checkouts and falseCheckout not in checkouts:

                        checkouts.append(checkout)


for score in startScores:

    oneGo(score)

    twoGoes(score)

    threeGoes(score)

print(len(checkouts+1))





