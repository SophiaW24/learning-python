#Mendel´s First Law

k = 2
m = 2
n = 2


def calcprob(k, m, n):
    population = k + m + n

    k_strand = (k / population) * (((k-1) / (population-1)) + (m / (population - 1)) + (n / (population - 1)))
    m_strand = (m / population) * (((3*(m-1)) / (4*(population-1))) + (k / (population - 1)) + (n / (2*(population - 1))))
    n_strand = (n / population) * ((k / (population - 1)) + (m / (2*(population - 1))))

    PA = round(k_strand + m_strand + n_strand, 5)
    return PA

calcprob(2,2,2)
0.78333
