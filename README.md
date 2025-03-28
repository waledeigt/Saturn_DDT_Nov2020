![image](https://user-images.githubusercontent.com/76570532/140928988-f7546a29-08ad-4c85-b634-611a5586531f.png)

# Saturn_DDT_Nov2020
Code used to analyse Saturn counts recorded by Chandra HRC-I DDT observations in November. The 3-sigma power and flux is also calculated, given a low count regime. Full description of analysis and observations can be found in Weigt+ 2021 (<url>https://doi.org/10.1093/mnras/stab1680</url>)

`sat_power_data.csv` - the determined background and Saturn counts following the description in Weigt+ 2021. The Chandra ObsID and observation time are also given to allow users to search for the data files in the CXO database <url>https://cda.harvard.edu/chaser/</url>

`sat_power_upper_limit.py` - python script used to work out the 3-sigma power and flux accounting for low count regime of Saturn observations. This script can be adapted for other planetary observations by changing the observation dependent parameters (e.g., angular distance).

The GOES plotting scripts can be found <url>https://github.com/waledeigt/CXO_and_GOES_analyses.git</url>.

