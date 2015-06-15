# spearman-rank.py

# set critical values
CRIT_VALUES = { 5:  1.000,
				6:  0.886,
				7:  0.786,
				8:  0.738,
				9:  0.700,
				10: 0.648,
				11: 0.618,
				12: 0.587,
				13: 0.560,
				14: 0.538,
				15: 0.521,
				16: 0.503,
				17: 0.488,
				18: 0.472,
				19: 0.460,
				20: 0.447,
				21: 0.436,
				22: 0.425,
				23: 0.416,
				24: 0.407,
				25: 0.398,
				26: 0.390,
				27: 0.383,
				28: 0.375,
				29: 0.368,
				30: 0.362 }

# the data sets to be ranked
set_1 = [0, 50, 150, 200, 250, 300, 350, 400, 450, 500]
set_2 = [0, 10, 28, 42, 59, 51, 73, 85, 104, 96]

# order the sets
set_1_ord = sorted(set_1)
set_2_ord = sorted(set_2)

# append relevant rank to each value in set
set_1_ranked = []
set_2_ranked = []

for i in range(len(set_1)):
	set_1_ranked.append([set_1[i], set_1_ord.index(set_1[i])+1])

for i in range(len(set_2)):
	set_2_ranked.append([set_2[i], set_2_ord.index(set_2[i])+1])

print set_1_ranked
print set_2_ranked

# calculate d
d = []
for i in range(len(set_1_ranked)):
	d.append(set_1_ranked[i][1] - set_2_ranked[i][1])
print d

# calculate d^2
d_sq = [i**2 for i in d]
print d_sq

# sum d^2
sum_d_sq = sum(d_sq)
print sum_d_sq

# calculate n^3 - n
n_cu_min_n = len(set_1)**3 - len(set_1)
print n_cu_min_n

# calculate r
r = 1 - ((6.0*sum_d_sq)/n_cu_min_n)
print r

critical = CRIT_VALUES[len(set_1)]

# compare r to relevant critical value
if r > critical:
	print 'significant correlation'