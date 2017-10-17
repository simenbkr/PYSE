

fs = 0.01
rs = 1
fc = 0.01
rc = 2
sw = 5

U_s = (fs**2 * (fs * (4*rs**2 + 9*rs*sw + 3*sw**2) + 6*rs**3)) / (3*rs**2*(rs+sw)*(fs*(8*rs+3*sw)+rs*(2*rs+sw)))

U_c = fc / (fc + rc)


U = U_s + U_c - U_s * U_c

print "U = {} = {}%".format(U, U*100)


