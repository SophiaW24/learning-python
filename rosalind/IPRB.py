#Mendel´s First Law

k = 2
m = 2
n = 2
​
population = k + m + n
​
k_strand = ((k/population) * ((k-1)/(population-1)) * 1) + ((k/population) * (m/(population-1)) * 1) + ((k/population) * (n/(population-1)) *1)
m_strand = ((m/population) * (k/(population-1)) * 1) + ((m/population) * ((m-1)/(population-1)) * 0.75) + ((m/population) * (n/(population-1)) * 0.5)
n_strand = ((n/population) * (k/(population-1)) * 1) + ((n/population) * (m/(population-1)) * 0.5) + ((n/population) * ((n-1)/(population-1)) * 0)
​
probability = round(k_strand + m_strand + n_strand, 5)
​
print(probability)
0.78333
