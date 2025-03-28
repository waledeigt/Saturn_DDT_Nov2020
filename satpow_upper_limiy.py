# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:46:58 2021

@author: dmw1n18
"""
"""Upper limit to Saturn's disk emission from Nov 2020 DDT Chandra HRC-I observations"""
import numpy as np
import pandas as pd

# Reading in data needed to calculate power
pow_data = pd.read_csv('sat_power_data.csv')
obs_id = pow_data['ObsID']
obs_time = np.array(pow_data['Obs_time (ks)']*1000).astype(float) # duration in seconds
ang_d = np.array(pow_data['ang_diameter (arcsec)']).astype(float)
sat_r = np.array(pow_data['Saturn-CXO distance (AU)']).astype(float)
sat_counts = np.array(pow_data['Corrected Counts']).astype(float)
og_counts = np.array(pow_data['Total counts']).astype(float)
bkg_counts = np.array(pow_data['Background']).astype(float)
# Assuming energies ~ 0.5 keV, use HRC effective area of ~ 40 cm^2

# Stating the assumptions

AU_2_cm = 1.49598E+13
## Wanting to calculate power of the photons detected by Chandra

# Detector assumptions
pix_size = 6.42938E-4 # pixel size, in cm
scale = 0.13175 # arcsec/pixel

sat_d = ang_d/scale 
pix_hrc = 30*60/scale # Jupiter and detector in pixels
sat_pix = (0.05*sat_d*pix_size)**2#*10000

# Number flux of counts
sat_flux = sat_counts/obs_time # counts/s
sat_ph_flux = sat_flux/sat_pix # counts/second/cm^2


sattest = 0.5E3*1.602E-19*sat_flux/40 # Wcm^-2
sat_power = 4*np.pi*((sat_r*AU_2_cm)**2)*sattest
# ahsnuc_power = 4*np.pi*((jup_r2*AU_2_cm)**2)*ahsnuctest
# # dpower = 4*np.pi*((5.1*AU_2_cm)**2)*dtest
print(sat_power/1E9)#, dpower/1E9)

flux_sat = sattest*1E4*1000 #Wcm^-2 -> Wm^-2 -> erg/cm^2/s
# flux_W_ahsnuc = ahsnuctest*1E4*1000 

# av_nhs_bright = reg_pow_data['Av_bright']
# max_nhs_bright = reg_pow_data['Max_bright']

"""Poisson stats"""

ct_err = np.sqrt(og_counts + bkg_counts)
print("Counts: {} +/- {}".format(sat_counts, ct_err))
print("Count flux: {} +/- {}".format(sat_flux*1E3, ct_err/obs_time*1E3))
flux_err = np.abs((ct_err/obs_time) * 0.5E3*1.602E-19/40 )*1E4*1000
pow_err = flux_err * 4*np.pi*((sat_r*AU_2_cm)**2)/(1E4*1000)
print("Power: {} +/- {}".format(sat_power/1E9, pow_err/1E9))
print("Flux: {} +/- {}".format(flux_sat*1e15, flux_err*1e15))

"""99.9% upper limit"""

mean_flux = []
testflux = []
upper_limit_flux = []
mean_power = []
upper_limit_power = []

zval = 3.291 # 3 sigma z val

for ii in range(len(ct_err)):
    mean_counts2=np.arange(0,round(sat_counts[ii]+ct_err[ii])+1)
    sat_flux2 = mean_counts2/obs_time[ii] # counts/s
    sat_ph_flux2 = sat_flux2/sat_pix[ii] # counts/second/cm^2
    sattest2 = 0.5E3*1.602E-19*sat_flux2/40 # Wcm^-2
    sat_power2 = 4*np.pi*((sat_r[ii]*AU_2_cm)**2)*sattest2
    testflux.append(sattest2*1E4*1000)
    mflux = np.mean(sattest2*1E4*1000) #Wcm^-2 -> Wm^-2 -> erg/cm^2/s
    mpow = np.mean(sat_power2/1E9)
    mean_flux.append(mflux)
    
    fl99 = zval*np.std(sattest2*1E4*1000)/np.sqrt(np.mean(mean_counts2))
    upper_limit_flux.append("99.99% upper limit mean flux:{} +/- {}, upper limit ={}".format(mflux, fl99, (mflux+fl99)))
    pow99 = zval*np.std(sat_power2/1E9)/np.sqrt(np.mean(mean_counts2))
    upper_limit_power.append("99.99% upper limit mean power:{} +/- {}, upper limit = {}".format(mpow, pow99, (mpow+pow99)))


